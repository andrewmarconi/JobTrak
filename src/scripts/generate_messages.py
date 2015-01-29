from __future__ import print_function
#from django.db import models
#from django.apps import apps
from subprocess import call
#from pygithub3 import Github
#import urllib, operator, time
#from mmg.jobtrak import *
import os
from JobTrak import settings

class GenerateMessages:
    APPS_DIR = os.path.join(settings.BASE_DIR,'mmg','jobtrak')
    MANAGE_APP = os.path.join(settings.BASE_DIR,"manage.py")
    TX_CONFIG = os.path.join(os.path.dirname(settings.BASE_DIR),".tx","config")
    
    def run_command(self,cmd,msg_ok="OK!",msg_err="An error happened."):
        print(self.get_header("Generating Global Project Message Files"))
        os.chdir(settings.BASE_DIR)
        cmd = ['python ' + self.MANAGE_APP + " makemessages -a --no-wrap"]
        try:
            retcode = call(cmd, shell=True)
            if retcode < 0:
                print(msg_err,"Error Code:", -retcode)
            else:
                print(msg_ok)
        except OSError as e:
            print(msg_err,"Execution Failed:", e)
        
    def get_header(self,title):
        rv = ("\n"+title+"\n")
        val = "="
        rv += (val * ((len(title)/len(val))+1))[:len(title)]
        return rv
        
    def make_messages(self):
        print(self.get_header("Generating Global Project Message Files"))

        os.chdir(settings.BASE_DIR)
        cmd = ['python ' + self.MANAGE_APP + " makemessages -a --no-wrap"]
        try:
            retcode = call(cmd, shell=True)
            if retcode < 0:
                print("An error happened. Error Code:", -retcode)
            else:
                print("OK!")
        except OSError as e:
            print("Execution failed:", e)

        print(self.get_header("--> Generating Messages by App"))
        apps_list = os.listdir(self.APPS_DIR)
        for app in apps_list:
            app_path = os.path.join(self.APPS_DIR,app)
            if os.path.isdir(app_path):
                print("* Generating messages for the",app,"app...")
                locale_path = os.path.join(app_path, "locale")
                if(os.path.exists(locale_path)):
                    os.chdir(app_path)
                    cmd = ['python ' + self.MANAGE_APP + " makemessages -a --no-wrap"]
                    try:
                        retcode = call(cmd, shell=True)
                        if retcode < 0:
                            print("An error happened. Error Code:", -retcode)
                        else:
                            print("OK!")
                    except OSError as e:
                        print("Execution failed:", e)
                else:
                    print("DIRECTORY DOESN'T EXIST", os.path.join(app_path,"locale"))
                        

    def pushpull_trans(self):
        print(self.get_header("Interacting with Transifex"))
        self.run_command(
            ['tx push-s'], 
            msg_ok="Successfully pussed new tokens to Transifex.")
        self.run_command(
            ['tx pull -a'],
            msg_ok="Successfully pulled new translations from Transifex."
        )
        
    def compile_messages(self):
        print(self.get_header("Compiling Messages"))
        self.run_command(
            ['python ' + self.MANAGE_APP + " compilemessages"],
            msg_ok="Messages all compiled. Be sure to check in the .po language files to git.")

def run():
    g=GenerateMessages()
    if os.path.isfile(g.TX_CONFIG):
        g.make_messages()
        g.pushpull_trans()
        g.compile_messages()
    else:
        print("--> Skipping language file management, since it's not configured.")
        print("    You need the Transifex client configured. Visit this Web site")
        print("    for more info: http://docs.transifex.com/developer/client/")


#         echo "    - Pushing source language to Transifex..."
#         tx push -s
#         echo "    - Pulling translated languages from Transifex..."
#         tx pull -a
#         echo "    - Compiling language files into .mo archives..."
#         
#     fi
#
#
# def run():
#     g=GenerateMessages()
#     g.make_messages_by_app()
#

#    g.output_instructions()
