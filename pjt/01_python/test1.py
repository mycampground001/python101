import os
import requests
import csv
#영화 대표코드, 영화명, 해당일 누적관객수, 해당일 기록
#boxoffice.csv에 저장한다.
key = os.getenv('KOBIS_KEY')
#vi ~/.bash_profile
#source ~/.base_profile
#export KOBIS_KEY =...
targetDt = [20190113,20190106,20181230,20181223,20181216,20181209,20181202,20181125,20181118,20181111]

base_url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json'

movieCd=[] #대표코드
movieNm =[] #영화명 국문
audiAcc =[] #누적관객수



# Q1. 영화진흥위원회 오픈 API(주간/주말 박스오피스 데이터) 최근 10주간 데이터 중에 주간 박스오피스 TOP10데이터를 수집합니다.
#     해당 데이터는 향후 화평점서비스에 서 기본으로 제공되는 화 목록으로 사용될 예정입니다.
# 1. 주간(월~일)까지 기간의 데이터를 조회합니다. 
# 2. 조회 기간은 총 10주이며, 기준일(마지막 일자)은 2019년 1월 13일입니다. 
# 3. 다양성 화/상업 영화를 모두 포함하여야 합니다. 
# 4. 한국/외국 영화를 모두 포함하여야 합니다. 
# 5. 모든 상영지역을 포함하여야 합니다.
cnt = 0
res=''
taki = []
test = []

for i in range(10):
    cnt += 1
    url = base_url + f'?key={key}&targetDt={targetDt[i]}&weekGb=0'
    response = requests.get(url).json()
    print(f"#{cnt}")
    for j in range(10):
        movieNm.append(response['boxOfficeResult']['weeklyBoxOfficeList'][j]['movieNm'])
        movieCd.append(response['boxOfficeResult']['weeklyBoxOfficeList'][j]['movieCd'])
        audiAcc.append(response['boxOfficeResult']['weeklyBoxOfficeList'][j]['audiAcc'])
        if not movieNm[j] in test:
            test.append(movieNm[j])
            movie = {
                '대표코드 ': movieCd[j],
                '영화명 ': movieNm[j],
                '누적관객수 ': audiAcc[j],
                '날짜 ': targetDt[i]
            }   
            taki.append(movie)
    movieCd=[] #대표코드
    movieNm =[] #영화명
    audiAcc =[] #누적관객수
    print()


#### Q1.
with open('boxofficer.csv', 'w', encoding='utf-8', newline='') as f:
    fieldnames = ['대표코드 ','영화명 ','누적관객수 ','날짜 ']
    write = csv.DictWriter(f, fieldnames=fieldnames)
    write.writeheader()
    for l in taki:    #lunch를 리스트[] 내 딕셔너리로 만듬.
        write.writerow(l)



#### Q2. 
