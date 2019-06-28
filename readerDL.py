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

    #Go to Adobe Reader site, click download button
    browser = webdriver.Chrome(chrome_options=chromeOptions)
    browser.get(('https://get.adobe.com/reader/'))
    time.sleep(1)

    #Uncheck each extension
    uncheck1 = browser.find_element_by_id('chrExtCheckbox').click()
    uncheck2 = browser.find_element_by_id('offerCheckbox').click()
    uncheck3 = browser.find_element_by_id('offerCheckbox1').click()

    #Hit download button
    adobeDownload = browser.find_element_by_id('buttonDownload').click()
    time.sleep(20)

    browser.quit()

    #Find file name that matches the download file, then start it
    #dirname = r'C:\Users\Administrator\Downloads\\'
    dirname = r'C:/Users/' + usernameStr + '/Downloads/'
    for filename in os.listdir(dirname):
        root, ext = os.path.splitext(filename)
        if root.startswith('readerdc') and ext == '.exe':
            readerVLC = App().start(dirname + filename)
      
    time.sleep(1)

    #Clicks through wizard
    installer = appAdobe['Adobe Acrobat Reader DC Installer']
    installer.Finish.click()
   
else:
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, "", None, 1)
    






