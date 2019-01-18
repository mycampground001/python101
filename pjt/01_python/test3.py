import os
import requests
import csv
import pprint

movie =[] #영화명 국문
movieCd = [] #대표코드
with open('movier.csv','r', encoding='utf-8', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        movie.append(row['영화명(국문) '])
        movieCd.append(row['대표코드 '])

client_id = os.getenv('NAVER_KEY')
client_secret = os.getenv('NAVER_SECRET')
headers = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret }


base_url ="https://openapi.naver.com/v1/search/movie.json"


image = [] #이미지url
link = [] #하이퍼텍스트 링크
userRating = [] #유저 평점
ssafy =[]

for i in range(len(movie)):
    url = base_url + f'?query={movie[i]}'
    response = requests.get(url, headers=headers).json()

    image.append(response['items'][0]['image'])
    link.append(response['items'][0]['link'])
    userRating.append(response['items'][0]['userRating'])
    print(movie[i])
    naver = {
        '대표코드 ':movieCd[i],
        '이미지 URL ':image[-1],
        'link ':link[-1],
        '유저평점 ':userRating[-1] 
    }
    ssafy.append(naver)
    image=[]
    link=[]
    userRating=[]

with open('movier_naver.csv', 'w', encoding='utf-8', newline='') as f:
    fieldnames = ['대표코드 ','이미지 URL ','link ','유저평점 ']
    write = csv.DictWriter(f, fieldnames=fieldnames)
    write.writeheader()
    for l in ssafy:   
        write.writerow(l)



# {'display': 1,
#  'items': [{'actor': '유해진|윤계상|',
#             'director': '엄유나|',
#             'image': 'https://ssl.pstatic.net/imgmovie/mdi/mit110/1676/167699_P4
# 0_175859.jpg',
#             'link': 'https://movie.naver.com/movie/bi/mi/basic.nhn?code=167699',

#             'pubDate': '2018',
#             'subtitle': 'MAL·MO·E: The Secret Mission',
#             'title': '<b>말모이</b>',
#             'userRating': '9.04'}],
#  'lastBuildDate': 'Fri, 18 Jan 2019 16:23:49 +0900',
#  'start': 1,
#  'total': 1}

# 3. 네이버 화 검색 API
# 앞서 진위에서 얻은 화명(국문)을 바탕으로 네이버 화 검색 API를 통해 추가적인 데이터를 수집합니다. 
# 해 당 데이터는 향후 화평점서비스에서 기준 평점 및 화 포스터 썸네일로 활용될 것입니다.
# 요청 화명을 통해 요청합니다. 응답 화별로 다음과 같은 내용을 저장합니다. 진위 화 대표코드, 
# 화 썸네일 이미지의 URL, 하 이퍼텍스트 link, 유저 평점 해당 결과를 movie_naver.csv에 저장합니다.