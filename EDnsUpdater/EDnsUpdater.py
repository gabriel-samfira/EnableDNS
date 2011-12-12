#!/usr/bin/python -d
 
import sys
import updater
import time
import signal
import gc
from PyQt4 import QtCore, QtGui
from login import Ui_Login
from main import Ui_MainWindow
from domains import Ui_DomainList
from about import Ui_About


def sigint_handler(*args):
    """Handler for the SIGINT signal."""
    QtGui.QApplication.quit()



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
        

    def run(self):
        try:
            cache = self.domains.config['cache']
        except:
            data = {'cache': {}}
            self.settings.save_cfg(data)
            self.reload_conf()

        self.count = self.update_interval
        while 1:
            if self.settings.is_configured() is False or self.settings.has_domain() is False:
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
                ret = False
                if self.get_cache('ip') is False:
                    ret = self.domains.update_ip(str(ip))
                else:
                    if str(self.domains.config['cache']['ip']) != str(ip):
                        ret = self.domains.update_ip(str(ip))
                        
                if ret is False:
                    self.count = 0
                    gc.collect()
                    continue
                    
                if str(ret) != '200':
                    self.emit(QtCore.SIGNAL("notifEvent"), ret)
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


class About(QtGui.QDialog):
    def __init__(self, data, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.p = parent
        self.ui = Ui_About()
        self.ui.setupUi(self)
        self.ui.buttonBox.button(self.ui.buttonBox.Ok).clicked.connect(self.close)
        

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
            if str(self.usr) != str(old_u):
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
            self.set_status("Incorect user/pass", "red")
        self.emit(QtCore.SIGNAL("userChanged"))


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
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.create_sys_tray()
        self.check_configs()
        self.connect_ctrls()
        self.run_loop()
    
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
        x = About(self)
        x.exec_()
                          
    def change_acct(self):
        x = MyLogin(self)
        self.connect(x, QtCore.SIGNAL("userChanged"), self.acct_callback)
        x.exec_()

    
    def change_dom(self):
        self.domains = updater.Domains()
        self.dom_data = self.domains.get_domains()
        x = myDomains(self.dom_data, parent=self)
        self.connect(x, QtCore.SIGNAL("domChanged"), self.dom_callback)
        x.exec_()
        
    def acct_callback(self):
        self.check_configs()
        self.display_info()        
        
    def dom_callback(self):
        self.check_configs()
        self.display_info()   
        return True
    
    def refresh(self):
        self.domains = updater.Domains()
        if 'cache' in self.domains.config:
            del self.domains.config['cache']
            self.domains.config.write()
        self.emit(QtCore.SIGNAL("RefreshEvent"))
        

    def check_configs(self):
        if self.settings.is_configured() is False:
            x = MyLogin(self)
            x.exec_()
            
        if self.settings.has_domain() is False:
            self.domains = updater.Domains()
            self.dom_data = self.domains.get_domains()
            x = myDomains(self.dom_data, parent=self)
            x.exec_()


    def refresh_configs(self):
        self.settings = updater.Settings()
        self.domains  = updater.Domains()

    def set_staus(self, msg1, msg2=None):
        txt = msg1
        if msg2 != None:
            txt = txt + "\n                 " + str(msg2)
        self.ui.UpStat.setText("Status:     %s" % txt)
        

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
        print msg

    def treatEvent(self, msg):
        print msg



def main():
    app = QtGui.QApplication(sys.argv)
    myapp = MainWin()
    myapp.show()
    sys.exit(app.exec_())



if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    main()
    
    
