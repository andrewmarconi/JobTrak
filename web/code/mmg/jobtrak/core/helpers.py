from mmg.jobtrak.links.models import *
from mmg.jobtrak.core.models import *
from bs4 import BeautifulSoup as bs
import certifi
import urllib3
import re

def get_listing_from_url(url):
    http = urllib3.PoolManager(
        cert_reqs='CERT_REQUIRED',
        ca_certs=certifi.where()
    )
    r = http.request( 'GET', url )
    if r.status==200:
        # good results
    else:
        # else


# https:\/\/authenticjobs.com\/jobs\/([0-9])\w+\/(([a-z])\w+\-).+
