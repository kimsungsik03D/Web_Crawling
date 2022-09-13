import requests
import json

# project_End : 2022년 07월 20일
# Refatoring : 2022년 07월 20일 17시
# developer : Kimsungsik (Bob)


if __name__ == '__main__':
    # host = 'localhost'
    # user = 'root'
    # password = 'Root1234'
    # db = 'pincar_v3'
    # charset = 'utf8'
    # port='3306'
    # # conn = pymysql.connect(host = 'localhost',user = 'root',password = 'Root1234',db = 'pincar_v3',charset = 'utf8',port=3306)
    # conn = pymysql.connect(host,user,password,db,charset,port)
    # cur = conn.cursor()
    #
    # sql = 'select * from user'
    # cur.execute(sql)
    #
    # for row in cur:
    #     print(row[0], row[1], row[2], row[3])
    #
    #
    #

    # 로그인이 필요한 화면일경우 sesison을 통해 로그인상태 구현 후 실제 페이지 크롤링 진행.
    sess = requests.session()
    # 로그인시 필요한 data -> Web_개발자도구_Network 로그인 Logic 확인 후 해당 파일에서 Payload에 FormData를 활용
    # 수정시 id, password 맞춰 수정.
    data = {
        "termYn": "N",
        "sbscrbCode": "G",
        "kakaoConnectId": '',
        "naverConnectId": '',
        "mberSe": "P",
        "redirectUrl": "",
        "plainText": "b6c4uCh4xTAW1P-R9pTWdv0Ju5S2xSXm9NcTXcYK",
        "signedText": "",
        "mberSeEntrprs": "CA",
        "id": "tjdtlr2620@naver.com",
        "password": "as862459@",
        "idSave": "on",
        "certFlag": "N"
    }

    # loginLogic에서 Headers부분에 RequestURL 참고
    # 통신방법에 따라 post, get
    res = sess.post("https://docu.gdoc.go.kr/cmm/main/login.do", data=data)


    # 실제 크롤링 하고지하는 페이지 구성
    # 2022년 7월 20일 16:00 Page : 12844
    # 2022년 7월 20일 16:00 Data : 64220
    with open('/Users/gimseongsig/Desktop/scraping_test4.txt', "a") as file:
        count = 1
        for page in range(1, 12845):
            print("page : ", page)
            data = {
                "currentPage": page,
                "currentMyPage": "1",
                "currentFavPage": "1",
                "currentRecvGroupPage": "1",
                "orderNm": "0",
                "searchOrgNm": ""
            }
            res = sess.post("https://docu.gdoc.go.kr/cmm/ldap/selectLdapList.do", data=data)

            J_res = json.loads(res.text)
            print(J_res['resultList'])
            # 1 페이지 당 5개의 항목 file에 입력
            for data in range(0, 5):
                file.write(str(count) + " : " + J_res['resultList'][data]['ou'] + " | " + J_res['resultList'][data]['ucorgfullname'] + "\n")
                count += 1
            file.write("\n") # 페이지별 공백추가.

    print("Complete Loop And Save")
    file.close()