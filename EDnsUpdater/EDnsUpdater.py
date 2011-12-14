#!/usr/bin/python -d
 
import sys
import os
import updater
import time
import signal
import gc
from PyQt4 import QtCore, QtGui
from login import Ui_Login
from main import Ui_MainWindow
from domains import Ui_DomainList
from about import Ui_About
from nodoms import Ui_NoDoms


try:
    settings_dir = os.path.join(os.environ['APPDATA'], "com.enabledns.updater")
except:
    settings_dir = "/tmp/com.enabledns.updater"


try:
    if os.path.isdir(settings_dir) is False:
        os.makedirs(settings_dir)
    log_file = os.path.join(settings_dir, "updater.log")
    log = open(log_file, "a", 0)
    sys.stdout = log
    sys.stderr = log
except Exception as err:
    print err
    sys.exit()
    

class authThread(QtCore.QThread):

    def __init__(self, user, psw):
        QtCore.QThread.__init__(self)
        self.u = user
        self.p = psw

    def __del__(self):
        self.wait()

    def run(self):
        self.settings = updater.Settings()
        self.domains  = updater.Domains()
        ret = self.domains.do_login(self.u,self.p)
        if ret is True:
            if self.settings.has_domain():
                del self.domains.config['domain']
                del self.domains.config['user']
                self.domains.config.write()
        self.emit(QtCore.SIGNAL("loginEvent"), ret)

    def begin(self): 
        self.start()


class updateThread(QtCore.QThread):

    def __init__(self, parent):
        QtCore.QThread.__init__(self)
        self.settings = updater.Settings()
        self.domains  = updater.Domains()
        self.p = parent
        self.connect(self.p, QtCore.SIGNAL("userChanged"), self.reload_conf)
        self.connect(self.p, QtCore.SIGNAL("domChangedT"), self.reload_conf)
        self.connect(self.p, QtCore.SIGNAL("RefreshEvent"), self.reload_conf)
        self.ip = None
        self.update_interval = 10
        

    def reload_conf(self):
        self.domains = updater.Domains()
        self.settings = updater.Settings()
        self.count = self.update_interval

    def __del__(self):
        self.wait()

    def get_cache(self, item):
        if 'cache' not in self.domains.config:
            self.domains.config['cache'] = {}
            self.domains.config.write()
        try:
            ret = self.domains.config['cache'][item]
        except:
            ret = False
        return ret
    
    def check_remote(self):
        try:
            rec_id = self.domains.config['domain']['id']
            rec_name = self.domains.config['domain']['rec_name']
        except:
            return 404
        
        ret = self.domains.get_dom_records(self.domains.config['domain']['name'])
        if type(ret) != list:
            return ret
        
        found = False
        for i in ret:
            if str(i['id']) == str(rec_id) and str(i['host']) == str(rec_name):
                found = True
                
        if found == False:
            del self.domains.config['domain']
            self.domains.config.write()
            return 404
        return True
        
    def emit_event(self, rem):
        self.count = 0
        gc.collect()
        self.emit(QtCore.SIGNAL("notifEvent"), rem)
        time.sleep(1)
        

    def run(self):
        try:
            cache = self.domains.config['cache']
        except:
            data = {'cache': {}}
            self.settings.save_cfg(data)
            self.reload_conf()
            
        if self.settings.auth_error() is True:
            self.p.set_acct("Authentication Error")            
            self.emit_event('401')
            
        self.count = self.update_interval
        while 1:
            if self.settings.needs_conf() is True:
                if self.settings.has_domain() is False:
                    self.p.set_record("UNCONFIGURED")
                if self.settings.is_configured() is False:
                    self.p.set_acct("UNCONFIGURED")
                time.sleep(1)
                gc.collect()
                continue
                
            if self.count >= self.update_interval:
                self.reload_conf()
                ip = self.domains.get_my_ip()
                if ip is None or str(ip).isdigit() is True:
                    self.count = 0
                    self.ip = "Unknown(No internet?)"
                    continue
                    
                self.ip = ip
                
                rem = self.check_remote()
                if rem is not True:
                    self.emit_event(rem)
                    continue
                
                ret = False
                if self.get_cache('ip') is False:
                    ret = self.domains.update_ip(str(ip))
                else:
                    if str(self.domains.config['cache']['ip']) != str(ip):
                        ret = self.domains.update_ip(str(ip))
                        
                if str(ret) != '200':
                    self.emit_event(ret)
                    continue
                else:
                    self.domains.config['cache']['ip'] = str(ip)
                    self.domains.config.write()
                self.count = 0
                gc.collect()
                
            self.p.set_staus("Refresh in: %s seconds" % str(self.update_interval-self.count), "Current IP: %s" % str(self.ip))
            self.count = self.count + 1
            gc.collect()
            time.sleep(1)
            

    def begin(self): 
        self.start()



