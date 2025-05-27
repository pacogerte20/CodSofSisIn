from hashlib import md5
from requests import get
from datetime import datetime

class RestMarvel:
    timestamp = datetime.now().strftime('%Y-%d%H:%M;%S')
    pub_key = '03126aa3feeb9c8fbf3aebd164f8d7d7'
    priv_key = 'aaa6e83c79f0106b5ab1654ae36dc2f32d15f957'
    

    def hash_params(self):
        hash_md5 = md5()
        hash_md5.update(f'{self.timestamp}{self.priv_key}{self.pub_key}'.encode('utf-8'))
        hashed_params = hash_md5.hexdigest()
        return hashed_params
    
    def get_heroes(self):
        params = {'ts': self.timestamp, 'apikey': self.pub_key, 'hash': self.hash_params()}
        hashed_params = hash_md5.hexdigest()
        return hashed_params
    
    def get_heroes(self):
        params = {'ts': self.timestamp, 'apikey': self.pub_key, 'hash': self.hash_params()}
        result =get('https://gateway.marvel.com:443/v1/public/characters',params=params)
        
        data = result.json()
        print(data)
        print(data['status'])
    
rest=RestMarvel()
rest.get_heroes()