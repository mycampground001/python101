import os
import requests
import csv

key = os.getenv('KOBIS_KEY')

targetDt = [20190113,20190106,20181230,20181223,20181216,20181209,20181202,20181125,20181118,20181111]

base_url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json'

movieCd=[] #대표코드
movieNm =[] #영화명 국문
audiAcc =[] #누적관객수

cnt = 0
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
    for l in taki:
        write.writerow(l)
