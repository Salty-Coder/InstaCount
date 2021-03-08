"""
Program made by Salty-Coder.
Protected by GNU General Public License v3.0
"""

from selenium import webdriver
from random import randint
import random
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import accountInfoGenerator as account



browser = webdriver.Chrome("chromedriver.exe")
browser.get("http://www.instagram.com/accounts/emailsignup/")

browser.execute_script('''window.open("","_blank");''')
browser.switch_to.window(browser.window_handles[1])
browser.get("https://www.fakemail.net/")
browser.switch_to.window(browser.window_handles[0])

time.sleep(4)

try:
    WebDriverWait(browser, 4).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/iframe")))
    print("> Found Captcha, attempting to bypass...")
    browser.close()
    browser.switch_to.window(browser.window_handles[0])
    import byPassCaptcha as bpcaptcha
    bpcaptcha()

except TimeoutException:
    print("> No Captcha found!")

email = browser.find_element_by_xpath("//*[@id=\"email\"]").text

time.sleep(3) #time.sleep count can be changed depending on the Internet speed.
name = account.username()

#Fill the email value
print("> The email is " + email)
browser.switch_to.window(browser.window_handles[0])
email_field = browser.find_element_by_name('emailOrPhone')
email_field.send_keys(email)

#Fill the fullname value
fullname_field = browser.find_element_by_name('fullName')
fullname_field.send_keys(account.generatingName())
print(account.generatingName())
#Fill username value
username_field = browser.find_element_by_name('username')
username_field.send_keys(name)
print(name)
#Fill password value
password_field  = browser.find_element_by_name('password')
password_field.send_keys('aa12345bb12345cc'+name) #You can determine another password here.


WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"react-root\"]/section/main/div/article/div/div[1]/div/form/div[7]/div/button"))).click()


time.sleep(3)

month_field = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/div[4]/div/div/span/span[1]/select/option[' + str(random.randint(1,9)) + ']')
month_field.click()

day_field = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/div[4]/div/div/span/span[2]/select/option[' + str(random.randint(1,17)) + ']')
day_field.click()

year_field = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/div[4]/div/div/span/span[3]/select/option[' + str(random.randint(21,102)) + ']')
year_field.click()

WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Next']"))).click()



time.sleep(8)

print('Registering....')

browser.switch_to.window(browser.window_handles[1])

time.sleep(8)

browser.execute_script('''window.open("","_blank");''')
browser.switch_to.window(browser.window_handles[2])
browser.get("https://www.fakemail.net/window/id/2") 
time.sleep(7)  
WebDriverWait(browser, 10).until(EC.visibility_of_element_located(By.XPATH("//*[@id=\"email_content\"]/table/tbody/tr[4]/td/table/tbody/tr/td/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td[2]")))  
verify = browser.find_element("xpath", "//*[@id=\"email_content\"]/table/tbody/tr[4]/td/table/tbody/tr/td/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td[2]").text
browser.close()
browser.switch_to.window(browser.window_handles[1])
browser.close()
browser.switch_to.window(browser.window_handles[0])
browser.find_element_by_xpath("//*[@id=\"react-root\"]/section/main/div/article/div/div[1]/div[2]/form/div/div[1]/input").send_keys(verify)
browser.find_element_by_xpath("//*[@id=\"react-root\"]/section/main/div/article/div/div[1]/div[2]/form/div/div[2]/button").click()

# UNFINISHED - CANNOT FIND CODE IN EMAIL
