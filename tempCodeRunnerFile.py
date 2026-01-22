import requests
from pprint import pprint as print

# 무작위 유저 정보 요청 경로
# API 요청

dummy_data = []
API_URL = lambda id: f'https://jsonplaceholder.typicode.com/users/{id}'

for id in range(10):
    response = requests.get(API_URL(id+1))
    parsed_data = response.json()
    dummy_data.append(parsed_data['name'])
# # 응답 데이터 출력
# print(response)

# # 변환 데이터 출력
# print(parsed_data)
# # 변환 데이터의 타입
# print(type(parsed_data))

# 특정 데이터 출력
# print(parsed_data['name'])


print (dummy_data)