## 크롤링 ver 1.5
#ver 1.1 :  초안 및 메인 코드
#ver 1.2 : 멀티 프로세스를 활용해서 로그인 무한루프 구성
#ver 1.2.1 : 멀티 프로세스를 활용해서 로그인 구성 테스트 공간
#ver 1.3 : 멀티 프로세스에 배열 전달해 각각 배열의 값을 순차적으로 하나씩 사용하는지 테스트
#ver 1.4 : 멀티프로세스를 통해 임시저장까지 테스트 -> false 이뉴는 중복 저장떄문에 안됨
#ver 1.5 :


#Log
# 9월 10일
# 문제점 :
# 다중 로그인시 로그인이 풀리는 현상이 있음
# 이때 현재 솔류션은 로그인 버튼이 존재한다면 다시 쿠키 지우고 로그인 태우는 방식인데 전에 다른곳에서 로그인되어서 튕겻다는 알림창이 나와서 그버튼 없애고 다시 하는거
# 생각해봐야함!!!!

# 9월 11일
# 예외처리로 로그인까지는 완료됨!!
# TODO 함수화 시켜서 무한루프 만들어보기 이건 test2.py 에서 진행 -> 완료
# TODO : 문서24에서 중복 로그인을 막아서 강제로 로그인 한다해도 임서저장단계에서 모든계 막힘... 어떻게 해결해야할까




# 참조
# 링크1 (멀티에서 배열 각각 변수 전달) : https://hamait.tistory.com/755
# 링크2 (input hidden에 script로 값 넣기) : https://www.tutorialspoint.com/how-to-key-in-values-in-input-text-box-with-javascript-executor-in-selenium-with-python





import os
import pickle
from multiprocessing import Process, current_process


from time import sleep
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# import multiprocessing
# driver = webdriver.Chrome("/Users/kimsungsik/Documents/Develop/chrome/chromedriver")

# def crolling(url,number):
def crolling(driver):

    drivertest = pickle.load(driver)

    # chrome_options = Options()
    # chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    # driver = webdriver.Chrome("/Users/kimsungsik/Documents/Develop/chrome/chromedriver", options=chrome_options)
    # driver = webdriver.Safari("/usr/bin/safaridriver")
    # url = 'https://docu.gdoc.go.kr/index.do'
    url = 'https://www.naver.com'
    driver.get(url)
