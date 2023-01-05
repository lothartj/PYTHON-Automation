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
PATH = ("C:\msedgedriver.exe")


driver = webdriver.Edge(PATH)

driver.get('https://bc.deepcatchgroup.com/Distr_BC21_UAT/')


time.sleep(3)

def login():
    py.write('lothart@deepcatch.com.na')
    time.sleep(3)
    py.hotkey('tab')
    py.write('Xonu71277')
    py.hotkey('enter')
login()

# time.sleep(10)

# search_button = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/form/div/div[2]/nav/div/div/nav/div[2]/div/div/div/div[2]/div/div/div/div[1]/div/div/div/div/div[2]/div/button')
# search_button.click()

time.sleep(10)

item_one = driver.find_element(By.LINK_TEXT, 'https://bc.deepcatchgroup.com/Distr_BC21_UAT/?company=Seapride%20-%20Food%20Services%20LIVE&node=00002329-0b83-0000-0c0f-4e00836bd2d2&page=31&dc=0&bookmark=31%3bGwAAAAJ7%2fzIANABJAEMARQA4ADMAMQA4ADM%3d')
item_one.click()