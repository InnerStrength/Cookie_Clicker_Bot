from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service("C:\Development\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("http://orteil.dashnet.org/cookieclicker/")
timeout = 60
cookie = driver.find_element(By.ID, "bigCookie")
endgame = 7200
upgrades_path = '/html/body/div[2]/div[2]/div[19]/div[3]/div[5]/div'
products_path = '/html/body/div/div[2]/div[19]/div[3]/div[6]/div'


def try_click(path):
    list = driver.find_elements(By.XPATH, path)
    list.reverse()
    try:
        for l in list:
            try:
                l.click()
            except:
                pass
    except TypeError:
        pass


def game():
    interval_time = time.time()
    while time.time() < interval_time + timeout:
        test = 0
        cookie.click()
        if test == timeout:
            break
        test -= 1


main_time = time.time()
while time.time() < main_time + endgame:
    test = 0
    try_click(upgrades_path)
    try_click(products_path)
    try:
        driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[8]/div/div[1]').click()
    except:
        pass

    game()
    if test == endgame:
        break
    test -= 1

time.sleep(1)
print(f"final cookie {driver.find_element(By.CSS_SELECTOR,'#cookies div').text}")

driver.quit()