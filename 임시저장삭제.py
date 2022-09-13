#문서24 자동 임시저장 삭제 로직 - 완성


from time import sleep
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import multiprocessing


def crolling():
    # 옵션 생성
    options = webdriver.ChromeOptions()
    # 창 숨기는 옵션 추가
    options.add_argument("headless")
    count = 1
    driver = webdriver.Chrome("/Users/kimsungsik/Documents/Develop/chrome/chromedriver")
    url = 'https://docu.gdoc.go.kr/doc/wte/docWriteList.do'
    driver.get(url)


    driver.find_element("xpath", '//*[@id="content"]/div/section/div/div[1]/ul/li[1]/a').click()  # 개인사용자 버튼
    driver.find_element("xpath", '//*[@id="id"]').send_keys("tjdtlr2620@naver.com")  # 아이디
    driver.find_element("xpath", '//*[@id="password"]').send_keys("as862459@")  # 비빌번호
    driver.find_element("xpath", '//*[@id="loginDataForm"]/div[3]/div[2]/fieldset/ul/li[2]/button').click()  # 로그인
    sleep(2)
    i=0
    while (i < 30):
        driver.find_element("xpath", '//*[@id="contents"]/div/table/tbody/tr[1]/td[2]/a').click()  # 게시글클릭
        sleep(1)
        driver.find_element("xpath", '//*[@id="delDoc"]').click()  # 삭제클릭
        sleep(1)
        driver.find_element("xpath", '//*[@id="jconfirm-buttons-bottom"]/button[2]').click()  # 삭제 예 클릭
        sleep(1)
        driver.find_element("xpath", '//*[@id="jconfirm-buttons-bottom"]/button').click()  # 확인클
        sleep(1.5)
        i+=1

    driver.quit()


def do_something():
    print('1초간 잠을 잡니다...')
    time.sleep(1)
    print('잠에서 깨었습니다...')

if __name__ == '__main__':
    crolling()


    # 태그             : driver.find_element("tag name", 'table')
    # xpath           : driver.find_element("xpath", '//*[@id="docTitle"]')
    # text 추출        : driver.find_element("xpath",'//*[@id="ldaps"]/tbody/tr[1]/td[2]').get_attribute("innerText")
    # input value 추출 : driver.find_element("xpath",'//*[@id="ldaps"]/tbody/tr[1]/td[2]').get_attribute("value")
    # click           : driver.find_element("xpath", '//*[@id="ldaps"]/tbody/tr[1]/td[1]').click()
    # input           : driver.find_element("xpath",'//*[@id="id"]').send_keys("text")

    # Chome 버전 103.0.5060.114(공식 빌드) (arm64)


