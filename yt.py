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

driver.get('https://www.youtube.com/')


def sleep():
    time.sleep(3)
sleep()

def sleep_short():
    time.sleep(5)
sleep_short()

def search_b():
    search_button = driver.find_element(By.XPATH, '/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input')
    search_button.click()
    search_button.send_keys('funny shorts')
    sleep()
    py.hotkey('enter')
search_b()

sleep()


def first_video():
    click_button = driver.find_element(By.XPATH, '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div[2]/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/ytd-thumbnail/a')
    click_button.click()
first_video()   

sleep()

# while 1 == 1 :
#     def click_down():
#         clickDown = driver.find_element(By.XPATH, '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-button-renderer/yt-button-shape/button')
#         clickDown.click()
#         sleep_short()
#     click_down()

def share_button():
    shareb = driver.find_element(By.XPATH, '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[2]/div[2]/ytd-reel-video-renderer[1]/div[2]/ytd-reel-player-overlay-renderer/div[2]/div[5]/ytd-button-renderer/yt-button-shape/label/button')
    shareb.click()
share_button()

sleep()

def copy_button():
    copyB = driver.find_element(By.XPATH, '/html/body/ytd-app/ytd-popup-container/tp-yt-paper-dialog/ytd-unified-share-panel-renderer/div[2]/yt-third-party-network-section-renderer/div[2]/yt-copy-link-renderer/div/yt-button-renderer/yt-button-shape/button')
    copyB.click()
copy_button()

sleep()

def opennew_tab():
    py.hotkey('ctrl', 't')
    sleep()
    py.typewrite("https://ssyoutube.com/en31/youtube-video-downloader")
    sleep()
    py.hotkey('enter')
opennew_tab()

# def search_link_button():
#     search5 = driver.find_element(By.XPATH, '/html/body/main/section[1]/div/div[1]/div/div/div/form/div/div[1]/div/div')
#     search5.click()
# search_link_button()

sleep()

def paste():
    py.hotkey('ctrl', 'v')
paste()

sleep()

# def download_video():
#     click_download = driver.find_element(By.XPATH, '//*[@id="download-mp4-720-audio"]
#     ')
#     click_download.click()
# download_video()

