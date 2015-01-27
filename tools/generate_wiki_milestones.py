#!/usr/bin/env python
from pygithub3 import Github
import urllib, operator, time

class GenerateWiki():
    """Class for generating wiki content. Currently only supports the dev/milestones page generation."""

    # Since we're not making changes, can just instantiate without login.
    #gh = Github('login'='andrewmarconi',password='')
    gh=Github()
    URL_BASE = "https://github.com/andrewmarconi/JobTrak/"
    URL_BASE_MS = "".join([URL_BASE,'milestones/'])

    # TODO For Future Development
    # def get_issues():
    #     issues=gh.issues.list_by_repo(user='andrewmarconi',repo='JobTrak')
    #     for i in issues.all():
    #         print "%s\t%s" % (i.number, i.title)
            
    def get_milestone_summary_table(self):
        def gen_milestone_table_head(title=""):
            """Simple table header block."""
            rvh  = "### %s\n" % (title)
            rvh += "| Milestone | Open Issues | Documentation |\n"
            rvh += "| :-------- | :---------: | :-----------: |\n"
            return rvh

        def gen_milestone_table_row(m):
            """Simple automation of generating a table row in Markdown format."""
            return "| [%s](%s) | %d of %d | [[Documentation|%s]] |\n" % (
                m['title'], self.URL_BASE_MS+urllib.quote(m['title']), 
                m['open'], m['total'], ''.join(['Milestone:-', m['title'].replace(' ','-')])
            )

        ms=self.gh.issues.milestones.list(user='andrewmarconi',repo='JobTrak',state='open')

        m_tlf=[]
        m_oth=[]

        for m in ms.all():
            m_itm={
                'title':m.title,
                'open':m.open_issues,
                'total':m.open_issues+m.closed_issues
            }
            if m.title.startswith('TLF '):
                m_tlf.append(m_itm)
            else:
                m_oth.append(m_itm)

        m_tlf=sorted(m_tlf, key=lambda k: k['title'])
        m_oth=sorted(m_oth, key=lambda k: k['title'])    

        rv = gen_milestone_table_head("Top Level Features")
        for m in m_tlf:
            rv += gen_milestone_table_row(m)
        rv += gen_milestone_table_head("Other Milestones")
        for m in m_oth:
            rv += gen_milestone_table_row(m)
        return rv

    def get_rev_date(self):
        """Generates the date and time footer, displaying when the document was generated for the wiki"""
        return ''.join(["***\n\nUpdated: ", time.strftime("%Y-%m-%d %H:%M")])

wiki_gen = GenerateWiki()
print wiki_gen.get_milestone_summary_table()
print wiki_gen.get_rev_date()
