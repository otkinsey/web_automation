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
import subprocess
import pdb
from DWX_ZeroMQ_Connector_v2_0_1_RC8 import DWX_ZeroMQ_Connector

BASE_URL = "https://orakle.io/login"

class AutomateBrowser(unittest.TestCase):
    def setUp(self):
        self.chrome_options = Options()
        # self.chrome_options.add_argument("--headless")
        self.chrome_options.add_experimental_option("detach",True) 
        self.chrome_options.binary_location = "C:\Users\otkin\dwx_connector\dwx-zeromq-connector\v2.0.1\python\api"
        self.driver = webdriver.Chrome(executable_path=os.path.abspath("chromedriver"), options=self.chrome_options)

    def test_search_target(self):
        
        self.driver.get(BASE_URL)
        self.driver.implicitly_wait(1) 
        self.driver.maximize_window()
        handle1 = self.driver.title
        # print("window 1 handle: {handle1}")
        #assert "We're Duo." in self.driver.page_source 

        Username = "MshaKa"
        UserForm = self.driver.find_element_by_xpath("//*[@id='email-thinkmeliusUsername']") 
        UserForm.send_keys(Username)   

        Password = "Kappaphi@1"
        Passbox = self.driver.find_element_by_xpath("//*[@id='password']") 
        Passbox.send_keys(Password) 
        
        signin = self.driver.find_element_by_xpath( "//*[@id='root']/div[3]/main/div/form/button/span[1]") 
        signin.click()

        # US30Scanner = self.driver.find_element_by_xpath( "//*[@id='root']/div[3]/main/div[2]/div[1]/div[2]/div/div[2]/a/button/span[1]/h6") 
        # alternate definition of US30Scanner using class name jss640 jss712 jss714 jss717 jss738 jss848
        self.driver.implicitly_wait(2)
        US30Scanner = self.driver.find_element_by_css_selector('#root > div.jss778 > main > div > div:nth-child(2) > div:nth-child(2) > div > div.jss637.jss771 > a > button')
        # print('[test_automate_browser] buttons: ', US30Scanner)
        US30Scanner.click()

        # Agreement = self.driver.find_element_by_xpath( "/html/body/div[2]/div[2]/div/div[3]/label/span[1]/span[1]/input") 
        self.driver.implicitly_wait(3)
        Agreement = self.driver.find_element_by_css_selector(".jss1024.jss1007 input[value='agreement']") 
        Agreement.click()

        Ok = self.driver.find_element_by_xpath( "/html/body/div[2]/div[2]/div/div[3]/button/span[1]") 
        Ok.click()
        self.driver.implicitly_wait(5)

        # return_keys(EntryPrice)

        # Arrow = self.driver.find_element_by_xpath( "//*[@id='root']/div[3]/main/div[4]/div[2]/svg").click()
        Arrow = self.driver.find_element_by_css_selector(".jss783.jss1017").click()

        Archive = self.driver.find_element_by_css_selector(".jss894.jss895 button:nth-child(2)") 
        Archive.click()
        self.driver.implicitly_wait(17)

        # Symbol = self.driver.find_element_by_xpath("//*[@id='root']/div[3]/main/div[2]/div[3]/div/div/div[2]/div[3]/ul/div/div[3]/div[2]/div[1]/div/div[1]") 
        Symbol = self.driver.find_element_by_css_selector(".jss566.jss584") 
        print('[TAB-test_search_target] Symbol: ',Symbol.text)
<<<<<<< Updated upstream
<<<<<<< Updated upstream

        EntryPrice = self.driver.find_element_by_css_selector(".jss606.jss810.jss813.jss818.jss819 p.jss566.jss574") 
        print('[TAB-test_search_target] Entry Price: ',EntryPrice.text); pdb.set_trace()
=======
        
>>>>>>> Stashed changes
=======
        
>>>>>>> Stashed changes

        TargetPrice = self.driver.find_element_by_css_selector(".jss566.jss574.jss599")
        print('[TAB-test_search_target] Target Price: ',TargetPrice.text)  

        # you need to find action (BUY or SELL)

        # subprocess.run(['open','/Applications/XM MT4.app'])


    # def init(self):

        # print('logging into Stack overflow')
        # self.driver=webdriver.Chrome('C:/Users/muathkinsey/AppData/Local/chromedriver_win32/chromedriver.exe')
        # self.driver.get('https://www.tradingview.com')
         
        # self.driver.implicitly_wait(5)

        # signin = self.driver.find_element_by_xpath( "/html/body/div[2]/div[3]/div/div[4]/span[2]") 
        # signin.click()

        # email = self.driver.find_element_by_xpath( "//*[@id='overlap-manager-root']/div/div[2]/div/div/div/div/div/div/div[1]/div[4]/div/span/span") 
        # email.click()

        # Username = "muathkinsey"
        # UserForm = self.driver.find_element_by_name('username')
        # UserForm.send_keys(Username)   

        # Password = "muath12345678"
        # Passbox = self.driver.find_element_by_name("password")
        # Passbox.send_keys(Password) 

        # submit = self.driver.find_element_by_class_name( "tv-button__loader") 
        # submit.click()
        # self.driver.implicitly_wait(10)


        # searchtarget = "US30"
        # search = self.driver.find_element_by_xpath('/html/body/div[3]/div[3]/div/div[3]/form/label/tv-autocomplete/input')
        # search.send_keys(searchtarget)   
        # # search.send_keys(keys.RETURN)   
        # self.driver.implicitly_wait(3)

        # self.driver.get('https://www.tradingview.com/chart/7kHCdkJL/')
        # self.driver.implicitly_wait(3)

        # fullchart = self.driver.find_element_by_xpath( "//*[@id='js-category-content']/div/div/div/div/div[1]/div/div[1]/div/a/span[2]") 
        # fullchart.click()
        # self.driver.implicitly_wait(5)



        

        
        

        # connect = self.driver.find_element_by_class_name( "button-1iktpaT1 size-l-2NEs9_xt intent-primary-1-IOYcbg appearance-default-dMjF_2Hu full-width-1wU8ljjC broker-login-submit-button button-1fGT2JpL") 
        # connect.click()
        

        _zmq = DWX_ZeroMQ_Connector
        # self.driver.find_element_by_xpath('//*[@id="openid-buttons"]/button[1]').click() 
        # self.driver.find_element_by_xpath('//input[@type="email"]').send_keys(username)
        # self.driver.find_element_by_xpath('//*[@id="identifierNext"]').click()
        # sleep(3)
        # self.driver.find_element_by_xpath('//input[@type="password"]').send_keys(password)
        # self.driver.find_element_by_xpath('//*[@id="passwordNext"]').click()
        # sleep(2)
        # self.driver.get("https://www.tradingview.com/")
        # self.driver.implicitly_wait(1)

        # passw=open('New Text Document (2).txt',"r",encoding="utf-8")   
        # password=str(passw.read()) 
        # user=open('New Text Document (3).txt',"r",encoding="utf-8")   
        # username=str(user.read())
        # mylike= Google(username,password)

        # login = self.driver.find_element_by_xpath( "/html/body/div[2]/div[3]/div/div[4]/span[2]/a") 
        # login.click()

        # Google = self.driver.find_element_by_xpath( "//*[@id='overlap-manager-root']/div/div[2]/div/div/div/div/div/div/div[1]/div[1]/span[1]") 
        # Google.click()

        # Username = "muath.kinsey@gmail.com"
        # UserForm = self.driver.find_elements_by_css_selector('#identifierId')
        # UserForm.send_keys(Username)
    





    

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