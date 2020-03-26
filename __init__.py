from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import card_details

#driver = webdriver.Chrome()
#session_id = driver.session_id;
#session_url = driver.command_executor._url

#driver.session_id='b1387d8bb5c60c2164ef07dac0000e8d'

#print(session_id,session_url)


#Pass the session_url you extracted

driver = webdriver.Remote(command_executor="http://127.0.0.1:62468",desired_capabilities={})

#Attach to the session id you extracted

driver.session_id = "82889b2d10caf26a00b1664bf799c268"

#Resume from that browser state



driver.get("https://paytm.com/credit-card-bill-payment")
time.sleep(20)

driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div[1]/div[1]/div/div[2]/div[1]/ul/li/div/input').send_keys("")
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div[1]/div[1]/div/div[2]/div[1]/ul/li[2]/div[1]/div/input').send_keys("1999")


driver.find_element_by_xpath('//*[@id="app"]/div/div[4]/div[1]/div[1]/div/div[2]/div[4]/button').click()
time.sleep(5)

driver.find_element_by_xpath('//*[@id="leftTab"]/ul/li[3]/a').click()


driver.find_element_by_xpath('//*[@id="cn1"]').send_keys(card_details.card_num)
driver.find_element_by_xpath('//*[@id="dcCvvBox"]').send_keys(card_details.cvv)
driver.find_element_by_xpath("//select[@id='dcExpMonth']/option[text()=card_details.expiry_month]").click()
driver.find_element_by_xpath("//select[@id='dcExpYear']/option[text()='2022']").click()

time.sleep(8)
driver.close()

