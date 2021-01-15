# Dictionary (딕셔너리)
# 얘내는 순서가 없는 데이터 타입임.
my_home={
    'location' : 'seoul' ,
    'area-code' : '02'
}
# 딕셔너리 원소 접5근
# 1번 방식
print(my_home['location'])
#print(my_home['name'])
# key error 이 나옴.
# i.e 키가 없거나, 잘못썻거나!

# 2번 방식
print(my_home.get('location'))
print(my_home.get('name'))
#None에 대한 정보를 줌 ( 실행은 가능 ) --> name을 가진 value 값은 없다 라는 것을 알려줌

# [] --> 리스트 , {} --> 딕셔너리