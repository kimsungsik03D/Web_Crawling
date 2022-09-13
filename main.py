## 크롤링 ver 1.1
#ver 1.1 :  초안 및 메인 코드



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

    print(
        WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.XPATH, '//*[@id="gnb"]/div/ul/li[6]/a'))))
    print(EC.presence_of_element_located((By.XPATH, '//*[@id="gnb"]/div/ul/li[6]/a')))
    print('로그인1 : ',EC.presence_of_element_located((By.XPATH, '//*[@id="gnb"]/div/ul/li[6]/a[contain(text(),"로그인")]')))
    print('로그아웃1 : ',EC.presence_of_element_located((By.XPATH, '//*[@id="gnb"]/div/ul/li[6]/a[contain(text(),"로그아웃")]')))
    print('로그인2 : ', driver.find_element("xpath", "//*[@id='gnb']/div/ul/li[6]/a").text == '로그인')
    print('로그인3 : ', driver.find_element("xpath", "//*[@id='gnb']/div/ul/li[6]/a").text != '로그인')
    # print('로그아웃2 : ',EC.presence_of_element_located((By.XPATH, '//*[@id="gnb"]/div/ul/li[6]/a[contain(text(),"로그아웃")]')))
    # a = driver.find_element("xpath", '//*[@id="gnb"]/div/ul/li[6]/a[contain(text(),"로그인")]')
    # print('a : ',a)
    driver.find_element("xpath", '//*[@id="gnb"]/div/ul/li[6]/a').click()  # 로그인버튼
    driver.find_element("xpath", '//*[@id="content"]/div/section/div/div[1]/ul/li[1]/a').click()  # 개인사용자 버튼
    driver.find_element("xpath", '//*[@id="id"]').send_keys("tjdtlr2620@naver.com")  # 아이디
    driver.find_element("xpath", '//*[@id="password"]').send_keys("as862459@")  # 비빌번호
    driver.find_element("xpath", '//*[@id="loginDataForm"]/div[3]/div[2]/fieldset/ul/li[2]/button').click()  # 로그인

    sleep(2)

    print('로그인4 : ', driver.find_element("xpath", "//*[@id='gnb']/div/ul/li[6]/a").text == '로그인')
    print('로그인5 : ', driver.find_element("xpath", "//*[@id='gnb']/div/ul/li[6]/a").text != '로그인')
    driver.find_element("xpath", '//*[@id="content"]/section/div[2]/div/div[1]/a[1]').click()  # 문서보내기버튼

    sleep(2)

    if driver.find_element("xpath", "//*[@id='gnb']/div/ul/li[6]/a").text == '로그인':
        driver.find_element("xpath", '//*[@id="gnb"]/div/ul/li[6]/a').click()  # 로그인버튼
        driver.find_element("xpath", '//*[@id="content"]/div/section/div/div[1]/ul/li[1]/a').click()  # 개인사용자 버튼
        driver.find_element("xpath", '//*[@id="id"]').send_keys("tjdtlr2620@naver.com")  # 아이디
        driver.find_element("xpath", '//*[@id="password"]').send_keys("as862459@")  # 비빌번호
        driver.find_element("xpath", '//*[@id="loginDataForm"]/div[3]/div[2]/fieldset/ul/li[2]/button').click()  # 로그인
        sleep(1)
        driver.find_element("xpath", '//*[@id="jconfirm-buttons-bottom"]/button[2]').click()  # 로그인
        sleep(2)
        driver.find_element("xpath", '//*[@id="content"]/section/div[2]/div/div[1]/a[1]').click()  # 문서보내기버튼

    driver.find_element("xpath", '//*[@id="contents"]/div/div[1]/div[1]/div/div/label').click()  # 모두예
    sleep(1.4)
    driver.find_element("xpath", '//*[@id="jconfirm-buttons-bottom"]/button').click()  # 모달 confirm
    sleep(1.4)
    #기관 검색 모달 열기
    # driver.find_element("xpath", '//*[@id="ldapSearch"]').click()  # 받는기관 클릭
    # sleep(1.4)
    # driver.find_element("xpath", '//*[@id="searchOrgNm"]').send_keys("과학기술정보통신부 우정사업본부 서울지방우정청 서울구로우체국 서울시흥1동우체국") #기관명 작성
    # sleep(0.5)
    # driver.find_element("xpath", '//*[@id="Form"]/button').click()  # 검색클릭

    # JavascriptExecutor
    # js = (JavascriptExecutor)
    # driver;
    driver.execute_script("document.getElementById('recvOrgCd').value='B553806'")
    driver.execute_script("document.getElementById('recvOrgNm').value='강원도자원봉사센터장'")
    # driver.executeScript();
    # driver.findElement(By.id("ElementId")).click();
    # driver.findElement(By.id("ElementId")).clear();
    # driver.findElement(By.id("ElementId")).sendKeys("theTextYouWant");
    #기관 input 강제 입력
    # driver.find_element("xpath", '//*[@id="recvOrgCd"]').send_keys("B553806") #기관 코드 입력
    # driver.find_element("xpath", '//*[@id="recvOrgNm"]').send_keys("강원도자원봉사센터장") #기관명 작성
    # sleep(1.5)
    # print('총건수 : ', driver.find_element("xpath", '//*[@id="ldapCnt"]').get_attribute("innerText"))

    # driver.find_element("xpath", '//*[@id="ldaps"]/tbody/tr[1]/td[1]/button').click()  # 선택 클릭
    # sleep(1.5)
    driver.find_element("xpath",'//*[@id="docTitle"]').send_keys("@테스트 중 입니다.")

    # iframe 값 입력
    iframe_content = driver.find_element("xpath", '//*[@id="polaris_1_contents"]/iframe')
    driver.switch_to.frame(iframe_content)
    content_write = driver.find_element("xpath", "/html/body/p")
    content_write.clear()
    content_write.send_keys("!221212211212122435465342343546542343")
    driver.switch_to.default_content()
    #
    sleep(2)
    driver.find_element("xpath", '//*[@id="apprNm"]').send_keys("@@@@@@@@@@")
    driver.find_element("xpath", '//input[@id="files_1_c100" and @type="file"]').send_keys("/Users/kimsungsik/Desktop/파이썬.png")
    #

    # driver.find_element("xpath", '//*[@id="addFiles_1_c100"]').click()
    sleep(1)
    driver.find_element("xpath", '//*[@id="saveGian"]').click()
    #
    #
    sleep(2)
    count += 1
    print(count)
    print(" 종료")
    driver.quit()
    #
    #


def do_something():
    print('1초간 잠을 잡니다...')
    time.sleep(1)
    print('잠에서 깨었습니다...')

if __name__ == '__main__':
    crolling()

    # start = time.perf_counter()

    # processes = []
    # for _ in range(2):
    #     p = multiprocessing.Process(target=crolling)  ## 각 프로세스에 작업을 등록
    #     p.start()
    #     processes.append(p)
    #
    # for process in processes:
    #     process.join()

    # finish = time.perf_counter()







    # 태그             : driver.find_element("tag name", 'table')
    # xpath           : driver.find_element("xpath", '//*[@id="docTitle"]')
    # text 추출        : driver.find_element("xpath",'//*[@id="ldaps"]/tbody/tr[1]/td[2]').get_attribute("innerText")
    # input value 추출 : driver.find_element("xpath",'//*[@id="ldaps"]/tbody/tr[1]/td[2]').get_attribute("value")
    # click           : driver.find_element("xpath", '//*[@id="ldaps"]/tbody/tr[1]/td[1]').click()
    # input           : driver.find_element("xpath",'//*[@id="id"]').send_keys("text")

    # Chome 버전 103.0.5060.114(공식 빌드) (arm64)


