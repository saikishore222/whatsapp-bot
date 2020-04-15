from selenium import webdriver
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
import csv
driver = webdriver.Chrome()
file_name="data.csv"
csvFile=open(file_name,'rt')
csvReader=csv.reader(csvFile,delimiter =",")
list_=list()
for row in csvReader:
    list_.append((row[0],row[1]))
print(list_)
counter=0
driver.get('https://web.whatsapp.com/')
print("scan the qr code")
sleep(8)
def send_attach(counter):
        filepath='C:\\Users\Yushmi\Desktop\whatsapp bot\car.jpg'
        input("Enter anything")
        user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(list_[counter][0]))
        user.click()
        attachment_box = driver.find_element_by_xpath('//div[@title = "Attach"]')
        attachment_box.click()
        image_box = driver.find_element_by_xpath(
        '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
        image_box.send_keys(filepath)
        sleep(10)
        send_button = driver.find_element_by_xpath('//span[@data-icon="send-light"]')
        send_button.click()
        sleep(10)
def send_msg(counter):
        print("message sending in the process")
        message='hi {},this is send from whatsapp bot.please note'.format(list_[counter][0])
        url='https:api.whatsapp.com/send?phone={}'.format("91"+list_[counter][1])
        driver.get(url)
        while True:
            try:
                driver.find_element_by_xpath('//*[@id="action-button"]').click()
                url2='https://web.whatsapp.com/send?phone={}'.format("91"+list_[counter][1])
                driver.get(url2)
                break
            except:
                pass
        while True:
            try:
                element=driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
                element.click()
                element.send_keys(message)
                element.send_keys(Keys.ENTER)
                break
            except:
                pass
for i in range(0,len(list_)):
        send_attach(counter)
        send_msg(counter)
        print("message sent succesfully to",list_[counter][1])
        counter+=1
print(counter," messages was sent by whatsapp bot")