# def crolling(driver):
    # # 옵션 생성
    # options = webdriver.ChromeOptions()
    # # 창 숨기는 옵션 추가
    # options.add_argument("headless")
    # count = 1
    # # while count < 3:
    # driver = webdriver.Chrome("/Users/kimsungsik/Documents/Develop/chrome/chromedriver")
    # # driver = webdriver.Safari("/usr/bin/safaridriver")
    # url = 'https://docu.gdoc.go.kr/index.do'
    # driver.get(url)
    #
    # driver.find_element("xpath", '//*[@id="gnb"]/div/ul/li[6]/a').click()  # 로그인버튼
    # driver.find_element("xpath", '//*[@id="content"]/div/section/div/div[1]/ul/li[1]/a').click()  # 개인사용자 버튼
    # driver.find_element("xpath", '//*[@id="id"]').send_keys("tjdtlr2620@naver.com")  # 아이디
    # driver.find_element("xpath", '//*[@id="password"]').send_keys("as862459@")  # 비빌번호
    # driver.find_element("xpath", '//*[@id="loginDataForm"]/div[3]/div[2]/fieldset/ul/li[2]/button').click()  # 로그인
    driver.execute_script("window.open('');")
    driver.execute_script("window.open('');")
    driver.execute_script("window.open('');")
    print('number : ',number)
    print('url : ',url)
    driver.switch_to.window(driver.window_handles[1])
    driver.get('https://www.naver.com')






    # driver.switch_to.window(driver.window_handles[1])
    # driver.get(url)
    # driver.switch_to.window(driver.window_handles[2])
    # driver.get(url)
    # driver.switch_to.window(driver.window_handles[3])
    # driver.get(url)
    # driver.switch_to.window(driver.window_handles[4])
    # driver.get(url)


    # 로그인 로직 시작
    # driver.find_element("xpath", '//*[@id="gnb"]/div/ul/li[6]/a').click()  # 로그인버튼
    # driver.find_element("xpath", '//*[@id="content"]/div/section/div/div[1]/ul/li[1]/a').click()  # 개인사용자 버튼
    # driver.find_element("xpath", '//*[@id="id"]').send_keys("tjdtlr2620@naver.com")  # 아이디
    # driver.find_element("xpath", '//*[@id="password"]').send_keys("as862459@")  # 비빌번호
    # driver.find_element("xpath", '//*[@id="loginDataForm"]/div[3]/div[2]/fieldset/ul/li[2]/button').click()  # 로그인
    #
    # sleep(2)
    # driver.find_element("xpath", '//*[@id="content"]/section/div[2]/div/div[1]/a[1]').click()  # 문서보내기버튼
    #
    # while driver.find_element("xpath", '//*[@id="gnb"]/div/ul/li[6]/a').text == '로그인':
    #     try:
    #         sleep(2)
    #         driver.delete_all_cookies()
    #         driver.find_element("xpath", '//*[@id="id"]').send_keys("tjdtlr2620@naver.com")  # 아이디
    #         driver.find_element("xpath", '//*[@id="password"]').send_keys("as862459@")  # 비빌번호
    #         driver.find_element("xpath",
    #                             '//*[@id="loginDataForm"]/div[3]/div[2]/fieldset/ul/li[2]/button').click()  # 로그인
    #         sleep(5)
    #     except :
    #         driver.find_element("xpath", '//*[@id="jconfirm-buttons-bottom"]/button').click()
    #         sleep(2)
    #         driver.delete_all_cookies()
    #         driver.find_element("xpath",
    #                             '//*[@id="loginDataForm"]/div[3]/div[2]/fieldset/ul/li[2]/button').click()  # 로그인
    #         sleep(2)
    #         driver.find_element("xpath", '//*[@id="content"]/section/div[2]/div/div[1]/a[1]').click()  # 문서보내기버튼
    #         sleep(5)
    # # 로그인 로직 끝
    #
    #
    # print( driver.get_cookies())
    # # 문서입력 로직 시작
    # driver.find_element("xpath", '//*[@id="contents"]/div/div[1]/div[1]/div/div/label').click()  # 모두예
    # sleep(1.4)
    # driver.find_element("xpath", '//*[@id="jconfirm-buttons-bottom"]/button').click()  # 모달 confirm
    # sleep(1.4)
    #
    #
    #
    #
    # # driver.find_element("xpath", '//*[@id="ldapSearch"]').click()  # 받는기관 클릭
    # # sleep(1.4)
    # # # driver.find_element("xpath", '//*[@id="searchOrgNm"]').send_keys("과학기술정보통신부 우정사업본부 서울지방우정청 서울구로우체국 서울시흥1동우체국") #기관명 작성
    # # # sleep(0.5)
    # # driver.find_element("xpath", '//*[@id="Form"]/button').click()  # 검색클릭
    # # sleep(1.5)
    # # print('총건수 : ', driver.find_element("xpath", '//*[@id="ldapCnt"]').get_attribute("innerText"))
    # #
    # # driver.find_element("xpath", '//*[@id="ldaps"]/tbody/tr[1]/td[1]/button').click()  # 선택 클릭
    #
    # driver.execute_script("document.getElementById('recvOrgCd').value='B553806'")
    # driver.execute_script("document.getElementById('recvOrgNm').value='강원도자원봉사센터장'")
    #
    # sleep(1.5)
    # driver.find_element("xpath", '//*[@id="docTitle"]').send_keys("테스트 중 입니다.")
    #
    # # iframe 값 입력
    # iframe_content = driver.find_element("xpath", '//*[@id="polaris_1_contents"]/iframe')
    # driver.switch_to.frame(iframe_content)
    # content_write = driver.find_element("xpath", "/html/body/p")
    # content_write.clear()
    # content_write.send_keys("!221212211212122435465342343546542343")
    # driver.switch_to.default_content()
    # #
    # sleep(2)
    # driver.find_element("xpath", '//*[@id="apprNm"]').send_keys("@@@@@@@@@@")
    # driver.find_element("xpath", '//input[@id="files_1_c100" and @type="file"]').send_keys(
    #     "/Users/kimsungsik/Desktop/파이썬.png")
    # #
    #
    # # driver.find_element("xpath", '//*[@id="addFiles_1_c100"]').click()
    # sleep(1)
    # driver.find_element("xpath", '//*[@id="saveGian"]').click()
    #
    # # 문서입력 로직 끝
    #


    sleep(30)


