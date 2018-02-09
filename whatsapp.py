# -*- coding: utf8 -*- 
# -*- encoding: utf-8 -*-
"""from __future__ import unicode_literals"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

class Whatsapp():
    """Class for Whatsapp"""
    browser = webdriver.Chrome() # can be place path of webdriver

    def __init__(self, driver='chrome'):
        if driver != 'chrome':
            self.browser = getattr(webdriver, driver)()
        URL = 'http://web.whatsapp.com'
        self.browser.get(URL)

    def getQR():
        try:
            wait = WebDriverWait(self.browser, 15)
            image = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div/div[1]/div[1]/div/img')))
            return image.get_attribute("src")
        except NoSuchElementException as e:
            return False

    def getContacts(self):
        result = []
        # Click on New Message
        btn_new_message = self.browser.find_element_by_xpath('//*[@id="side"]/header/div[2]/div/span/div[2]')
        btn_new_message.click()
        # Run script to scroll down
        scroll_script = open('scroll.js', 'r').read()
        self.browser.execute_script(scroll_script)
        # Wait 20 seconds
        sleep(20)
        # Extract names of contacts
        selector = '#app > div > div > div.drawer-manager > span.pane.pane-one > div > span > div > div.drawer-body > div:nth-child(2) > div > div > div > div > div > div.chat-body > div.chat-main > div > span'
        contacts = self.browser.find_elements_by_css_selector(selector)
        for contact in contacts:
            result.append(contact.text)
        # Press Go back
        self.browser.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/span[1]/div/span/div/header/div/div/button/span').click()
        return result

    def getActiveChat(self, contact_name):
        chat = self.browser.find_element_by_xpath('//span[contains(text(),"{contact_name}")]'.format(contact_name=contact_name))
        return chat.click()

    def getChatBySearch(self, term):
        sleep(1)
        searchbox = self.browser.find_element_by_xpath('//*[@id="side"]/div[2]/div/label/input')
        searchbox.click()
        searchbox.send_keys(term)
        sleep(1)
        # Click on avatar image of search
        chat = self.browser.find_element_by_xpath(u'//span[contains(text(), "{term}")]'.format(term=term))
        chat.click()



    def setTextMessage(self, text):
        messagebox = self.browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
        return messagebox.send_keys(text)
        

    def send(self):
        return self.browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/button').click()

    def exit(self):
        return self.browser.quit()
