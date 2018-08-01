#! /usr/bin/python3.5

from selenium import webdriver

browser = webdriver.Firefox()
browser.get('https://inventwithpython.com')

try:
    elem = browser.find_element_by_class_name('navbar')
    print('Found <%s> element with that class name!' %elem.tag_name)
except:
    print('Was not able to find an element with that class name.')
