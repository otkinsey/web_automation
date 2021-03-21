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
        # print("window 1 handle: {handle1}")
        #assert "We're Duo." in self.driver.page_source 

        Username = "MshaKa"
        UserForm = self.driver.find_element_by_xpath("//*[@id='email-thinkmeliusUsername']") 
        UserForm.send_keys(Username)   

        Password = "Lockdown0&"
        Passbox = self.driver.find_element_by_xpath("//*[@id='password']") 
        Passbox.send_keys(Password) 
        
        signin = self.driver.find_element_by_xpath( "//*[@id='root']/div[3]/main/div/form/button/span[1]") 
        signin.click()

        # US30Scanner = self.driver.find_element_by_xpath( "//*[@id='root']/div[3]/main/div[2]/div[1]/div[2]/div/div[2]/a/button/span[1]/h6") 
        # alternate definition of US30Scanner using class name jss640 jss712 jss714 jss717 jss738 jss848
        self.driver.implicitly_wait(2)
        US30Scanner = self.driver.find_elements_by_css_selector('.jss640.jss712.jss714.jss717.jss738.jss848')[1]
        print('[test_automate_browser] buttons: ', US30Scanner)
        US30Scanner.click()

        Agreement = self.driver.find_element_by_xpath( "/html/body/div[2]/div[2]/div/div[3]/label/span[1]/span[1]/input") 
        Agreement.click()

        Ok = self.driver.find_element_by_xpath( "/html/body/div[2]/div[2]/div/div[3]/button/span[1]") 
        Ok.click()

        # return_keys(EntryPrice)

        Archive = self.driver.find_element_by_xpath( "//*[@id='root']/div[3]/main/div[3]/div[3]/div/div/div[2]/div[2]/div/div/div/button[2]/span[1]/span/span") 
        Archive.click()

        self.driver.implicitly_wait(5)

        Symbol = self.driver.find_element_by_xpath("//*[@id='root']/div[3]/main/div[3]/div[3]/div/div/div[2]/div[3]/ul/div/div/div[1]/div[2]/div[1]/h6") 
        print('[TAB-test_search_target] Symbol: ',Symbol.text)


        EntryPrice = self.driver.find_element_by_xpath("//*[@id='root']/div[3]/main/div[3]/div[3]/div/div/div[2]/div[3]/ul/div/div/div[1]/div[2]/div[1]/div/div[1]/p") 
        print('[TAB-test_search_target] Entry Price: ',EntryPrice.text)

        TargetPrice = self.driver.find_element_by_xpath("//*[@id='root']/div[3]/main/div[3]/div[3]/div/div/div[2]/div[3]/ul/div/div/div[1]/div[2]/div[2]/div[1]/p[1]") 
        print('[TAB-test_search_target] Target Price: ',TargetPrice.text)  








    

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