from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager as CM
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from random import randint, uniform
from time import time, sleep
import logging
import random, zipfile


DEFAULT_IMPLICIT_WAIT = 1

class Selenium:


    def get(self, url="https://starux.ch", headless=False, proxy=False):
        
        options = Options()
        if headless:
            options.add_argument("--headless=chrome")
        options.add_argument("--start-maximized")
        viewport = random.choice(['2560,1440', '1920,1080', '1536,864'])
        options.add_argument("--window-size="+viewport)
        self.driver = webdriver.Firefox(options=options)
        fail = 0
        while True:
            try:
                self.driver.get(url)
                break
            except:
                fail += 1
                print("Request failed, retrying => "+str(fail))
                if fail == 3:
                    raise Exception("Request failed")
        sleep(random.uniform(0.4, 0.8))
        self.driver.install_addon("cookie_quick_manager-0.5rc2.xpi")

        return self.driver
    

    
    def __get_element__(self, element_tag, locator):
        """Wait for element and then return when it is available"""
        try:
            locator = locator.upper()
            dr = self.driver
            if locator == 'ID' and self.is_element_present(By.ID, element_tag):
                return WebDriverWait(dr, 15).until(lambda d: dr.find_element(By.ID, element_tag))
            elif locator == 'NAME' and self.is_element_present(By.NAME, element_tag):
                return WebDriverWait(dr, 15).until(lambda d: dr.find_element(By.NAME,element_tag))
            elif locator == 'XPATH' and self.is_element_present(By.XPATH, element_tag):
                return WebDriverWait(dr, 15).until(lambda d: dr.find_element(By.XPATH,element_tag))
            elif locator == 'CSS' and self.is_element_present(By.CSS_SELECTOR, element_tag):
                return WebDriverWait(dr, 15).until(lambda d: dr.find_element(By.CSS_SELECTOR ,element_tag))
            else:
                logging.info(f"Error: Incorrect locator = {locator}")
        except Exception as e:
            logging.error(e)
        logging.info(f"Element not found with {locator} : {element_tag}")
        return None

    def is_element_present(self, how, what):
        """Check if an element is present"""
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException:
            return False
        return True

    def __wait_for_element__(self, element_tag, locator, timeout=30):
        """Wait till element present. Max 30 seconds"""
        result = False
        self.driver.implicitly_wait(0)
        locator = locator.upper()
        for i in range(timeout):
            initTime = time()
            try:
                if locator == 'ID' and self.is_element_present(By.ID, element_tag):
                    result = True
                    break
                elif locator == 'NAME' and self.is_element_present(By.NAME, element_tag):
                    result = True
                    break
                elif locator == 'XPATH' and self.is_element_present(By.XPATH, element_tag):
                    result = True
                    break
                elif locator == 'CSS' and self.is_element_present(By.CSS_SELECTOR, element_tag):
                    result = True
                    break
                elif locator == "TAGNAME" and self.is_element_present(By.TAG_NAME, element_tag):
                    result = True
                    break
                else:
                    logging.info(f"Error: Incorrect locator = {locator}")
            except Exception as e:
                logging.error(e)
                print(f"Exception when __wait_for_element__ : {e}")

            sleep(1 - (time() - initTime))
        else:
            print(
                f"Timed out. Element not found with {locator} : {element_tag}")
        self.driver.implicitly_wait(DEFAULT_IMPLICIT_WAIT)
        return result

    def __type_slow__(self, element_tag, locator, input_text=''):
        """Type the given input text"""
        try:
            self.__wait_for_element__(element_tag, locator, 5)
            element = self.__get_element__(element_tag, locator)
            actions = ActionChains(self.driver)
            actions.click(element).perform()
            for s in input_text:
                element.send_keys(s)
                sleep(uniform(0.008, 0.02))

        except Exception as e:
            logging.error(e)
            print(f'Exception when __typeSlow__ : {e}')

    def __random_sleep__(self, minimum=2, maximum=7):
        t = randint(minimum, maximum)
        logging.info(f'Wait {t} seconds')
        sleep(t)

    def __scrollup__(self):
        # self.driver.execute_script(
        # "window.scrollTo(0, document.body.scrollHeight);")
        ActionChains(self.driver).send_keys(Keys.PAGE_UP).perform()

    def __scrolltry__(self, path):
        element = self.driver.find_element("xpath", path)
        desired_y = (element.size['height'] / 2) + element.location['y']
        current_y = (self.driver.execute_script('return window.innerHeight') / 2) + self.driver.execute_script('return window.pageYOffset')
        scroll_y_by = desired_y - current_y
        self.driver.execute_script("window.scrollBy(0, arguments[0]);", scroll_y_by)

    def __scrolldown__(self):
        # self.driver.execute_script(
        # "window.scrollTo(0, document.body.scrollHeight);")
        ActionChains(self.driver).send_keys(Keys.PAGE_DOWN).perform()

    def __scrollback__(self, original_location):
        self.driver.execute_script("window.scroll(0, 0);")
        self.__random_sleep__(3, 5)
        self.driver.execute_script(f"window.scrollTo(0, {original_location});")

