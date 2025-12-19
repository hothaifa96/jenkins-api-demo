import requests

url = "localhost:5005/api"

def sanity_test():
    res = requests.get(url=f'{url}/rates')
    if res.status_code != 200:
        raise Exception('not ready for PRD')
    
