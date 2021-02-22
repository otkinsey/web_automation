import os
import io
import unittest
import contextlib
from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time

BASE_URL = "https://orakle.io/login"

class AutomateBrowser(unittest.TestCase):
    def setUp(self):
        self.chrome_options = Options()
        # self.chrome_options.add_argument("--headless")
        self.chrome_options.add_experimental_option("detach",True)
        self.chrome_options.binary_location = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
        self.driver = webdriver.Chrome(executable_path=os.path.abspath("chromedriver"), options=self.chrome_options)

    def test_search_target(self):
        
        self.driver.get(BASE_URL)
        self.driver.implicitly_wait(1)
        handle1 = self.driver.title
        print(f"window 1 handle: {handle1}")
        #assert "We're Duo." in self.driver.page_source 

        Username = "MshaKa"
        UserForm = self.driver.find_element_by_xpath("//*[@id='email-thinkmeliusUsername']") 
        UserForm.send_keys(Username)   

        Password = "Lockdown0&"
        Passbox = self.driver.find_element_by_xpath("//*[@id='password']") 
        Passbox.send_keys(Password)

        



        #Username = MshaKa
        #UserForm = self.driver.find_element_by_xpath(//*[@id="email-thinkmeliusUsername"]) 
        #UserForm.send_keys(Username)
        
        signin = self.driver.find_element_by_xpath( "//*[@id='root']/div[3]/main/div/form/button/span[1]") 
        signin.click()

        # *** keep this in the code for reference
        # ActionChains(self.driver).move_to_element(product).click() *** keep this in the code for reference
        # self.driver.execute_script("document.querySelector(\"[href='/product']\").click()")
        # time.sleep(3) 
        # ******

        #self.driver.get(BASE_URL+'/product')
        #for handle in self.driver.window_handles:
            #self.driver.switch_to.window(handle)
        #handle2 = self.driver.window_handles
        #print(f"test_automate_browser.py - window 2 handle: {self.driver.title}")
        #page_heading = self.driver.find_element_by_css_selector(".header-basic__content.content h1")

        
        # WebDriverWait(self.driver, 10).until(lambda x:x.find_element_by_css_selector(".header-basic__content.content"))

        #assert "Access Security" in page_heading.text
        

    #def tear_down(self):
        # self.driver.close() 

if __name__ == "__main__":
    unittest.main()
    
    # *** keep this in the code for reference
    # import __main__ 
    # suite = unittest.TestLoader().loadTestsFromModule(__main__)
    # with io.StringIO() as buf:
    #     with contextlib.redirect_stdout(buf):
    #         unittest.TextTestRunner(stream=buf).run(suite)
    #     print("*** CAPTURED TEXT ***:\n%s" % buf.getvalue())
    # ******

    # 4098020