class NoDoms(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.p = parent
        self.ui = Ui_NoDoms()
        self.ui.setupUi(self)
        self.connect_ctrls()
    
    def connect_ctrls(self):
        self.ui.ChangeAcct.clicked.connect(self.ch_acct)
    
    def ch_acct(self):
        self.p.change_acct()
        self.close()
    
    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_Escape:
            if self.p.settings.is_configured() is False:
                sys.exit()
            else:
                self.close()
    
    def closeEvent(self, event):
        if self.p.settings.is_configured() is False:
            sys.exit()
        else:
            event.accept()


class About(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.p = parent
        self.ui = Ui_About()
        self.ui.setupUi(self)
        self.ui.buttonBox.button(self.ui.buttonBox.Ok).clicked.connect(self.close)
    
    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_Escape:
            self.close()
        


class myDomains(QtGui.QDialog):
    def __init__(self, data, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.p = parent
        self.ui = Ui_DomainList()
        self.ui.setupUi(self)
        self.populate_tree(data)
        self.connect_ctrls()
        
    def connect_ctrls(self):
        self.ui.ok.clicked.connect(self.set_domain)
        
    def set_domain(self):
        rec = self.ui.Domains.currentItem()
        if rec != None:
            self.dom_name = rec.text(0)
            self.rec_name = rec.text(1)
            self.rec_id = rec.text(2)
            data = {'domain': {'name': self.dom_name, 'rec_name': self.rec_name, 'id': self.rec_id}}
            if 'cache' in self.p.domains.config:
                del self.p.domains.config['cache']
                self.p.domains.config.write()
            self.p.settings.save_cfg(data)
            self.p.emit(QtCore.SIGNAL("domChangedT"))
            self.emit(QtCore.SIGNAL("domChanged"))
            self.close()
        
    def populate_tree(self, data):
        count = 0
        for i in data:
            x = QtGui.QTreeWidgetItem(self.ui.Domains)
            self.ui.Domains.topLevelItem(count).setText(0, QtGui.QApplication.translate("DomainList", str(i['zone_name']), None, QtGui.QApplication.UnicodeUTF8))
            self.ui.Domains.topLevelItem(count).setText(1, QtGui.QApplication.translate("DomainList", str(i['rec']) , None, QtGui.QApplication.UnicodeUTF8))
            self.ui.Domains.topLevelItem(count).setText(2, QtGui.QApplication.translate("DomainList", str(i['id']), None, QtGui.QApplication.UnicodeUTF8))
            count = count + 1

    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_Escape:
            if self.p.settings.has_domain() is False:
                sys.exit()
            else:
                self.close()
    
    def closeEvent(self, event):
        if self.p.settings.has_domain() is False:
            sys.exit()
        else:
            event.accept()


class MyLogin(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.p = parent
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.connect_ctrls()
        if self.p.settings.is_configured() is True:
            self.ui.username.setText(self.p.domains.config['user']['username'])
            self.ui.password.setText(self.p.domains.config['user']['password'])
        
    def connect_ctrls(self):
        self.ui.Buttons.button(self.ui.Buttons.Save).clicked.connect(self.try_login)
        self.ui.Buttons.button(self.ui.Buttons.Cancel).clicked.connect(self.close)
    
    def set_status(self, text, color):
        self.ui.status.setText(str(text))
        self.ui.status.setStyleSheet("#status { color : %s; }" % str(color));
    
        
    def start_thread(self):
        self.ui.Buttons.button(self.ui.Buttons.Save).setEnabled(False)
        self.ui.Buttons.button(self.ui.Buttons.Cancel).setEnabled(False)
        self.loginT = authThread(self.usr, self.psw)
        self.set_status("Authenticatig...", "blue")
        self.loginT.begin()
        self.connect(self.loginT, QtCore.SIGNAL("loginEvent"), self.h_rsp)
    
    
    def try_login(self):
        self.usr = self.ui.username.text()
        self.psw = self.ui.password.text()
        
        if self.p.settings.is_configured() is True:
            old_u = self.p.domains.config['user']['username']
            old_p = self.p.domains.config['user']['password']
            if str(self.usr) != str(old_u) or str(self.psw) != str(old_p):
                self.start_thread()
            else:
                self.close()
        else:
            self.start_thread()
        
    
    def h_rsp(self, rsp):
        if rsp == True:
            data = {'user': {'username': str(self.usr), 'password': str(self.psw)}}
            try:
                self.set_status("Success", "green")
                self.p.settings.save_cfg(data)
                self.p.domains = updater.Domains()
                self.set_status("Retrieving domain list, please wait...", "green")
                self.p.dom_data = self.p.domains.get_domains()
                self.close()
            except:
                self.set_status("Failed to write config :(", "red")
        else:
            self.ui.Buttons.button(self.ui.Buttons.Save).setEnabled(True)
            self.ui.Buttons.button(self.ui.Buttons.Cancel).setEnabled(True)
            txt = self.p.get_code_text(rsp)
            self.set_status(str(txt), "red")
        self.emit(QtCore.SIGNAL("userChanged"))


    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_Escape:
            if self.p.settings.is_configured() is False:
                sys.exit()
            else:
                self.close()


    def closeEvent(self, event):
        if self.p.settings.is_configured() is False:
            sys.exit()
        else:
            event.accept()

    
    
class MainWin(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.settings = updater.Settings()
        self.domains  = updater.Domains()
        self.dom_data = []
        self.codes =    {
                            '401' : 'Incorrect user/pass, or no API access.',
                            '404' : 'Could not find domain/record',
                            '500' : 'A server error has occurred',
                        }
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.create_sys_tray()
        self.check_configs()
        self.connect_ctrls()
        self.run_loop()
    
    
    def get_code_text(self, code):
        try:
            txt = self.codes[str(code)]
        except:
            txt = "Unknown error occured. Please Try again later."
        return txt
        
    
    def stub(self):
        print 111
    
    def connect_ctrls(self):
        self.ui.ch_acct.clicked.connect(self.change_acct)
        self.ui.ch_dom.clicked.connect(self.change_dom)
        self.ui.refresh.clicked.connect(self.refresh)
        self.connect(self.ui.actionHide, QtCore.SIGNAL('triggered()'), self.hide)
        self.connect(self.ui.actionQuit_2, QtCore.SIGNAL('triggered()'), sys.exit)
        self.connect(self.ui.actionAbout, QtCore.SIGNAL('triggered()'), self.about)
        
       
    def about(self):
        x = About(parent=self)
        x.exec_()
                          
    def change_acct(self):
        x = MyLogin(self)
        self.connect(x, QtCore.SIGNAL("userChanged"), self.acct_callback)
        x.exec_()

    
    def change_dom(self):
        self.domains = updater.Domains()
        try:
            del self.domains.config['domain']
            self.domains.config.write()
        except:
            pass
        self.dom_data = self.domains.get_domains()
        if len(self.dom_data) > 0:
            x = myDomains(self.dom_data, parent=self)
            self.connect(x, QtCore.SIGNAL("domChanged"), self.dom_callback)
        else:
            x = NoDoms(parent=self)
        x.exec_()
        
        
    def acct_callback(self):
        self.check_configs()
        self.display_info()        
        
        
    def dom_callback(self):
        self.check_configs()
        self.display_info()   
    
    
    def refresh(self):
        self.domains = updater.Domains()
        if 'cache' in self.domains.config:
            del self.domains.config['cache']
            self.domains.config.write()
        self.emit(QtCore.SIGNAL("RefreshEvent"))
        
        
    def get_cache(self):
        try:
            self.cache = self.domains.config['cache']
        except:
            self.domains.config['cache'] = {}
            self.domains.config.write()
            self.cache = {}
        return self.cache
        

    def check_configs(self):
        self.refresh_configs()
        if self.settings.is_configured() is False:
            x = MyLogin(self)
            x.exec_()
        if self.settings.has_domain() is False:
            self.domains = updater.Domains()
            self.dom_data = self.domains.get_domains()
            if len(self.dom_data) > 0:
                x = myDomains(self.dom_data, parent=self)
            else:
                x = NoDoms(parent=self)
            x.exec_()


    def refresh_configs(self):
        self.settings = updater.Settings()
        self.domains  = updater.Domains()

    def set_staus(self, msg1, msg2=None):
        txt = msg1
        if msg2 != None:
            txt = txt + "\n                 " + str(msg2)
        self.ui.UpStat.setText("Status:     %s" % txt)
        
    def set_record(self, msg1, msg2=None):
        txt = msg1
        if msg2 != None:
            txt = txt + "\n                 " + str(msg2)
        self.ui.DomInfo.setText("Record:   %s" % txt)
     
    def set_acct(self, msg1, msg2=None):
        txt = msg1
        if msg2 != None:
            txt = txt + "\n                 " + str(msg2)
        self.ui.AcctInfo.setText("Account: %s" % txt)

    def display_info(self):
        self.refresh_configs()
        rec_name = self.domains.config['domain']['rec_name']
        if rec_name == '@':
            dsp_rec = self.domains.config['domain']['name']
        else:
            dsp_rec = rec_name + "." + self.domains.config['domain']['name']
            
        self.ui.AcctInfo.setText("Account: %s" % str(self.domains.config['user']['username']))
        self.ui.DomInfo.setText("Record:   %s" % str(dsp_rec))
        

    def run_loop(self):
        self.updateT = updateThread(self)
        self.display_info()
        self.updateT.begin()
        self.connect(self.updateT, QtCore.SIGNAL("notifEvent"), self.treatEvent)
        self.connect(self.updateT, QtCore.SIGNAL("notifIPEvent"), self.treatIPEvent)


    def create_sys_tray(self):
        self.sysTray = QtGui.QSystemTrayIcon(self)
        menu = QtGui.QMenu()
        exit = menu.addAction("Exit")
        self.sysTray.setContextMenu(menu)
        self.connect(exit, QtCore.SIGNAL('triggered()'), sys.exit)
        self.sysTray.setIcon( QtGui.QIcon(':/updater/icon.png') )
        self.sysTray.setVisible(True)
        self.connect(self.sysTray, QtCore.SIGNAL("activated(QSystemTrayIcon::ActivationReason)"), self.on_sys_tray_activated)

        self.sysTrayMenu = QtGui.QMenu(self)
        act = self.sysTrayMenu.addAction("FOO")

    def on_sys_tray_activated(self, reason):     
        if reason == 3:   
            if self.isVisible ():
                self.setVisible(False)
            else:
                self.setVisible(True)
                

    def treatIPEvent(self, msg):
        print "IP event: " + str(msg)


    def treatEvent(self, msg):
        if str(msg) == '401':
            cache = self.get_cache()
            self.domains.config['cache']['auth_err'] = True
            self.domains.config.write()
            self.change_acct()
        if str(msg) == '404':
            self.change_dom()

    def closeEvent(self, event):
        if self.isVisible():
            self.setVisible(False)
        event.ignore()
            


def main():
    app = QtGui.QApplication(sys.argv)
    myapp = MainWin()
    if len(sys.argv) > 1 and str(sys.argv[1]) == 'show':
        myapp.show()
    sys.exit(app.exec_())



if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    main()
    
    
