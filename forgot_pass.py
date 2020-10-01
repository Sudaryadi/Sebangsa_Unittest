import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from unittest import TestCase
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


class LoginTest(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.get("https://sebangsa.com/")
        self.driver.maximize_window()
        sleep(5)

    def test_login(self):

        driver = self.driver
        driver.find_element_by_xpath('//*[@id="dropbtn-login"]').click()
        sleep(5)
        driver.find_element_by_xpath('//*[@id="loginForm"]/p[3]/a/strong').click()
        sleep(5)
        driver.find_element_by_id('username').send_keys("kalung")
        sleep(5)
        driver.find_element_by_xpath('//*[@id="loginForm"]/div[2]/button').click()



        # Pindah new tab untuk email verification #
        driver.execute_script("window.open('https://www.mailinator.com/', 'new window')")
        driver.switch_to.window(driver.window_handles[0])
        sleep (3)

        driver.switch_to.window(driver.window_handles[1])
        driver.find_element_by_id('addOverlay').send_keys("kalung")
        driver.find_element_by_id('go-to-public').click()
        sleep(3)
        driver.find_element_by_xpath('//*[@id="row_kalung-1600908557-838444"]/td[4]/a').click()
        sleep(5)
        # Kembali masuk website melalui tautan di inbox #
        baseurl = 'https://sebangsa.com/changepass/kalung/1600905048887/b2caedd356aa1d58c4aee559dcec36d5d0d293ee3d9ddeab3974bed795817a1726378f386a5f51a1b8bc75306bfada4823b99f19828c1a43610f11bd9c88f987'
        driver.execute_script("window.open('baseurl', 'new window')")
        driver.get(baseurl)

        #driver.switch_to_window(driver.window_handles[1])
        #sleep (3)
        #driver.switch_to_window(driver.window_handles[2])

        sleep(5)
        # Ganti password baru #
        driver.find_element_by_id('password').send_keys("kalung")
        driver.find_element_by_id('passwordConf').send_keys("kalung")
        sleep(3)
        driver.find_element_by_xpath('//*[@id="changePassword"]/button').click()
        sleep(5)
        # Login dengan password baru #
        driver.find_element_by_id('username').send_keys("kalung")
        sleep(5)
        driver.find_element_by_id('password').send_keys("kalung")
        sleep(5)
        driver.find_element_by_xpath('//*[@id="loginForm"]/p[2]/button').click()
        sleep(8)
        # Verifikasi profil user #
        profil_user = driver.find_element_by_xpath('//*[@id="site-container"]/div[5]/div/div[1]/div/section/div[1]/div[2]/div/a')
        cek_profil = profil_user.get_attribute('title')
        print
        cek_profil
        self.assertRegex(cek_profil, 'kalung')

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()