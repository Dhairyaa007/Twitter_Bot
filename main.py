from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

DOWNLOAD = 0
UPLOAD = 0
TWEE_MAIL = 'Your Email'
TWEE_PSWD = 'Your Password'


class InternetSpeedTwitterBot:

    def __init__(self):
        self.chrome_driver_path = Service("C://Program Files (x86)/chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.chrome_driver_path)
        self.driver.maximize_window()
        self.down = 100
        self.up = 10
        self.get_internet_speed()
        self.tweet_msg()

    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net/')
        go_button = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[1]')
        go_button.click()
        time.sleep(60)
        download_speed = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div['
                                                            '3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div['
                                                            '1]/div/div[2]/span').text
        print(download_speed)
        upload_speed = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div['
                                                          '3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div['
                                                          '2]/span').text
        print(upload_speed)
        global DOWNLOAD, UPLOAD
        DOWNLOAD = download_speed
        UPLOAD = upload_speed

    def tweet_msg(self):
        self.driver.get('https://twitter.com/i/flow/login')

        time.sleep(10)
        username = self.driver.find_element(By.NAME, 'text')
        username.send_keys(TWEE_MAIL)
        next_btn = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div['
                                                      '2]/div/div/div[2]/div[2]/div/div/div/div[6]/div')
        next_btn.click()

        time.sleep(10)
        user_verify = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div['
                                                         '2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div['
                                                         '2]/div/input')
        user_verify.send_keys('ImmortalDrince')
        next_btn = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div['
                                                      '2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div')
        next_btn.click()

        time.sleep(10)
        password = self.driver.find_element(By.NAME, 'password')
        password.send_keys(TWEE_PSWD)
        login_btn = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div['
                                                       '2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div')
        login_btn.click()

        time.sleep(10)
        tweet_btn = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div['
                                                       '1]/div[3]/a/div')
        tweet_btn.click()

        time.sleep(5)
        tweet_compose = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div['
                                                           '2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div['
                                                           '2]/div[1]/div/div/div/div/div/div['
                                                           '2]/div/div/div/div/label/div[1]/div/div/div/div/div/div['
                                                           '2]/div/div/div/div')
        tweet_msg = f'Hey there! My Download speed is: {DOWNLOAD} and Upload speed is: {UPLOAD}'
        tweet_compose.send_keys(tweet_msg)
        tweet_post_btn = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div['
                                                            '2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div['
                                                            '2]/div[3]/div/div/div[2]/div[4]/div/span/span')
        tweet_post_btn.click()


Tweebot = InternetSpeedTwitterBot()
