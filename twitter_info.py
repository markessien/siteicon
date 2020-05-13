


def find_twitter_handles(soup, siteicons):

    # Method 1: Meta-Tag Twitter:Creator
    twitter_handle = soup.find("meta", attrs={'name' : 'twitter:creator'})
    siteicons.twitter_handle = twitter_handle.get('content')
    
    return siteicons