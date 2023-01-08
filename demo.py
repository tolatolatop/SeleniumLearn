#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/1/9 6:08
# @Author  : tolatolatop
# @File    : demo.py.py
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

executable_path = r"venv/chromedriver.exe"
driver = webdriver.Chrome(executable_path=executable_path)
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()
