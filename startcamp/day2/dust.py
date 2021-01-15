import requests
from pprint import pprint

key='zGSv9n%2FXZeZOWVi9YNGptF6MTxFnYXH0VFPBtTG1NFYoITj%2BHLpjECdRv6Jkrsqpf%2Fp5%2Fc1j61Ci53mP0zxD2A%3D%3D'
return_type='json'
num_of_rows='5'
page_no='1'
sido_name='서울'
ver='1.0'
url = f'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={key}&returnType={return_type}&numOfRows={num_of_rows}&pageNo={page_no}&sidoName={sido_name}&ver={ver}'


response = requests.get(url).json()
pprint(response)



# stationname의 미세먼지 농도는 pm10value. 라는 메세지를 출력하시오

station_name1 = response['response']['body']['items'][0]['stationName']
pm_10value = response['response']['body']['items'][0]['pm10Value']

print(f'{station_name1}의 미세먼지 농도는 {pm_10value}입니다.')