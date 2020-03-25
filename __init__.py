from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import card_details

driver = webdriver.Chrome()
session_id = driver.session_id
print(session_id)
driver.get("https://paytm.com/credit-card-bill-payment")
time.sleep(20)
elem = driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div[1]/div[1]/div/div[2]/div[1]/ul/li/div/input')
elem.send_keys("5523650001337111")
amount=driver.find_element_by_xpath('//*[@id="app"]/div/div[4]/div[1]/div[1]/div/div[2]/div[1]/ul/li[2]/div[1]/div/input')
amount.send_keys("100")
proceed=driver.find_element_by_xpath('//*[@id="app"]/div/div[4]/div[1]/div[1]/div/div[2]/div[4]/button')
amount.send_keys("100")
proceed.click()

sel_deb_card=driver.find_element_by_xpath('//*[@id="leftTab"]/ul/li[3]/a')
sel_deb_card.click()

driver.find_element_by_xpath('//*[@id="cn1"]').send_keys(card_details.card_num)
driver.find_element_by_xpath('//*[@id="dcCvvBox"]').send_keys(card_details.cvv)
driver.find_element_by_xpath("//select[@id='dcExpMonth']/option[text()=card_details.expiry_month]").click()
driver.find_element_by_xpath("//select[@id='dcExpYear']/option[text()='2022']").click()

time.sleep(8)
driver.close()

