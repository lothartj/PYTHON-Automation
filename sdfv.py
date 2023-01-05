import os
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

# Open the desktop calculator application
os.startfile("C:\\Users\\lothart\\Desktop\\Amend")

def down():
  py.hotkey('down')

down()
down()
down()
down()
down()
down()

py.hotkey('enter')

def right():
  py.hotkey('6')

right()
right()
right()
right()
right()
right()



