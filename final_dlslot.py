import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
import ssl
import dataframe_image as dfi
import telegram
TELEGRAM_BOT_TOKEN = '5362509728:AAGws5rqxn4nWeAQ6x2An__YM7AdBGWNCl8'
TELEGRAM_CHAT_ID = '631331311'
PHOTO_PATH = 'C:\\Users\\SHANID\\PycharmProjects\\pythonProject\\test.png'
s = requests.Session()
proxy = '127.0.0.1:8080'
#os.environ['http_proxy'] = proxy
#os.environ['HTTP_PROXY'] = proxy
#os.environ['https_proxy'] = proxy
#os.environ['HTTPS_PROXY']= proxy
#os.environ['REQUESTS_CA_BUNDLE'] = "C:\\Users\\SHANID\\Desktop\\cacert.pem"
burp0_url = "https://sarathi.parivahan.gov.in:443/slots/dlSlotEnquiry.do?id=sardlenq"
burp0_headers = {"Referer": "https://sarathi.parivahan.gov.in/sarathiservice/stateSelectBean.do", "Connection": "close"}
burp0_request = s.get(burp0_url, headers=burp0_headers )
burp0_response = burp0_request.headers
#print(burp0_response)
Cookie = (burp0_response['Set-Cookie'])
#print(Cookie)


burp1_url = "https://sarathi.parivahan.gov.in:443/slots/stateBean.do"
burp1_headers = {"Content-Type": "application/x-www-form-urlencoded", "Referer": "https://sarathi.parivahan.gov.in/slots/stateBean.dO", "Connection": "close"}
burp1_data = {"stCode": "KL", "stName": "Kerala", "rtoCode": "KL14", "rtoName": "0"}
burp1_req = s.post(burp1_url, headers=burp1_headers, data=burp1_data )
#print(burp1_req)



burp2_url = "https://sarathi.parivahan.gov.in:443/slots/dlSlotEnquiry.do?subOffice=0&opernType=loadCOVs&trackCode=0"
burp2_headers = {"Referer": "https://sarathi.parivahan.gov.in/slots/stateBean.do", "Connection": "close"}
burp2_req =s.get(burp2_url, headers=burp2_headers)
#print(burp2_req.content)


burp3_url = "https://sarathi.parivahan.gov.in:443/slots/dlSlotEnquiry.do?subOffice=0&selectedCOVs=ANY%20COVs&opernType=checkSlotTimes"
burp3_headers = {"Referer": "https://sarathi.parivahan.gov.in/slots/stateBean.do", "Connection": "close"}
burp3_req = s.get(burp3_url, headers=burp3_headers)
#print(burp3_req.content)


burp4_url = "https://sarathi.parivahan.gov.in:443/slots/dlSlotEnquiry.do?subOffice=0&selectedCOVs=ANY%20COVs&opernType=loadDLQuotaDet&trackCode=0&trkrto=0&radioType=RTO"
burp4_headers = {"Referer": "https://sarathi.parivahan.gov.in/slots/stateBean.do", "Connection": "close"}
REQ = s.get(burp4_url, headers=burp4_headers)
DATA = REQ.content
#print(DATA)
soup = BeautifulSoup(REQ.content, 'html.parser')
table = soup.find('table', class_='table-mod1')
df = pd.read_html(str(table).upper())[0]
df.columns = df.iloc[0]
print(df)
df=df.tail(-1)
SLOT = df.loc[(df['SLOT1 (07.30-08.00)'] != '0') | (df['SLOT2 (11.00-11.30)'] != '0') | (df['SLOT3 (14.00-14.30)'] != '0') | (df['SLOT4 (15.00-15.30)'] != '0')]
print (SLOT)
if not SLOT.empty:
    dfi.export(df, 'C:\\Users\\SHANID\\PycharmProjects\\pythonProject\\test.png')
    bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)
    bot.send_message(chat_id=TELEGRAM_CHAT_ID, text="SLOT FOUND")
    bot.send_photo(chat_id=TELEGRAM_CHAT_ID, photo=open(PHOTO_PATH, 'rb'))
#send_message_url = 'https://api.telegram.org/bot{0}/sendMessage?chat_id={1}&text={3}'.format(bot_token, chat_id , df)
#send_message_response = requests.get(send_message_url)
#print(send_message_response.content)





