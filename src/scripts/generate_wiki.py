from __future__ import print_function
import os, sys
from django.db import models
from django.apps import apps
from subprocess import call
from pygithub3 import Github
import urllib, operator, time
from JobTrak import settings
from mmg.jobtrak import *

# TODO Update milestone page generator (and move it to the Tools package) to actually write the file instead of simply outputting it to the console.

class Tool():

    WIKI_DIR = os.path.dirname(os.path.dirname(settings.BASE_DIR)) + "/JobTrak.wiki/"
    MODELGRAPH_DIR = os.path.dirname(settings.BASE_DIR) + "/doc/model_maps/"
    
    # def _print_models(self):
    # """Prints out a list of models to the console."""
    #     for app in apps.get_apps():
    #         if str(app.__package__).startswith('mmg.jobtrak'):
    #             print(" ".join(["App:", app.__package__]))
    #             for model in apps.get_models(app):
    #                 print(" ".join(["\tModel:", model._meta.object_name]))
    #                 for field in model._meta.fields:
    #                     print(" ".join(["\t\tField:", field.name, field.attname, field.get_internal_type()]))

    def get_header(self,title):
        rv = ("\n\n"+title+"\n")
        val = "="
        rv += (val * ((len(title)/len(val))+1))[:len(title)]
        return rv
        
    def generate_model_table_md(self, model):
        """Generates a markdown-formatted table of a model"""
        rv  = "| Field | Type |\n| :---- | :--: |\n"
        for field in model._meta.fields:
            rv += "| **" + field.name + "**"
            if (field.name != field.attname): # Foreign Key
                rv += " (FK)"
            rv += " | " + field.get_internal_type() + " |\n"
        return rv

    def get_rev_date(self):
        """Generates the date and time footer, displaying when the document was generated for the wiki"""
        return ''.join(["***\nUpdated: ", time.strftime("%Y-%m-%d %H:%M")])
        
    def generate_app_graphs(self):
        print(self.get_header("Generate App Model Graphs"))
        app_names=""
        for app in apps.get_apps():
            if str(app.__package__).startswith('mmg.jobtrak'):
                filename = self.MODELGRAPH_DIR + str(app.__package__).replace('.','-') + '.png'
                app_names += str(app.__package__).replace('mmg.jobtrak.','') + " "
                cmd = ['python ./manage.py graph_models ' + str(app.__package__).replace('mmg.jobtrak.','') + ' -g -o "' + filename + '"' ]
                print("--> Generating " + filename + "...")
                try:
                    retcode = call(cmd, shell=True)
                    if retcode < 0:
                        print("An error happened. Error Code:", -retcode)
                except OSError as e:
                    print("Execution failed:", e)
        filename = self.MODELGRAPH_DIR + 'all.png'
        cmd = ['python ./manage.py graph_models ' + app_names + '-g -o "' + filename + '"']
        print("--> Generating " + filename + "...")
        try:
            retcode = call(cmd, shell=True)
            if retcode < 0:
                print("An error happened. Error Code:", -retcode)
        except OSError as e:
            print("Execution failed:", e)
   
    def generate_app_and_model_docs(self):
        print(self.get_header("Generate App and Model Wiki Docs in Markdown"))
        p_filename = 'Design:-Models'
        p_content = "### Project Models\n\n"
        p_content += "\n| App | Models |\n| :----- | :----- |\n"
        for app in apps.get_apps():
            if str(app.__package__).startswith('mmg.jobtrak'):
                print("".join(["--> Processing ",str(app.__package__),"..."]))
                a_filename =''.join([
                    "App:-", app.__package__.replace('.','-').replace('mmg-jobtrak-','')
                ])
                a_content = "### App: " + app.__package__.replace('mmg.jobtrak.','') + "\n"
                a_content += "**Package**: " + str(app.__package__) + "\n\n"
                p_content += "| [["+str(app.__package__)+"|"+a_filename+"]] | "
                if len(apps.get_models(app)) > 0:
                    a_content += "| Model |\n| ----- |\n"
                    for model in apps.get_models(app):
                        m_filename=''.join([
                            "Model:-", str(app.__package__).replace(".","-").replace('mmg-jobtrak-',''),
                            "-", model._meta.object_name])
                        p_content += "[[" + model._meta.object_name + "|" + m_filename + "]] "
                        a_content += "| [[" + model._meta.object_name + "|" + m_filename + "]] |\n"
                        m_content = "### Model: " + model._meta.object_name + "\n"
                        m_content += "**Package**: " + str(app.__package__) + "\n\n"
                        m_content += "[[Back to " + app.__package__.replace('mmg.jobtrak.','') 
                        m_content += "|" + a_filename + "]]\n\n"
                        m_content += self.generate_model_table_md(model)
                        m_content += "\n\n" + self.get_rev_date()
                        print(" ".join(["    - Writing file:",m_filename+".md"]))
                        f = open(self.WIKI_DIR + m_filename + ".md", 'w')
                        f.write(m_content)
                        f.close()
                    p_content += " |\n"
                    a_content += "\n!["+str(app.__package__)+"](https://raw.githubusercontent.com/andrewmarconi/JobTrak/master/doc/model_maps/"
                    a_content += str(app.__package__).replace('.','-') + ".png)\n"
                else: # No models.
                    p_content += " (No models in this app yet) |\n"
                    a_content += "TODO: There are presently no models in this app."
                a_content += "\n\n" + self.get_rev_date()
                print(" ".join(["    - Writing file:", a_filename]))
                f = open(self.WIKI_DIR + a_filename + ".md", 'w')
                f.write(a_content)
                f.close()
            else:
                print("".join(["--> Skipping ",str(app.__package__),"..."]))
        p_content += "![](https://raw.githubusercontent.com/andrewmarconi/JobTrak/master/doc/model_maps/all.png)"
        p_content += "\n\n" + self.get_rev_date()
        f = open(self.WIKI_DIR + p_filename + ".md", 'w')
        f.write(p_content)
        f.close()

    def output_instructions(self):
        print(self.get_header("That's a wrap."))
        print("New materials have been generated. Now, be sure to:")
        print("[ ] git add in this project for all of the model_maps.")
        print("[ ] git add in the wiki project for all of the revised docs.")

def run():
    print("Running...")
    t=Tool()
    t.generate_app_and_model_docs()
    t.generate_app_graphs()
    t.output_instructions()