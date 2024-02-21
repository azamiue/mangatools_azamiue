from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
import undetected_chromedriver as uc
import chapterChecking
import keyboard

def fetchingURL(url, option, type):
    options = webdriver.ChromeOptions()
    driver = type.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)


    driver.get(url)
    
    if option == 1:
        chapterChecking.chapterChecking()
    else:
        pass

    while True:
        if keyboard.is_pressed('q'):
            break

if __name__ == '__main__':
    fetchingURL('https://www.coffeemanga.io/wp-admin', 1, uc)



