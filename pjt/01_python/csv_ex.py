import csv
lunch = [
    {
        'store':'맘터',
        'menu':'사이버거'
    },
    {
        'store':'노은각',
        'menu':'잠자면'
    }
]
lunch2 = {
    '맘터':'사이',
    '노은':'짬자',
    '노we':'erw자',
}
with open('lunch4.csv', 'w', encoding='utf-8', newline='') as f:
    write = csv.writer(f)
    write.writerow(('가게','메뉴'))
    for item in lunch2.items():
        write.writerow(item)

# with open('lunch.csv','w',encoding='utf-8') as f:
#     for key, value in lunch.items():
#         f.write(f'{key}, {value}\n')

# with open('lunch2.csv','w',encoding='utf-8', newline='') as f:
#     fieldnames = ['store','menu']
#     write = csv.DictWriter(f, fieldnames=fieldnames)
#     write.writeheader()
#     write.writerow({'menu':'잠자면','store':'노으안'})

with open('lunch3.csv','w',encoding='utf-8', newline='') as f:
    fieldnames = ['store','menu']
    write = csv.DictWriter(f, fieldnames=fieldnames)
    write.writeheader()
    for l in lunch:    #lunch를 리스트[] 내 딕셔너리로 만듬.
        write.writerow(l)

with open('lunch4.csv','r', encoding='utf-8', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row['가게'], row['메뉴'])
