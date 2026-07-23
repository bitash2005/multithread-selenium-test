from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

class action:
    def __init__(self,driver:webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver,15)
        
    def login(self):
        l_g = self.wait.until(EC.element_to_be_clickable((By.XPATH ,"//a[@href='/login']")))
        l_g.click()
        enter_mail = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@type='email']")))
        enter_mail.clear()
        enter_mail.click()
        enter_mail.send_keys("bita1223@gmail.com")
        enter_pass = self.wait.until(EC.element_to_be_clickable((By.XPATH ,"//input[@type='password']" )))
        enter_pass.clear()
        enter_pass.click()
        enter_pass.send_keys("9999")
        login_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH ,"//button[@data-qa='login-button']")))
        login_btn.click()
        time.sleep(3)
        
    def delete (self):
        self.login()
        delet_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH ,"//a[@href='/delete_account']" )))
        delet_btn.click()
        
    def verify_login_failed(self):
        error_element = self.wait.until(EC.element_to_be_clickable((By.XPATH , "//p[contains(text(),'Your email or password is incorrect!')]")))
        erorr_txt = error_element.text()
        assert "Your email or password is incorrect!" in erorr_txt , "erorr : why user can login ? "  
               
        
    