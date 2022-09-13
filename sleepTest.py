import time
from time import sleep
import asyncio
from selenium import webdriver
from selenium.webdriver.common.by import By


# 참고 URL : https://www.daleseo.com/python-asyncio/

async def find_users_async(n,driver):
    # print(n)
    # print(n['num'])
    # await asyncio.sleep(5)
    # print(n['title'])
    # for i in range(1, n + 1):
    #     print(f'{n}명 중 {i}번 째 사용자 조회 중 ...')
    #     await asyncio.sleep(1)
    # print(f'> 총 {n} 명 사용자 비동기 조회 완료!')
    await asyncio.sleep(2)
    driver.switch_to.window(driver.window_handles[n['num']])
    url = 'https://docu.gdoc.go.kr/doc/wte/docWriteForm.do'
    driver.get(url)
    #
    await asyncio.sleep(2)
    driver.find_element("xpath", '//*[@id="contents"]/div/div[1]/div[1]/div/div/label').click()  # 모두예
    # sleep(1.4)
    # driver.find_element("xpath", '//*[@id="jconfirm-buttons-bottom"]/button').click()  # 모달 confirm
    # sleep(1.4)

    # await asyncio.sleep(1.4)
    #
    #
    # driver.execute_script("document.getElementById('recvOrgCd').value='B553806'")
    # driver.execute_script("document.getElementById('recvOrgNm').value='강원도자원봉사센터장'")
    #
    # driver.find_element("xpath", '//*[@id="docTitle"]').send_keys(n['title'])
    # # driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    # await asyncio.sleep(2)
    # driver.find_element("xpath", '//*[@id="apprNm"]').send_keys("@@@@@@@")
    #
    # driver.find_element("xpath", '//input[@id="files_1_c100" and @type="file"]').send_keys(
    #     "/Users/kimsungsik/Desktop/파이썬.png")
    # # await asyncio.sleep(1)
    # # driver.find_element("xpath", '//*[@id="saveGian"]').click()
    #
    # await asyncio.sleep(1)
    # driver.find_element("xpath", '//*[@id="saveGian"]').click()
    # # driver.find_element("xpath", '//*[@id="jconfirm-buttons-bottom"]/button').click()
    # # driver.find_element("xpath", '//*[@id="saveGian"]').click()
    #
    # # print('!!',driver.find_element("xpath",'//*[@id="jconfirm-box81249"]/div').text)

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
    end = time.time()
    print(f'>>> 비동기 처리 총 소요 시간: {end - start}')

if __name__ == '__main__':
    driver = webdriver.Chrome("/Users/kimsungsik/Documents/Develop/chrome/chromedriver")
    url = 'https://docu.gdoc.go.kr/index.do'
    driver.get(url)
    driver.find_element("xpath", '//*[@id="gnb"]/div/ul/li[6]/a').click()  # 로그인버튼
    driver.find_element("xpath", '//*[@id="content"]/div/section/div/div[1]/ul/li[1]/a').click()  # 개인사용자 버튼
    driver.find_element("xpath", '//*[@id="id"]').send_keys("tjdtlr2620@naver.com")  # 아이디
    driver.find_element("xpath", '//*[@id="password"]').send_keys("as862459@")  # 비빌번호
    driver.find_element("xpath", '//*[@id="loginDataForm"]/div[3]/div[2]/fieldset/ul/li[2]/button').click()  # 로그인

    driver.execute_script("window.open('');")
    driver.execute_script("window.open('');")
    driver.execute_script("window.open('');")
    driver.execute_script("window.open('');")

    asyncio.run(process_async(driver))
