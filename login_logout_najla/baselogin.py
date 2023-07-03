import time
from page import loginPage
from page import link
from data import inputan 

def positive_login (driver): 
        driver.get(link.baseurl) #open demo blaze web
        #test success log in
        driver.find_element(*loginPage.clickbtn).click() #Click Log in menu on header
        time.sleep(1)
        driver.find_element(*loginPage.adduser).send_keys(inputan.validuser) #input username
        driver.find_element(*loginPage.addpass).send_keys(inputan.validpass) #input password
        driver.find_element(*loginPage.accuser).click()#click login btn
        time.sleep(1)

def negative_login_wrg_user (driver): 
        driver.get(link.baseurl) #open demo blaze web
        #test failed log in
        driver.find_element(*loginPage.clickbtn).click() #Click Log in menu on header
        time.sleep(1)
        driver.find_element(*loginPage.adduser).send_keys(inputan.invalidpass) #input username
        driver.find_element(*loginPage.addpass).send_keys(inputan.validpass) #input password
        driver.find_element(*loginPage.accuser).click()#click login btn
        time.sleep(1)

