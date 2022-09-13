# 웹 크롤링 (ver 1.0)

<h4>문서 24 웹크롤링<br></h4>
<p>주요 동작</p>
<p>문서 24 접속 -> 로그인 -> 문서작성 -> 기관, 제목, 내용, 첨부파일, 임시저장</p>
<hr>
<p>사용 라이브러리</p>
<p>asyncio 3.4.3<br>selenium 4.4.3</p>
<hr>
<h3><p>동작 설명</p></h3>
<p>1. 드라이버 경로</p>

```
driver = webdriver.Chrome(driverPath)
```


<p>2. URL 이동</p>

```
driver.get(url)
```

<p>3. 클릭</p>

```
driver.find_element("xpath", '//*[@id="gnb"]/div/ul/li[6]/a').click()  # 로그인버튼
```

<p>4. 입력</p>

```
driver.find_element("xpath", '//*[@id="id"]').send_keys("tjdtlr2620@naver.com")  # 아이디
```

<p>5. 대기</p>

```
sleep(0.4)
```

<p>6. 자바스크립스 사용(새창)</p>

```
driver.execute_script("window.open('');")
```
<p>7. 자바스크립스 사용(창 선택)</p>

```
driver.switch_to.window(driver.window_handles[n['num']])
```

<p>8. 자바스크립스 사용(스크롤 제)</p>

```
driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
driver.execute_script('window.scrollTo(0,0)')
driver.execute_script('window.scrollTo(X,Y)')
```


<p>9. 파일첨부</p>

```
driver.find_element("xpath", '//input[@id="files_1_c100" and @type="file"]').send_keys(filePath)
```
<p>10. 비동기 호출 로직</p>

``` phthon
asyncio.run(process_async(driver))

async def process_async(driver):
    start = time.time()
    data = [...]
    await asyncio.wait([
        find_users_async(data[0], driver),
        find_users_async(data[1], driver),
    ])
    end = time.time()
    print(f'>>> 비동기 처리 총 소요 시간: {end - start}')
    
async def find_users_async(n,driver):
    print(n)
    print(n['num'])
    print(n['title'])
```

 