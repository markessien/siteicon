# Copyright 2020 Mark Essien. All Rights Reserved.
#
# Licensed under the MIT License
# ================================================
import re

from bs4 import BeautifulSoup
from urllib.request import urlopen
from dataclasses import dataclass


@dataclass
class SiteIcons:
    favicon: str # Largest found favicon
    favicon_16: str
    favicon_32: str

# Simple tool that tries to get a good representation of a website

def get_site_icon(site_url):
    
    html = urlopen(site_url).read()
    if not html:
        return None
    
    # print(html)

    siteicons = SiteIcons(None, None, None)
    soup = BeautifulSoup(html, features="html.parser")
    favicons = soup.findAll("link", rel="icon")
    for favicon in favicons:
        icon_href = favicon.get('href')
        icon_size = favicon.get('sizes')

        if icon_size:
            nums = [int(s) for s in re.findall(r'\d+', icon_size)]
            num = nums[0]
            if num == 32:
                siteicons.favicon_32 = icon_href
            elif num == 16:
                siteicons.favicon_16 = icon_href
        else:
            siteicons.favicon = icon_href

        if siteicons.favicon_32 and not siteicons.favicon:
            siteicons.favicon = siteicons.favicon_32

        if siteicons.favicon_16 and not siteicons.favicon:
            siteicons.favicon = siteicons.favicon_16

    return siteicons

siteicons = get_site_icon('https://markessien.com')
print(str(siteicons))