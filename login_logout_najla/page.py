from selenium.webdriver.common.by import By
# element locator for log in
class loginPage():
    clickbtn = (By.CSS_SELECTOR,"[data-target='#logInModal']")
    adduser = (By.ID,"loginusername")
    addpass = (By.ID,"loginpassword")
    accuser = (By.CSS_SELECTOR,"[onclick='logIn()']")

class link():
    baseurl = "https://www.demoblaze.com/"
