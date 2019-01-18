# 4. 화 포스터 이미지 저장
# 앞서 네이버 화 검색 API를 통해 얻은 
# 이미지 URL에 요청을 보내 실제 이미지 파일로 저장합니다. 
# 해당 데이 터는 향후 화 목록에서 포스터 이미지로 사용될 것입니다. 
# 요청 이미지 URL 응답 응답받은 결과를 파일로 저장합니다. 
# 저장시 반드시 wb 옵션으로 저장하시기 바랍니다. 
# 저장되는 파일명은 images 폴더 내에 영진위 영화 대표코드.jpg 입니다

import csv
import requests
import os

image = []
movieCd =[]

with open('movier_naver.csv','r', encoding='utf-8', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        image.append(row['이미지 URL '])
        movieCd.append(row['대표코드 '])

for i in range(len(movieCd)):
    with open(f'{movieCd[i]}.jpg','wb') as g:
        imagin = requests.get(image[i]).content
        g.write(imagin)

# for i in range(len(info)):
#     fname = info[i]['영화코드']
#     with open(f'{fname}.jpg','wb') as g:
#         image = requests.get(naver_info[i]['이미지 url ']).content
#         g.write(image)
