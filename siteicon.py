# Copyright 2020 Mark Essien. All Rights Reserved.
#
# Licensed under the MIT License
# ================================================
from bs4                import BeautifulSoup
from typing             import List
from dataclasses        import dataclass
from urllib.request     import urlopen

from favicon_info import find_favicons, FavIcon
from twitter_info import find_twitter_handles

# A dataclass to store all the found site representations
@dataclass
class SiteIcons:
    favicon: str # Largest found favicon
    favicons: List[FavIcon]
    twitter_handle: str

# Simple tool that tries to get a good representation of a website

def get_site_icon(site_url):
    
    # Retrieve the site
    html = urlopen(site_url).read()
    if not html:
        return None

    # Parse the website html
    soup = BeautifulSoup(html, features="html.parser")
    if soup == None:
        return None

    # Move results into structures    
    siteicons = SiteIcons(None, [], None)
    siteicons = find_favicons(soup, siteicons)

    siteicons = find_twitter_handles(soup, siteicons)

    return siteicons

# 'https://erikbern.com/2019/12/09/hiring-at-better.html'
# https://bastian.rieck.me/blog/
# 'https://markessien.com'
siteicons = get_site_icon('https://erikbern.com/2019/12/09/hiring-at-better.html')
print(str(siteicons))