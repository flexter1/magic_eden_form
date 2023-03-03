import random
import names
import requests
from loguru import logger
from multiprocessing import Pool
from random import choice

GoogleUrl = 'https://docs.google.com/forms/d/e/1FAIpQLScCIKXm0j4FOjttLROfB4-o4OALduPsWndVDvKc-vbvftInxQ'
urlResponse = GoogleUrl+'/formResponse'
urlReferer = GoogleUrl+'/viewform'
with open('mails.txt','r') as file:
    mails_list = [x.rstrip() for x in file.readlines()]

with open('ua.txt','r') as file:
    ua_list = [x.rstrip() for x in file.readlines()]

with open('eth.txt','r') as file:
    eth_list = [x.rstrip() for x in file.readlines()]

with open('sol.txt','r') as file:
    sol_list = [x.rstrip() for x in file.readlines()]

def register(index):
    try:
        mail = mails_list[index]
        eth = eth_list[index]
        sol = sol_list[index]
    
        data = {
            'entry.351426949': sol,
            'entry.1658522070': eth,
            'entry.1643820280':mail
        }
        resp = requests.post(urlResponse,data=data, headers={'Referer':urlReferer,'User-Agent': choice(ua_list)})
        if resp.status_code==200:
            with open('success.txt','a+') as file:
                file.writelines(f"{mail}:{sol}:{eth}\n")
                logger.success(f'{mail} | Success')
    except Exception as exc:
        logger.error(exc)



if __name__ == '__main__':
    Pool(processes=5).map(register,range(len(mails_list)))
