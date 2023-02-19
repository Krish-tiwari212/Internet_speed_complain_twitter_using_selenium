from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

path = "C:\dev\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)
driver.get("https://www.speedtest.net/")
start = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
start.click()
while driver.current_url[:32] != ("https://www.speedtest.net/result"):
    down_speed = driver.find_element(By.XPATH,
                                     '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
down_speed = driver.find_element(By.XPATH,
                                 '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
up_speed = driver.find_element(By.XPATH,
                               '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
do = float(down_speed.get_attribute("innerHTML"))
up = float(up_speed.get_attribute("innerHTML"))
if do < 4 and up < 4:
    driver.switch_to.new_window()
    driver.get("https://twitter.com/home?lang=en")
    sleep(6)
    email = driver.find_element(By.XPATH,
                                '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
    email.click()
    email.send_keys("#")
    email.send_keys(Keys.ENTER)
    sleep(4)
    passw = driver.find_element(By.XPATH,
                                '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
    passw.send_keys("#")
    passw.send_keys(Keys.ENTER)
    sleep(8)
    tweet_click = driver.find_element(By.XPATH,
                                      '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]')
    tweet_click.click()
    sleep(3)
    tweet_click = driver.find_element(By.XPATH,
                                      '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
    tweet_click.send_keys(
        f"Internet provider, I was promised the speed of 4mbps up/down but I am only getting {do} down and {up} upload.")
    but = driver.find_element(By.XPATH,
                              '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]')
    but.click()
c = input()
