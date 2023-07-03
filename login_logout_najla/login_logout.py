# Run The Test HERE!
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import baselogin

#Successful Login And Logout Test
class test_login_logout(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
   
    def test_login_logout_success(self): 
        driver =self.browser
         #Log In
        baselogin.positive_login(driver)
        # validasi Log in
        response_data = driver.find_element(By.ID,"cat").text
        self.assertIn('CATEGORIES', response_data)
        time.sleep(1)


        #test success log out
        driver.find_element(By.CSS_SELECTOR,"[onclick='logOut()']").click()#click logout btn
        time.sleep(2)
        logout = driver.find_element(By.ID,"nava").text
        self.assertIn('PRODUCT STORE', logout)
        time.sleep(1) 
    
    def test_login_failed (self): #wrong user
        driver = self.browser #buka web browser
        baselogin.negative_login_wrg_user(driver)

        # validasi
        Alert(driver).accept()
        
         
def tearDown(self):
    self.browser.close()

if __name__ == "__main__":
    unittest.main()