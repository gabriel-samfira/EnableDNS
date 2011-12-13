#!/usr/bin/env python

import requests
import sys
from configobj import ConfigObj
import json
import os
import sys
import getpass
import time


class Domains():

    def __init__(self):
        self.url = 'https://enabledns.com/api/domains'
        self.export_url = 'https://enabledns.com/api/export.json'
        self.config = Settings().get_config()


    @classmethod
    def do_login(cls, username, password):
        x = 'https://enabledns.com/api/domains.json'
        data = requests.get(x, auth=(username, password))
        if str(data.status_code) != '200':
            return data.status_code
        return True
        
        
    def get_my_ip(self):
        try:
            ip = requests.get('https://enabledns.com/ip')
        except:
            return None
        if str(ip.status_code) != '200':
            return ip.status_code
        return ip.content

    def format_response(self, data):
        resp = []
        for i in data.keys():
            for j in data[i]:
                if j['type'] == 'A':
                    resp.append({'id': j['id'], 'rec': j['host'], 'zone_name': i})
        return resp
                

    def get_domains(self):
        x = self.export_url
        data = requests.get(x, auth=(self.config['user']['username'], self.config['user']['password']))
        rr = data.status_code
        if str(rr) != '200':
            return rr
        
        try:
            rec = json.loads(data.content)
        except Exception as err:
            print ("Got invalid data from server. Please try again later: %s" % str(err))
            return False
        
        return self.format_response(rec)
        

    def get_dom_records(self, dom):
        x = self.url +  '/' + str(dom) + '.json'
        data = requests.get(x, auth=(self.config['user']['username'], self.config['user']['password']))
        rr = data.status_code
        if str(rr) != '200':
            return rr
        
        try:
            rec = json.loads(data.content)
        except Exception as err:
            print("Got invalid data from server. Please try again later: %s" % str(err))
            return False
            
        tmp = []
        for i in rec:
            if str(i['type']) == 'A':
                tmp.append(i)
                
        return tmp
        

    def create_entry(self, ent):
        self.ip = self.get_my_ip()
        rec_data = {'host': str(ent), 'ttl': 600, 'type': 'A', 'data': str(self.ip)} 
        x = self.url + '/' + self.config['domain']['name'] + '.json'
        hdr = {'Content-type': 'application/json'}
        data = requests.post(x, auth=(self.config['user']['username'], self.config['user']['password']), headers=hdr, data=json.dumps(rec_data))
        if str(data.status_code) != '200':
            return data.status_code
        return True

    def get_record_info(self, ip):
        try:
            rec = self.config['domain']['id']
        except Exception as err:
            raise Exception("No record information found in config")
            
        return[{'id': int(rec), 'data': str(ip)}]
            

    def update_ip(self, ip):
        try:
            rec_info = self.get_record_info(ip)
        except:
            return '404'
        x = self.url + '/' + self.config['domain']['name'] + '.json'
        hdr = {'Content-type': 'application/json'}
        tmp = requests.put(x, auth=(self.config['user']['username'], self.config['user']['password']), data=json.dumps(rec_info), headers=hdr)
        
        return tmp.status_code

        
class Settings():

    def __init__(self):
        try:
            self.settings_dir = os.path.join(os.environ['APPDATA'], "com.enabledns.updater")
        except:
            self.settings_dir = "/tmp/com.enabledns.updater"
        self.cfg = os.path.join(self.settings_dir, "config.ini")

    def is_configured(self):
        cfg = self.get_config()
        if cfg is False:
            return cfg
        try:
            cfg['user']['username']
        except:
            return False
        return os.path.isfile(self.cfg)

    def save_cfg(self, data):
        self.create_configs()
        if os.path.isfile(self.cfg) is False:
            x = ConfigObj()
            x.filename = self.cfg
        else:
            try:
                x = ConfigObj(self.cfg)
            except Exception as err:
                raise Exception("Failed to parse config file")
        x.merge(data)
        x.write()
        return True

        
    def get_config(self):
        if os.path.isfile(self.cfg) is False:
            return False
        
        cfg = ConfigObj(self.cfg)
        return cfg
    
    def has_domain(self):
        cfg = self.get_config()
        try:
            ret = cfg['domain']['id']
        except:
            ret = False
        return ret
    
    def auth_error(self):
        cfg = self.get_config()
        try:
            ret = cfg['cache']['auth_err']
            ret = True
        except:
            ret = False
        return ret
    
    def needs_conf(self):
        if self.has_domain() is False or self.is_configured() is False or self.auth_error() != False:
            return True
        return False
    
    def create_configs(self):
        if os.path.isdir(self.settings_dir) is False:
            try:
                os.makedirs(self.settings_dir)
            except Exception as err:
                raise Exception("Failed to create settings directory: %s" % str(self.settings_dir))
        return True
