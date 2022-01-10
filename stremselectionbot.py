import requests
import lxml
from bs4 import BeautifulSoup as bs
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'
}

with requests.Session() as s:
    def getSession():
        response = s.get('https://epprd.mcmaster.ca/psp/prepprd/EMPLOYEE/EMPL/?cmd=logout', headers=headers)
        if response.status_code == 200:
            print('Getting Session...')
        else:
            print('Error')
    def logIn():
        user=input("please input your username: ")
        password=input("Please input your password: ")
        logIn_data = {
            'userid': user, #### Input Username
            'pwd': password ##### Input Password
        }
        response = s.post('https://epprd.mcmaster.ca/psp/prepprd/EMPLOYEE/EMPL/?&cmd=login&languageCd=ENG', headers=headers, data=logIn_data)
        if response.status_code == 200:
            print('Logging-In...')
        else:
            print('Error')

    def studentCenter():
        response = s.get('https://epprd.mcmaster.ca/psp/prepprd/EMPLOYEE/SA/c/SA_LEARNER_SERVICES.SSS_STUDENT_CENTER.GBL',headers=headers)

    def getResult():
        response = s.get('https://csprd.mcmaster.ca/psc/prcsprd/EMPLOYEE/SA/c/SA_LEARNER_SERVICES.SSS_MY_ACAD.GBL?Page=SSS_MY_ACAD&Action=U&ExactKeys=Y', headers=headers)
        if response.status_code == 200:
            print('Getting Result...')
        else:
            print('Error')
        text_soup = bs(response.content, 'lxml')
        result_html = str(text_soup.find_all('span', attrs={'id':"#ICSetFieldSSS_MY_ACAD.TREECNTRLFIELD1.S4"})[0])
        result = result_html.split('">')[1].split('</')[0]
        while True:
            if 'Intgr' in result:
                print('Waiting for Results...')
                time.sleep(2)
                getResult()
            else:
                print('Your stream: '+ result)
                break


    getSession()
    logIn()
    studentCenter()
    getResult()
