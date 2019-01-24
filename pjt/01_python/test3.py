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
