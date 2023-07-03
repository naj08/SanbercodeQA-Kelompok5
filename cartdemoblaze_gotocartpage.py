import unittest
import time
from selenium import webdriver
#from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
#from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome()
#DEFAULT_EXECUTABLE_PATH = "chromedriver"

# test scenario

class GoToCartPage(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        #webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.url = "https://www.demoblaze.com/"
    # positive case

    def test_a_success_gotocartpage_withoutlogin(self):
        # steps
            driver = self.browser #buka web browser
            driver.get(self.url) # buka situs
            #time.sleep(0.5)
            time.sleep(1)
            #driver.find_element(By.XPATH, "/html//a[@id='cartur']").click()
            driver.find_element(By.ID,"cartur").click() # go to cart
            #validasi
            url = driver.current_url
            self.assertIn('/cart.html', url)
            btncart = driver.find_element(By.CLASS_NAME, "btn.btn-success").text
            self.assertEqual('Place Order', btncart)



    def test_b_success_gotocartpage(self):
    # steps
        driver = self.browser #buka web browser
        driver.get(self.url) # buka situs
        time.sleep(0.5)
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
        #validasi
        url = driver.current_url
        self.assertIn('/cart.html', url)
        btncart = driver.find_element(By.CLASS_NAME, "btn.btn-success").text
        self.assertEqual('Place Order', btncart)

        def tearDown(self):
            self.browser.close()


if __name__ == "__main__":
        unittest.main()

