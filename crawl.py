from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from time import sleep
from datetime import datetime, timedelta
from selenium.webdriver.common.by import By
import os 
import logging
# Configure logging to write to a file
logging.basicConfig(level=logging.DEBUG,
                    filename='example.log',  # Name of the log file
                    filemode='a',  # Append mode, which allows you to add to the file without overwriting it
                    format='%(asctime)s - %(levelname)s - %(message)s')


# update chrome by search for chrome drive download
# download chrome drive suitable for your chrome browser version (shown in setting -> about chrome)

service = Service(executable_path='./chromedriver.exe')
options = webdriver.ChromeOptions()
browser = webdriver.Chrome(service=service, options=options)

# 2. Mở thử một trang web
website = 'https://violet.vn'

browser.get(website)
end = browser.find_element(By.ID,"username")
end.clear()
end.send_keys("manh2604")
end = browser.find_element(By.ID,"password")
end.clear()
end.send_keys("111111")

button_xpath = "/html/body/div[1]/div/div/div/div[4]/div[1]/div[1]/form/div/div[4]/input"
btn = browser.find_element(By.XPATH,button_xpath)
btn.click()
# browser.close()

sleep(5)
# collect 1000 username 
f = open ("username.txt","a", encoding="utf-8")
count = 0

for i in range (6455144,6455144+10000):
    link = f"https://violet.vn/message/mailbox/type/compose/us_to/{i}"
    try:
        browser.get(link)
        input_element = browser.find_element(By.ID, "ms_address")

        # Get the value attribute of the input element
        value = input_element.get_attribute("value")
        f.write(f'{i}\t{value}\n')
        count += 1
        print (value)
    except Exception as e:
        print (e)
        
    if count % 10 == 0:
        f.close()
        sleep(1)
        f = open ("username.txt","a", encoding="utf-8")
        sleep(1)

    if count % 71 == 0:
        browser.close()
        sleep(2)
        browser = webdriver.Chrome(service=service, options=options)
        browser.get(website)
        end = browser.find_element(By.ID,"username")
        end.clear()
        end.send_keys("manh2604")
        end = browser.find_element(By.ID,"password")
        end.clear()
        end.send_keys("111111")

        button_xpath = "/html/body/div[1]/div/div/div/div[4]/div[1]/div[1]/form/div/div[4]/input"
        btn = browser.find_element(By.XPATH,button_xpath)
        btn.click()
        # browser.close()

        sleep(5)

