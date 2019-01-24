import os
import requests
import csv

key = os.getenv('KOBIS_KEY')
# http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key=430156241533f1d058c603178cc3ca0e&movieCd=20124079

base_url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json'

movieCd=[] #대표코드
movieNm =[] #영화명 국문
movieNmEn =[] #영화명 영문
movieNmOg = [] #영화명 원문
openDt = [] #개봉연도
showTm = [] #상영시간
genreNm = [] #장르명
peopleNm = [] #감독명
watchGradeNm = [] #관람등급 명칭
staffs = [] #배우 최대 3명까지
actor =[]

star = ''
taki = []

with open('boxofficer.csv','r', encoding='utf-8', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        movieCd.append(int(row['대표코드 ']))

for i in range(len(movieCd)):
    url = base_url + f'?key={key}&movieCd={movieCd[i]}'
    response = requests.get(url).json()

    movieNm.append(response['movieInfoResult']['movieInfo']['movieNm'])
    movieNmEn.append(response['movieInfoResult']['movieInfo']['movieNmEn'])
    movieNmOg.append(response['movieInfoResult']['movieInfo']['movieNmOg'])
    openDt.append(response['movieInfoResult']['movieInfo']['openDt'])
    showTm.append(response['movieInfoResult']['movieInfo']['showTm'])
    genreNm.append(response['movieInfoResult']['movieInfo']['genres'][0]['genreNm'])
    peopleNm.append(response['movieInfoResult']['movieInfo']['directors'][0]['peopleNm'])
    watchGradeNm.append(response['movieInfoResult']['movieInfo']['audits'][0]['watchGradeNm'])

    for j in range(len(response['movieInfoResult']['movieInfo']['actors'])):
        if len(response['movieInfoResult']['movieInfo']['actors'])<=3:
            staffs.append(response['movieInfoResult']['movieInfo']['actors'][j]['peopleNm'])
        else:
            if j>=3:
                break
            staffs.append(response['movieInfoResult']['movieInfo']['actors'][j]['peopleNm'])
            
    star = ', '.join(staffs)
    print(star)

    movie = {
        '대표코드 ': movieCd[i],
        '영화명(국문) ': movieNm[-1],
        '영화명(영문) ': movieNmEn[-1],
        '영화명(원문) ': movieNmOg[-1],
        '개봉연도 ': openDt[-1],
        '상영시간 ': showTm[-1],
        '장르 ': genreNm[-1],
        '감독 명': peopleNm[-1],
        '관람등급 ': watchGradeNm[-1],
        '배우 ': star

    }
    taki.append(movie)
    movieNm=[]
    movieNmEn =[]
    movieNmOg =[]
    openDt =[]
    showTm =[]
    genreNm =[]
    peopleNm = []
    watchGradeNm =[]
    staffs= [] 

#### Q2.
with open('movier.csv', 'w', encoding='utf-8', newline='') as f:
    fieldnames = ['대표코드 ','영화명(국문) ','영화명(영문) ','영화명(원문) ','개봉연도 ','상영시간 ','장르 ','감독 명','관람등급 ','배우 ']
    write = csv.DictWriter(f, fieldnames=fieldnames)
    write.writeheader()
    for l in taki:
        write.writerow(l)