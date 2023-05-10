import requests
import hashlib

#  funtion to request API data 
def request_api_data(query_char):
    
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check the api and try again')
    return res

    

def pwned_api_data(password):
    # check password if it exists in API response
    sha1password = (hashlib.sha1(password.encode('utf-8')).hexdigest().upper())
    return sha1password
request_api_data('123')