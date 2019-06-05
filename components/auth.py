import jwt
import os
import sys
import json
class Auth():
    def __init__(self):
        with open(os.path.dirname(os.path.abspath(__file__))+'/cert.json') as json_file:
            self.__data = json.load(json_file)
    
    def register(self,account,password):
        json_data = {}
        encrypt  = {}

        encrypt['username'] = account
        encrypt['password'] = password

        json_data['username'] =  account
        json_data['token'] = jwt.encode(encrypt, 'secret', algorithm='HS256').decode('utf-8')
        self.__data.append(json_data)
        return self.__save()

    def cert(self,account,password):
        for ele in self.__data:
            if ele['username'] == account and password == jwt.decode(ele['token'],'secret',algorithms=['HS256'])['password']:
                return True
        
        return False

    def __save(self):
        with open(os.path.dirname(os.path.abspath(__file__))+'/cert.json','w') as outfile:
            json.dump(self.__data,outfile)
        return True


if __name__ == '__main__':
    auth = Auth()

