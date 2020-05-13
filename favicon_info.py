import re
from dataclasses    import dataclass
from helpers        import fully_qualify_url
# A dataclass that represents a single favicon
@dataclass
class FavIcon:
    url: str
    width: int
    height: int
    
    # Uses the dimension of the image to figure out if it is less than or
    # greater than another
    def __lt__(self, other):
            return (self.width * self.height) < (other.width * other.height)


def find_favicons(site_url, soup, siteicons):

    # Get all favicons from the html
    favicons = soup.findAll("link", rel="icon")
    for favicon in favicons:
        
        # Get url and dimensions of the favicons
        icon_href = fully_qualify_url(site_url, favicon.get('href'))
        icon_size = favicon.get('sizes')

        # If we got valid sizes, then store them
        if icon_size:
            icon_size_num = [int(s) for s in re.findall(r'\d+', icon_size)]        
            f = FavIcon(icon_href, icon_size_num[0], icon_size_num[1])
        else:
            f = FavIcon(icon_href, -1, -1)
        
        # Add this favicon to a list
        siteicons.favicons.append(f)

    # Sort the favicons so we can easily get the largest
    siteicons.favicons.sort(reverse=True)

    # Put the biggest favicon in the favicon param for ease of retrieval
    if siteicons.favicon and len(siteicons.favicon) > 0:
        siteicons.favicon = siteicons.favicons[0].url

    return siteicons