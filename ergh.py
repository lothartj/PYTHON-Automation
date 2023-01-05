import tkinter as tk
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re,datetime,os,sys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from telnetlib import EC
import pyautogui as py
PATH = ("C:\chromedriver.exe")



driver = webdriver.Chrome(PATH)

# sales order
# def open_new():
#     driver.get('https://www.youtube.com/shorts/nSMNrOBAIO0')
#     py.hotkey('ctrl', 't')
#     driver.get('https://b2b.deepcatchgroup.com:3055/stocktake/admin/section')
    
# open_new()

def open_url():
    driver.get('https://b2b.deepcatchgroup.com:3055/stocktake/admin/section')
    



# while 1==1:
#     click_button = driver.find_element(By.XPATH, '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-button-renderer/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]')
#     click_button.click()
#     py.hotkey('ctrl, t')
#     time.sleep(15)


