import requests
from Crypto.Cipher import AES
import base64
from random import randrange
from bs4 import BeautifulSoup
import urllib3
import re
import time
import datetime
import json
import argparse


class DaKa:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.key = None
        self.aes_crypt = None
        self.base_url = "https://wxxy.csu.edu.cn/ncov/wap/default/index"
        self.login_url = "https://ca.csu.edu.cn/authserver/login?service=https%3A%2F%2Fwxxy.csu.edu.cn%2Fa_csu%2Fapi%2Fcas%2Findex%3Fredirect%3Dhttps%253A%252F%252Fwxxy.csu.edu.cn%252Fncov%252Fwap%252Fdefault%252Findex%26from%3Dwap"
        self.save_url = "https://wxxy.csu.edu.cn/ncov/wap/default/save"
        self.info = None
        self.sess = requests.Session()

    def login(self):
        def __login_passwd_aes(mode=AES.MODE_CBC):
            def __random_str(num):
                chars = "ABCDEFGHJKMNPQRSTWXYZabcdefhijkmnprstwxyz2345678"
                return ''.join([chars[randrange(len(chars))] for i in range(num)])

            passwd_with_salt, iv = __random_str(64) + self.password, __random_str(16)
            self.aes_crypt = AESCrypt(self.key, mode, iv, passwd_with_salt)
            return self.aes_crypt.encrypt()

        try:
            login_res = self.sess.get(self.base_url, allow_redirects=True)
            login_html = login_res.content.decode()
            login_soup = BeautifulSoup(login_html, "html.parser")
            login_form = login_soup.find("form", id="pwdFromId")
            self.key = login_form.find("input", id="pwdEncryptSalt")['value']
            login_data = {
                "username": self.username,
                "password": __login_passwd_aes(),
                "captcha": '',
                "rememberMe": login_form.find("input", id="rememberMe")['value'],
                "_eventId": login_form.find("input", id="_eventId")['value'],
                "cllt": login_form.find("input", id="cllt")['value'],
                "dllt": login_form.find("input", id="dllt")['value'],
                "lt": login_form.find("input", id="lt")['value'],
                "execution": login_form.find("input", id="execution")['value']
            }
            self.sess.post(self.login_url, data=login_data, allow_redirects=True)  # session中cookies单点登录相关的key改变
        except Exception as e:
            print("中南大学统一登录过程出错")
            exit(1)

    def get_info(self):
        def __get_date():
            today = datetime.date.today()
            return "%4d%02d%02d" % (today.year, today.month, today.day)

        urllib3.disable_warnings()
        res1 = self.sess.get(self.base_url, verify=False)
        content1 = res1.content.decode()
        data1 = re.findall(r'def = {[\s\S]*?};', content1)[0]

        jsontext = eval(data1[data1.find("{"):data1.rfind(";")].replace(" ", ""))
        geo_text = jsontext['geo_api_info']
        geo_text = geo_text.replace("false", "False").replace("true", "True")
        geo_obj = eval(geo_text)['addressComponent']
        area = geo_obj['province'] + " " + geo_obj['city'] + " " + geo_obj['district']
        name = re.findall(r'realname: "([^\"]+)",', content1)[0]
        number = re.findall(r"number: '([^\']+)',", content1)[0]

        new_info = jsontext.copy()
        new_info['name'] = name
        new_info['number'] = number
        new_info['area'] = area
        new_info["date"] = __get_date()
        new_info["created"] = round(time.time())
        new_info['city'] = geo_obj['city']
        new_info['address'] = eval(geo_text)['formattedAddress']
        self.info = new_info

    def post(self):
        res = self.sess.post(self.save_url, data=self.info)
        return json.loads(res.text)


def main(username, password):
    print("1. 启动打卡程序")
    dk = DaKa(username, password)
    print("2. 进行单点登录")
    dk.login()
    print("3. 获取打卡信息")
    dk.get_info()
    print("4. 准备为%s同学打卡" % dk.info['name'])
    res = dk.post()
    if str(res['e']) == '0':
        print('☑︎为%s打卡成功' % dk.info['name'])
    else:
        print('☒%s' % res['m'])


class AESCrypt:
    """
    csu encrypt.js实现过程如下：
    function getAesString(data, key0, iv0) {
        key0 = key0.replace(/(^\s+)|(\s+$)/g, "");
        var key = CryptoJS.enc.Utf8.parse(key0);
        var iv = CryptoJS.enc.Utf8.parse(iv0);
        var encrypted = CryptoJS.AES.encrypt(data, key, {
            iv: iv,
            mode: CryptoJS.mode.CBC,
            padding: CryptoJS.pad.Pkcs7
        });
        return encrypted.toString();
    }
    function encryptAES(data, aesKey) {
        if (!aesKey) {
            return data;
        }
        var encrypted = getAesString(randomString(64) + data, aesKey, randomString(16));
        return encrypted;
    }
    var $aes_chars = 'ABCDEFGHJKMNPQRSTWXYZabcdefhijkmnprstwxyz2345678';
    var aes_chars_len = $aes_chars.length;
    function randomString(len) {
        var retStr = '';
        for (i = 0; i < len; i++) {
            retStr += $aes_chars.charAt(Math.floor(Math.random() * aes_chars_len));
        }
        return retStr;
    }
    """

    def __init__(self, key, mode, iv, data):
        self.key = key.encode('utf-8')
        self.mode = mode
        self.iv = iv.encode('utf-8')
        self.data = self.pkcs7(data)
        self.cipher = AES.new(self.key, self.mode, self.iv)
        self.encryptedStr = None

    def encrypt(self):
        self.encryptedStr = base64.b64encode(self.cipher.encrypt(self.data))
        return self.encryptedStr

    def pkcs7(self, data, block_num=16):
        """
        填充规则：如果长度不是block_num的倍数，余数使用余数进行补齐
        :return:
        """
        pad = block_num - len(data.encode('utf-8')) % block_num
        data = data + pad * chr(pad)
        return data.encode('utf-8')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--username', type=str, default=None)
    parser.add_argument('--password', type=str, default=None)
    args = parser.parse_args()
    main(args.username, args.password)
