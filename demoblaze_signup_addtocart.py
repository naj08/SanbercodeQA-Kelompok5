from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from time import sleep
import unittest


username = "mawmaw"
password = "123"

class DemoBlazeTest(unittest.TestCase):
    def setUp(self):
        #create a headless Chrome browser
        op = webdriver.ChromeOptions()
        op.add_argument('headless')
        self.driver = webdriver.Chrome()
        self.url="https://www.demoblaze.com/"  


    def test_case1(self): #Create Sign up Succes

        driver = self.driver #buka web browser
        driver.get(self.url) # buka situs
        driver.maximize_window()
        sleep(1)
        # get the signup modele
        signup=driver.find_element(By.ID,"signin2")
        WebDriverWait(driver,5).until(EC.element_to_be_clickable(signup))
        signup.click()
        username=driver.find_element(By.ID,"sign-username")
        WebDriverWait(driver,5).until(EC.visibility_of(username))
        username.send_keys("mawmaw")
        password=driver.find_element(By.ID,"sign-password")
        WebDriverWait(driver,5).until(EC.visibility_of(password))
        password.send_keys("123")
        driver.find_element(By.ID, "signInModal").click()
        sleep(5)

    def test_case2(self): #Sign up Invalid Username

        driver = self.driver #buka web browser
        driver.get(self.url) # buka situs
        driver.maximize_window()
        sleep(1)
        signup=driver.find_element(By.ID,"signin2")
        WebDriverWait(driver,5).until(EC.element_to_be_clickable(signup))
        signup.click()
        user=driver.find_element(By.ID,"sign-username")
        WebDriverWait(driver,5).until(EC.visibility_of(user))
        user.send_keys("mawmaw2")
        pwd=driver.find_element(By.ID,"sign-password")
        WebDriverWait(driver,5).until(EC.visibility_of(pwd))
        pwd.send_keys("123")
        driver.find_element(By.ID, "signInModal").click()
        sleep(5) 
    
    def test_case3(self): #Sign up Invalid Password

        driver = self.driver #buka web browser
        driver.get(self.url) # buka situs
        driver.maximize_window()
        sleep(1)
        signup=driver.find_element(By.ID,"signin2")
        WebDriverWait(driver,5).until(EC.element_to_be_clickable(signup))
        signup.click()
        usr=driver.find_element(By.ID,"sign-username")
        WebDriverWait(driver,5).until(EC.visibility_of(usr))
        usr.send_keys("mawmaw2")
        pswd=driver.find_element(By.ID,"sign-password")
        WebDriverWait(driver,5).until(EC.visibility_of(pswd))
        pswd.send_keys("abc")
        driver.find_element(By.ID, "signInModal").click()
        sleep(5) 

    def test_case4(self): # Log in and password success.

        driver = self.driver #buka web browser
        driver.get(self.url) # buka situs
        driver.maximize_window()
        sleep(1)
        # get the login modele
        login=driver.find_element(By.ID,"login2")
        WebDriverWait(driver,5).until(EC.element_to_be_clickable(login))
        login.click()
        usrnm=driver.find_element(By.ID,"loginusername")
        WebDriverWait(driver,5).until(EC.visibility_of(usrnm))
        usrnm.send_keys("mawmaw")
        pwwd=driver.find_element(By.ID,"loginpassword")
        WebDriverWait(driver,5).until(EC.visibility_of(pwwd))
        pwwd.send_keys("123")
        driver.find_element("xpath", "//button[contains(text(),'Log in')]").click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Log out")))#untuk bantuan,tidak ada fungsi click
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Cart"))).click()

    def test_cart_without_login(self):
        driver=self.driver
        driver.get(self.url)
        driver.maximize_window()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Cart"))).click()

    def test_add_to_cart_with_login(self):
        driver = self.driver #buka web browser
        driver.get(self.url) # buka situs
        driver.maximize_window()
        login=driver.find_element(By.ID,"login2")
        WebDriverWait(driver,5).until(EC.element_to_be_clickable(login))
        login.click()
        usnm=driver.find_element(By.ID,"loginusername")
        WebDriverWait(driver,5).until(EC.visibility_of(usnm))
        usnm.send_keys("mawmaw")
        pwd2=driver.find_element(By.ID,"loginpassword")
        WebDriverWait(driver,5).until(EC.visibility_of(pwd2))
        pwd2.send_keys("123")
        driver.find_element("xpath", "//button[contains(text(),'Log in')]").click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Log out")))#untuk bantuan,tidak ada fungsi click
        # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Phones"))).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Samsung galaxy s6"))).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Add to cart"))).click()
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        successMessage=alert.text
        print(alert.text)
        alert.accept()
        self.assertEqual("Product added.", successMessage)
    def test_add_more_than_one_with_login(self):
        driver = self.driver #buka web browser
        driver.get(self.url) # buka situs
        driver.maximize_window()
        login=driver.find_element(By.ID,"login2")
        WebDriverWait(driver,5).until(EC.element_to_be_clickable(login))
        login.click()
        username1=driver.find_element(By.ID,"loginusername")
        WebDriverWait(driver,5).until(EC.visibility_of(username1))
        username1.send_keys("mawmaw")
        password1=driver.find_element(By.ID,"loginpassword")
        WebDriverWait(driver,5).until(EC.visibility_of(password1))
        password1.send_keys("123")
        driver.find_element("xpath", "//button[contains(text(),'Log in')]").click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Log out")))#untuk bantuan,tidak ada fungsi click
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Samsung galaxy s6"))).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Add to cart"))).click()
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        successMessage=alert.text
        print(alert.text)
        alert.accept()
        self.assertEqual("Product added.", successMessage)
        driver.find_element(By.XPATH, "//a[contains(text(),'Home')]").click()
        WebDriverWait(driver,10).until(EC.presence_of_element_located((By.LINK_TEXT,"Nokia lumia 1520"))).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Add to cart"))).click()
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert2 = driver.switch_to.alert
        message = alert2.text
        print(alert2.text)
        alert.accept()
        self.assertEqual("Product added.", message)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Cart"))).click()
    
    def test_delete_one_with_login(self):
        driver = self.driver #buka web browser
        driver.get(self.url) # buka situs
        driver.maximize_window()
        login=driver.find_element(By.ID,"login2")
        WebDriverWait(driver,5).until(EC.element_to_be_clickable(login))
        login.click()
        username2=driver.find_element(By.ID,"loginusername")
        WebDriverWait(driver,5).until(EC.visibility_of(username2))
        username2.send_keys("mawmaw")
        password2=driver.find_element(By.ID,"loginpassword")
        WebDriverWait(driver,5).until(EC.visibility_of(password2))
        password2.send_keys("123")
        driver.find_element("xpath", "//button[contains(text(),'Log in')]").click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Log out")))#untuk bantuan,tidak ada fungsi click
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Samsung galaxy s6"))).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Add to cart"))).click()
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        successMessage=alert.text
        print(alert.text)
        alert.accept()
        self.assertEqual("Product added.", successMessage)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Cart"))).click()
        sleep(2)
        driver.find_element(By.LINK_TEXT,"Delete").click()
        
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()