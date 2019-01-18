import requests

for i in range(5):
    url = f"https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={837+i}" #들어가면됨. 이것이 json 파일
    response = requests.get(url).json()
    for j in range(1,7):
        print(response[f'drwtNo{j}'],end = ' ')
    print()