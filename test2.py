## 크롤링 ver 1.2.1
#ver 1.1 :  초안 및 메인 코드
#ver 1.2 : 멀티 프로세스를 활용해서 로그인 무한루프 구성
#ver 1.2.1 : 멀티 프로세스를 활용해서 로그인 구성 테스트 공간

# Log
# 9월 10일
# 문제점 :
# 다중 로그인시 로그인이 풀리는 현상이 있음
# 이때 현재 솔류션은 로그인 버튼이 존재한다면 다시 쿠키 지우고 로그인 태우는 방식인데 전에 다른곳에서 로그인되어서 튕겻다는 알림창이 나와서 그버튼 없애고 다시 하는거
# 생각해봐야함!!!!

# 9월 11일
# 예외처리로 로그인까지는 완료됨!!
# TODO 함수화 시켜서 무한루프 만들어보기 이건 test2.py 에서 진행



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
    # while count < 3:
    driver = webdriver.Chrome("/Users/kimsungsik/Documents/Develop/chrome/chromedriver")
    # driver = webdriver.Safari("/usr/bin/safaridriver")
    url = 'https://docu.gdoc.go.kr/index.do'
    driver.get(url)

    driver.find_element("xpath", '//*[@id="gnb"]/div/ul/li[6]/a').click()  # 로그인버튼
    driver.find_element("xpath", '//*[@id="content"]/div/section/div/div[1]/ul/li[1]/a').click()  # 개인사용자 버튼
    driver.find_element("xpath", '//*[@id="id"]').send_keys("tjdtlr2620@naver.com")  # 아이디
    driver.find_element("xpath", '//*[@id="password"]').send_keys("as862459@")  # 비빌번호
    driver.find_element("xpath", '//*[@id="loginDataForm"]/div[3]/div[2]/fieldset/ul/li[2]/button').click()  # 로그인

    sleep(2)
    driver.find_element("xpath", '//*[@id="content"]/section/div[2]/div/div[1]/a[1]').click()  # 문서보내기버튼

    if driver.find_element("xpath", '//*[@id="gnb"]/div/ul/li[6]/a').text == '로그인':
        sleep(2)
        driver.delete_all_cookies()
        driver.find_element("xpath", '//*[@id="content"]/div/section/div/div[1]/ul/li[1]/a').click()  # 개인사용자 버튼
        driver.find_element("xpath", '//*[@id="id"]').send_keys("tjdtlr2620@naver.com")  # 아이디
        driver.find_element("xpath", '//*[@id="password"]').send_keys("as862459@")  # 비빌번호
        driver.find_element("xpath", '//*[@id="loginDataForm"]/div[3]/div[2]/fieldset/ul/li[2]/button').click()  # 로그인
        sleep(5)

        if driver.find_element("xpath", '//*[@id="gnb"]/div/ul/li[6]/a').text == '로그인':
            try:
                sleep(2)
                driver.delete_all_cookies()
                driver.find_element("xpath", '//*[@id="content"]/div/section/div/div[1]/ul/li[1]/a').click()  # 개인사용자 버튼
                driver.find_element("xpath", '//*[@id="id"]').send_keys("tjdtlr2620@naver.com")  # 아이디
                driver.find_element("xpath", '//*[@id="password"]').send_keys("as862459@")  # 비빌번호
                driver.find_element("xpath",'//*[@id="loginDataForm"]/div[3]/div[2]/fieldset/ul/li[2]/button').click()  # 로그인
                sleep(5)
            except:
                driver.find_element("xpath", '//*[@id="jconfirm-buttons-bottom"]/button').click()
                sleep(2)
                driver.delete_all_cookies()
                driver.find_element("xpath",'//*[@id="loginDataForm"]/div[3]/div[2]/fieldset/ul/li[2]/button').click()  # 로그인
                sleep(2)
                driver.find_element("xpath", '//*[@id="content"]/section/div[2]/div/div[1]/a[1]').click()  # 문서보내기버튼
                print("로그인 버튼인지? 4", driver.find_element("xpath", '//*[@id="gnb"]/div/ul/li[6]/a').text == '로그인')
                sleep(5)

        # sleep(5)
    driver.find_element("xpath", '//*[@id="contents"]/div/div[1]/div[1]/div/div/label').click()  # 모두예
    sleep(1.4)

    sleep(30)


'//*[@id="jconfirm-buttons-bottom"]/button'

if __name__ == '__main__':
    processes = []
    for _ in range(5):
        p = multiprocessing.Process(target=crolling)  ## 각 프로세스에 작업을 등록
        p.start()
        processes.append(p)

    for process in processes:
        process.join()

