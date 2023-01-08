#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/1/9 6:11
# @Author  : tolatolatop
# @File    : main.py.py
import sys
import time
from argparse import ArgumentParser

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from PIL import Image


def init_chrome_driver(config):
    options = webdriver.ChromeOptions()
    options.add_argument('lang=zh_CN.UTF-8')

    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,  # 关闭保存密码
    }

    options.add_experimental_option("prefs", prefs)
    options.add_argument('--no-sandbox')  # 解决DevToolsActivePort文件不存在的报错
    options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
    options.add_argument('--start-maximized')  # 最大化运行（全屏窗口）,不设置，取元素会报错
    # 关闭ssl提示
    options.add_argument('ignore-certificate-errors')
    # 禁用浏览器正在被自动化程序控制的提示
    # options.add_experimental_option("useAutomationExtension", False)
    # options.add_experimental_option("excludeSwitches", ["enable-automation"])

    executable_path = r"venv/chromedriver.exe"
    driver = webdriver.Chrome(executable_path=executable_path, chrome_options=options)
    return driver


def init_arg_parser():
    ap = ArgumentParser()
    return ap


def run(driver):
    driver.get("http://www.python.org")
    assert "Python" in driver.title
    driver.save_screenshot("test.png")
    driver.execute_script("alert('ok')")
    time.sleep(3)


def main():
    ap = init_arg_parser()
    namespace = ap.parse_args(sys.argv[1:])

    driver = init_chrome_driver(namespace)
    run(driver)
    driver.close()


if __name__ == "__main__":
    main()
