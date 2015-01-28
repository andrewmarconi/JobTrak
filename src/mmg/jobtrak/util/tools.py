from __future__ import print_function
import os
from django.db import models
from django.apps import apps
from pygithub3 import Github
import urllib, operator, time
from JobTrak import settings
from mmg.jobtrak import *

# mmg.jobtrak.util.tools
class Tool():
    
    # X._meta.object_name gives the object name
    # X._meta.verbose_name gives the human readable name
    # X._meta.get_all_field_names() - all the fields
    # X._meta.get_internal_type() - type of field
    # X._meta.attname - attribute name
    # X._meta.name - name can retrieve by (if the two match, it's a local field, otherwise it's a related field)
    
    def print_models(self):
        for app in apps.get_apps():
            if str(app.__package__).startswith('mmg.jobtrak'):
                print(" ".join(["App:", app.__package__]))
                for model in apps.get_models(app):
                    print(" ".join(["\tModel:", model._meta.object_name]))
                    for field in model._meta.fields:
                        print(" ".join(["\t\tField:", field.name, field.attname, field.get_internal_type()]))

    def generate_model_table_md(self, model):
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
        
    def generate_model_docs(self):
        WIKI_DIR = os.path.dirname(os.path.dirname(settings.BASE_DIR)) + "/JobTrak.wiki/"
        for app in apps.get_apps():
            if str(app.__package__).startswith('mmg.jobtrak'):
                print("".join(["--> Processing ",str(app.__package__),"..."]))
                a_filename =''.join([
                    "App:-",
                    app.__package__.replace('.','-').replace('mmg-jobtrak-',''),
                    ".md"
                ])
                a_content = "### App: " + app.__package__.replace('mmg.jobtrak.','') + "\n"
                a_content += "**Package**: " + str(app.__package__) + "\n\n"
                if len(apps.get_models(app)) > 0:
                    a_content += "| Model |\n| ----- |\n"
                    for model in apps.get_models(app):
                        m_filename=''.join([
                            "Model:-",
                            str(app.__package__).replace(".","-").replace('mmg-jobtrak-',''),
                            "-",
                            model._meta.object_name,
                            ".md"
                        ])
                        a_content += "| [[" + model._meta.object_name + "|" + m_filename + "]] |\n"
                        m_content = "### Model: " + app.__package__.replace('mmg.jobtrak.','') + "\n"
                        m_content += "**Package**: " + app.__package__ + "\n"
                        m_content += "[[Back to App|" + a_filename + "]]\n\n"
                        m_content += self.generate_model_table_md(model)
                        m_content += "\n\n" + self.get_rev_date()
                        print(" ".join(["    - Writing file:",m_filename]))
                        f = open(WIKI_DIR + m_filename, 'w')
                        f.write(m_content)
                        f.close()
                else: # No models.
                    a_content += "TODO: There are presently no models in this app."
                a_content += "\n\n" + self.get_rev_date()
                print(" ".join(["    - Writing file:", a_filename]))
                f = open(WIKI_DIR + a_filename, 'w')
                f.write(a_content)
                f.close()
            else:
                print("".join(["--> Skipping ",str(app.__package__),"..."]))
