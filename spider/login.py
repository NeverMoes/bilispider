import requests
import http.cookiejar as cookielib
from PIL import Image
import rsa
import json
import binascii


headers = {
    "Host": "passport.bilibili.com",
    "Referer": "https://passport.bilibili.com/login",
    'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:33.0) Gecko/20100101 Firefox/33.0',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
}


session = requests.session()
session.cookies = cookielib.LWPCookieJar(filename='bilicookies')


def get_captcha():
    r = session.get('https://passport.bilibili.com/captcha')

    with open('captcha.jpg', 'wb') as f:
        f.write(r.content)
        f.close()

    im=Image.open('captcha.jpg')
    im.show()
    im.close()

    captcha = input('captcha\n >  ')
    return captcha


def encrypt(password):
    response = session.get('http://passport.bilibili.com/login?act=getkey')
    token = json.loads(response.content.decode('utf-8'))
    password = str(token['hash'] + password).encode('utf-8')
    pub_key = token['key']
    pub_key = rsa.PublicKey.load_pkcs1_openssl_pem(pub_key)
    message = rsa.encrypt(password, pub_key)
    message = binascii.b2a_base64(message)
    return message


def login():
    username = input('username\n>  ')
    passwd = input('password\n>  ')

    session.get('https://passport.bilibili.com/login')
    captcha = get_captcha()
    passwd=encrypt(passwd)

    postdata = {
        'act': 'login',
        'gourl': '',
        'keeptime': '2592000',
        'userid': username,
        'pwd': passwd,
        'vdcode': captcha,
    }

    res = session.post('https://passport.bilibili.com/login/dologin', data=postdata, allow_redirects=True)
    print(res.text)
    session.cookies.save()


login()