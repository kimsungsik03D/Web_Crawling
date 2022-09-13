## 크롤링 ver 1.5
#ver 1.1 :  초안 및 메인 코드
#ver 1.2 : 멀티 프로세스를 활용해서 로그인 무한루프 구성
#ver 1.2.1 : 멀티 프로세스를 활용해서 로그인 구성 테스트 공간
#ver 1.3 : 멀티 프로세스에 배열 전달해 각각 배열의 값을 순차적으로 하나씩 사용하는지 테스트
#ver 1.4 : 멀티프로세스를 통해 임시저장까지 테스트 -> false 이뉴는 중복 저장떄문에 안됨
#ver 1.5 : 비동기 처리로 프로토타입 구성 완성 - 완성


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

#9월13일
# 1차 프로토타입은 완료

# 참고
# 링크1 (멀티에서 배열 각각 변수 전달) : https://hamait.tistory.com/755
# 링크2 (input hidden에 script로 값 넣기) : https://www.tutorialspoint.com/how-to-key-in-values-in-input-text-box-with-javascript-executor-in-selenium-with-python

# 링크3  : https://www.daleseo.com/python-asyncio/


import time
from time import sleep
import asyncio
from selenium import webdriver


async def find_users_async(n,driver):
    print(n)
    print(n['num'])
    print(n['title'])

    if n['num']!=0:
        driver.switch_to.window(driver.window_handles[n['num']])
    url = 'https://docu.gdoc.go.kr/doc/wte/docWriteForm.do'
    # url = 'https://docu.gdoc.go.kr/index.do'
    driver.get(url)

    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    sleep(0.4)
    driver.execute_script('window.scrollTo(0,0)')
    driver.find_element("xpath", '//*[@id="contents"]/div/div[1]/div[1]/div/div/label').click()  # 모두예
    driver.find_element("xpath", '//*[@id="jconfirm-buttons-bottom"]/button').click()  # 모달 confirm
    sleep(0.4)
    driver.execute_script('window.scrollTo(0,500)')
    driver.execute_script("document.getElementById('recvOrgCd').value='B553806'")
    driver.execute_script("document.getElementById('recvOrgNm').value='강원도자원봉사센터장'")

    driver.find_element("xpath", '//*[@id="docTitle"]').send_keys(n['title'])

    # await asyncio.sleep(2)
    sleep(0.4)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    driver.find_element("xpath", '//*[@id="apprNm"]').send_keys("@@@@@@@")



    driver.find_element("xpath", '//input[@id="files_1_c100" and @type="file"]').send_keys("/Users/kimsungsik/Desktop/png-transparent-python-logo-thumbnail.png")
    sleep(1.5)
    try:
        driver.find_element("xpath", '//*[@id="saveGian"]').click()  # 임시저장버튼
        sleep(1)
        driver.find_element("xpath", '//*[@id="jconfirm-buttons-bottom"]/button').click()
        driver.find_element("xpath",'//*[@id="delDoc"]').click()

    except:
        try:
            print("예외! %d",n['num'])
            driver.find_element("xpath", '//*[@id="saveGian"]').click()  # 임시저장버튼
            sleep(1)
            driver.find_element("xpath", '//*[@id="jconfirm-buttons-bottom"]/button').click()
        except:
            return;

        driver.find_element("xpath", '//*[@id="saveGian"]').click()


async def process_async(driver):
    start = time.time()
    data = [{'num':0,'title':'제목0'},
            {'num':1,'title':'제목1'},
            {'num':2,'title':'제목2'},
            {'num':3,'title':'제목3'},
            {'num':4,'title':'제목4'}]
    await asyncio.wait([
        find_users_async(data[0], driver),
        find_users_async(data[1], driver),
        find_users_async(data[2], driver),
        find_users_async(data[3], driver),
        find_users_async(data[4], driver),
    ])

    driver.quit()
    end = time.time()
    print(f'>>> 비동기 처리 총 소요 시간: {end - start}')


if __name__ == '__main__':
    driver = webdriver.Chrome("/Users/kimsungsik/Documents/Develop/chrome/chromedriver")
    url = 'https://docu.gdoc.go.kr/index.do'
    # url = 'https://docu.gdoc.go.kr/doc/wte/docWriteForm.do'
    driver.get(url)
    driver.find_element("xpath", '//*[@id="gnb"]/div/ul/li[6]/a').click()  # 로그인버튼
    driver.find_element("xpath", '//*[@id="content"]/div/section/div/div[1]/ul/li[1]/a').click()  # 개인사용자 버튼
    driver.find_element("xpath", '//*[@id="id"]').send_keys("tjdtlr2620@naver.com")  # 아이디
    driver.find_element("xpath", '//*[@id="password"]').send_keys("as862459@")  # 비빌번호
    driver.find_element("xpath", '//*[@id="loginDataForm"]/div[3]/div[2]/fieldset/ul/li[2]/button').click()  # 로그인
    sleep(0.4)
    driver.find_element("xpath", '//*[@id="content"]/section/div[2]/div/div[1]/a[1]').click()  # 문서보내기버튼

    driver.execute_script("window.open('');")
    # driver.execute_script("window.open('');")
    # driver.execute_script("window.open('');")
    # driver.execute_script("window.open('');")

    asyncio.run(process_async(driver))


# 9월 13일 로직 완성
# xpath를 활용해 구성됨.
# Logic
# 1. 로그인
# 2. 새 탭 만들기
# 3. process_async()에서 비동기로 처리할 파라미터 던지기
# 4. find_users_async() 에서 받은 파라미터의 정보를 통해 이의신청 문서 작성
#    중간중간 스크롤을 통해 입력해야하는 부분 으로 이동해ㅓㅅ 입력하는중
# TODO : 스크랩핑할때 코드도 같이 스크랩핑 가능한지 확인해야함.