# def action( url, number):
    # driver.switch_to.window(driver.window_handles[number])
    # driver.get(url)
    # driver.switch_to.window(driver.window_handles[2])
    # driver.get(url)
    # driver.switch_to.window(driver.window_handles[3])
    # driver.get(url)
    # driver.switch_to.window(driver.window_handles[4])
    # driver.get(url)

def doubler(number):



    result = number * 2
    proc_name = current_process().name
    print('{0} doubled to {1} by: {2}'.format(number, result, proc_name))


if __name__ == '__main__':
    # 옵션 생성
    # options = webdriver.ChromeOptions()
    # 창 숨기는 옵션 추가
    # options.add_argument("headless")
    # count = 1
    # while count < 3:
    # global driver
    driver = webdriver.Chrome("/Users/kimsungsik/Documents/Develop/chrome/chromedriver")


    #
    # driver.find_element("xpath", '//*[@id="gnb"]/div/ul/li[6]/a').click()  # 로그인버튼
    # driver.find_element("xpath", '//*[@id="content"]/div/section/div/div[1]/ul/li[1]/a').click()  # 개인사용자 버튼
    # driver.find_element("xpath", '//*[@id="id"]').send_keys("tjdtlr2620@naver.com")  # 아이디
    # driver.find_element("xpath", '//*[@id="password"]').send_keys("as862459@")  # 비빌번호
    # driver.find_element("xpath", '//*[@id="loginDataForm"]/div[3]/div[2]/fieldset/ul/li[2]/button').click()  # 로그인
    #
    # driver.execute_script("window.open('');")
    # driver.execute_script("window.open('');")
    # driver.execute_script("window.open('');")
    # driver.execute_script("window.open('');")
    #
    #
    # numbers = [1]
    # crolling('https://docu.gdoc.go.kr/index.do',1)
    #
    #
    #
    # #
    # # numbers = [1]
    # # procs = []
    # # # proc = Process(target=doubler, args=(5,))
    # #
    # # for index, number in enumerate(numbers):
    # #     proc = Process(target=crolling, args=(driver,number))
    # #     procs.append(proc)
    # #     proc.start()
    # #
    # # proc = Process(target=doubler, name='Test', args=(2,))
    # # proc.start()
    # # procs.append(proc)
    # #
    # # for proc in procs:
    #
    # # crolling(driver)
    numbers = [1]
    procs = []
    # proc = Process(target=doubler, args=(5,))
    a=''
    b=''
    pickle.dump(driver,a)
    pickle.load(a,b)
    print(a)
    print(b)
    for index, number in enumerate(numbers):
        # proc = Process(target=crolling, args=(driver,))
        proc = Process(target=crolling, args=(pickle.dump(driver),))
        procs.append(proc)
        proc.start()

    proc = Process(target=doubler, name='Test', args=(2,))
    proc.start()
    procs.append(proc)

    for proc in procs:
        proc.join()



#참조 링크 : https://hamait.tistory.com/755