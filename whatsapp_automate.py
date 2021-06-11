# from selenium import webdriver
#
# driver = webdriver.Chrome("C:\chromedriver.exe")
# driver.get('https://web.whatsapp.com/')
# name = input('Enter with name of user or group: ')
# msg = input('Enter with your message: ')
# count = int(input('Enter the count: '))
#
# input('Enter anything after scanning QR code')
# user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
# user.click()
#
# msg_box = driver.find_element_by_class_name('input-container')
#
# for i in range(count):
#     msg_box.send_keys(msg)
#     button = driver.find_element_by_class_name('compose-btn-send')
#     button.click()

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

msg = ["Mensagem 1", "Mensagem 2"]

options = Options()
options.add_argument("--user-data-dir=chrome-data")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome('C:\\chromedriver\\chromedriver.exe', options=options)
driver.maximize_window()
driver.get('https://web.whatsapp.com/')  # Already authenticated

time.sleep(6)
driver.find_element_by_xpath("//*[@title='+55 32 9194-7650']").click()

for i in msg:
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(msg)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button/span').click()
    time.sleep(3)

time.sleep(10)
driver.close()
