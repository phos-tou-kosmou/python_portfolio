from requests.compat import urljoin
import string

def ombd_url_builder(input):

    input = string.replace(input, ' ', '+')
    base='http://www.omdbapi.com/t=' + input
