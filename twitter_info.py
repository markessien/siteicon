


def find_twitter_handles(soup, siteicons):

    # Method 1: Meta-Tag Twitter:Creator
    twitter_handle = soup.find("meta", attrs={'name' : 'twitter:creator'})
    if twitter_handle:
        siteicons.twitter_handle = twitter_handle.get('content')
        return siteicons

    # Method 2: Twitter ID is specified
    twitter_id = soup.find("meta", attrs={'property' : 'twitter:account_id'})
    if twitter_id:
        siteicons.twitter_id = twitter_id.get('content')
        # https://twitter.com/intent/follow?user_id=<id here> <-- can be used to get photo later
        return siteicons

    
    return siteicons