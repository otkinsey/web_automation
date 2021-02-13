import os
import io
import unittest
import contextlib
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

class AutomateBrowser(unittest.TestCase):
    def setUp(self):
        self.chrome_options = Options()
        self.chrome_options.add_argument("--headless")
        self.chrome_options.binary_location = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
        self.driver = webdriver.Chrome(executable_path=os.path.abspath("chromedriver"), options=self.chrome_options)

    def test_search_target(self):
        self.driver.get("https://www.duo.com")
        self.driver.implicitly_wait(4)
        assert "We're Duo." in self.driver.page_source
        # self.driver.find_element_by_xpath('//a[@href="/product"]').click()
        product = self.driver.find_element_by_xpath('//a[@href="/product"]')
        ActionChains(self.driver).move_to_element(product).click()
        print(f"test_automate_browser.py - product: {product}")

    def tear_down(self):
        self.driver.close() 

if __name__ == "__main__":
    import __main__ 
    suite = unittest.TestLoader().loadTestsFromModule(__main__)
    with io.StringIO() as buf:
        with contextlib.redirect_stdout(buf):
            unittest.TextTestRunner(stream=buf).run(suite)
        print("*** CAPTURED TEXT ***:\n%s" % buf.getvalue())