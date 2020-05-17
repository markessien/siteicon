# Copyright 2020 Mark Essien. All Rights Reserved.
#
# Licensed under the MIT License
# ================================================

import json

from bs4                import BeautifulSoup
from typing             import List
from dataclasses        import dataclass
from urllib.request     import urlopen
from flask import request

from flask import Flask
app = Flask(__name__)

from favicon_info import find_favicons, FavIcon
from twitter_info import find_twitter_handles
from generate_icon import generate_icon
from flask import render_template
from dataclasses_json import dataclass_json

# A dataclass to store all the found site representations
@dataclass_json
@dataclass
class SiteIcons:
    favicon: str # Largest found favicon
    favicons: List[FavIcon]
    twitter_handle: str
    twitter_id: str

    def best_option(self):
        if self.favicon:
            return self.favicon

        return None

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
    siteicons = SiteIcons(None, [], None, None)
    siteicons = find_favicons(site_url, soup, siteicons)

    siteicons = find_twitter_handles(soup, siteicons)

    return siteicons

def create_icon():
    relevant_text = "hi world"
    return generate_icon(relevant_text)

# Tough one: https://saagarjha.com/blog/ 
# 'https://erikbern.com/2019/12/09/hiring-at-better.html'
# https://bastian.rieck.me/blog/
# 'https://markessien.com'
# https://macwright.org/2020/05/10/spa-fatigue.html
# https://superorganizers.substack.com/p/stop-trying-to-make-hard-work-easy
# siteicons = get_site_icon('https://saagarjha.com/blog')
# print(str(siteicons))

# i f siteicons.best_option() == None:
    # We could not find anything. Let's make one
#     create_icon()


@app.route('/api/')
def api(methods=['GET', 'POST']):
    site_url = request.args.get('site_url')
    if site_url == None or site_url == "":
        return json.dumps({"result_code" : 0, "result_text" : "No URL specified"})

    print(site_url)
    siteicons = get_site_icon(site_url)
    result = {"result_code" : 1, "result_text" : "Success", "result" : siteicons.to_dict()}
    return result

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')