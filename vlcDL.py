### Import modules ###
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from pywinauto.application import Application as App
import pywinauto
import ctypes, sys
import os

#To elevate priviledges during download
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    usernameStr = input('Username: ')

    #Change Chrome options
    chromeOptions = webdriver.ChromeOptions()
    prefs = {'safebrowsing.enabled': 'false'}
    chromeOptions.add_experimental_option("prefs", prefs)

    #Go to VLC site, click download button
    browser = webdriver.Chrome(chrome_options=chromeOptions)
    browser.get(('https://www.videolan.org/vlc/download-windows.html'))
    vlcDownload = browser.find_element_by_id('downloadButton2').click()
    time.sleep(25)

    browser.quit()

    #Find file name that matches the download file, then start it
    #dirname = r'C:\Users\Administrator\Downloads\\'
    dirname = r'C:/Users/' + usernameStr + '/Downloads/'
    for filename in os.listdir(dirname):
        root, ext = os.path.splitext(filename)
        if root.startswith('vlc') and ext == '.exe':
            appVLC = App().start(dirname + filename)
    
    time.sleep(1)

    #Clicks through wizard
    lang = appVLC['Installer Language']
    lang.Ok.click()

    setUp = appVLC['VLC media player Setup']
    setUp.Next.click()
    time.sleep(1)
    setUp.Next.click()
    time.sleep(1)
    setUp.Next.click()
    time.sleep(10)
    setUp.Install.click()


else:
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, "", None, 1)



