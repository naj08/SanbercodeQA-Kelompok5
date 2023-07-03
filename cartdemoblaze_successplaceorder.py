import unittest
import time
from selenium import webdriver
#from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
#from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome()
#DEFAULT_EXECUTABLE_PATH = "chromedriver"

# test scenario

class SuccessPlaceOrder(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        #webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.url = "https://www.demoblaze.com/"
    # positive case

    def test_a_success_placeorder(self):
    # steps
        driver = self.browser #buka web browser
        driver.get(self.url) # buka situs
        #time.sleep(0.5)
        driver.find_element(By.XPATH, "//a[@id='login2']").click()
        time.sleep(0.5)
        driver.find_element(By.ID,"loginusername").send_keys("johnndoee") # fill username
        #time.sleep(1)
        driver.find_element(By.ID,"loginpassword").send_keys("johnndoee") # fill password
        #time.sleep(0.5)
        driver.find_element(By.XPATH, "//div[@id='logInModal']/div[@role='document']//div[@class='modal-footer']/button[2]").click()
        time.sleep(2)
        #driver.find_element(By.XPATH, "/html//a[@id='cartur']").click()
        driver.find_element(By.ID,"cartur").click() # go to cart
        time.sleep(1)
        driver.find_element(By.XPATH, "/html//div[@id='page-wrapper']//button[@type='button']").click()
        time.sleep(0.5)
        driver.find_element(By.ID,"name").send_keys("johnndoee") # fill name
        driver.find_element(By.ID,"country").send_keys("nevada") # fill country
        driver.find_element(By.ID,"city").send_keys("last vegas") # fill city
        driver.find_element(By.ID,"card").send_keys("01010101010101") # fill card
        driver.find_element(By.ID,"month").send_keys("07") # fill month
        driver.find_element(By.ID,"year").send_keys("2023") # fill year
        #driver.find_element(By.CSS_SELECTOR, "[onclick='purchaseOrder()']").click()
        driver.find_element(By.XPATH, "//div[@id='orderModal']/div[@role='document']//div[@class='modal-footer']/button[2]").click()
        #validasi
        placeorder = driver.find_element(By.XPATH, "//body/div[10]/h2[.='Thank you for your purchase!']").text
        self.assertIn('Thank you for your purchase!', placeorder)

        def tearDown(self):
            self.browser.close()


    def test_b_success_repeatclickpurchase(self):
    # steps
        driver = self.browser #buka web browser
        driver.get(self.url) # buka situs
        #time.sleep(0.5)
        driver.find_element(By.XPATH, "//a[@id='login2']").click()
        time.sleep(0.5)
        driver.find_element(By.ID,"loginusername").send_keys("johnndoee") # fill username
        #time.sleep(1)
        driver.find_element(By.ID,"loginpassword").send_keys("johnndoee") # fill password
        #time.sleep(0.5)
        driver.find_element(By.XPATH, "//div[@id='logInModal']/div[@role='document']//div[@class='modal-footer']/button[2]").click()
        time.sleep(1)
        #driver.find_element(By.XPATH, "/html//a[@id='cartur']").click()
        driver.find_element(By.ID,"cartur").click() # go to cart
        time.sleep(1)
        driver.find_element(By.XPATH, "/html//div[@id='page-wrapper']//button[@type='button']").click()
        time.sleep(0.5)
        driver.find_element(By.ID,"name").send_keys("johnndoee") # fill name
        driver.find_element(By.ID,"country").send_keys("nevada") # fill country
        driver.find_element(By.ID,"city").send_keys("last vegas") # fill city
        driver.find_element(By.ID,"card").send_keys("01010101010101") # fill card
        driver.find_element(By.ID,"month").send_keys("07") # fill month
        driver.find_element(By.ID,"year").send_keys("2023") # fill year
        #driver.find_element(By.XPATH, "//div[@id='orderModal']/div[@role='document']//div[@class='modal-footer']/button[2]").click()
        #time.sleep(0.5)
        #validasi
        response_data = driver.find_element(By.XPATH, "//div[@id='orderModal']/div[@role='document']//div[@class='modal-footer']/button[2]").is_enabled()
        self.assertEqual(False, response_data)

        def tearDown(self):
            self.browser.close()

    def test_c_success_clickokplaceorder(self):
    # steps
        driver = self.browser #buka web browser
        driver.get(self.url) # buka situs
        driver.find_element(By.XPATH, "//a[@id='login2']").click()
        time.sleep(0.5)
        driver.find_element(By.ID,"loginusername").send_keys("johnndoee") # fill username
        #time.sleep(1)
        driver.find_element(By.ID,"loginpassword").send_keys("johnndoee") # fill password
        #time.sleep(0.5)
        driver.find_element(By.XPATH, "//div[@id='logInModal']/div[@role='document']//div[@class='modal-footer']/button[2]").click()
        time.sleep(2)
        driver.find_element(By.ID,"cartur").click() # go to cart
        time.sleep(1)
        driver.find_element(By.XPATH, "/html//div[@id='page-wrapper']//button[@type='button']").click()
        time.sleep(0.5)
        driver.find_element(By.ID,"name").send_keys("johnndoee") # fill name
        driver.find_element(By.ID,"country").send_keys("nevada") # fill country
        driver.find_element(By.ID,"city").send_keys("last vegas") # fill city
        driver.find_element(By.ID,"card").send_keys("01010101010101") # fill card
        driver.find_element(By.ID,"month").send_keys("07") # fill month
        driver.find_element(By.ID,"year").send_keys("2023") # fill year
        driver.find_element(By.XPATH, "//div[@id='orderModal']/div[@role='document']//div[@class='modal-footer']/button[2]").click()
        time.sleep(0.5)
        driver.find_element(By.XPATH, "//body/div[10]//button[.='OK']").click()
        #validasi
        self.assertEqual(driver.page_source.__contains__("Place Order"), True)

        def tearDown(self):
            self.browser.close()

if __name__ == "__main__":
        unittest.main()

