import random


# 1. 1~45까지의 수
numbers = range(1,46)
print(numbers)
#2. 6개를 무작위로 추첨
pick = random.sample(numbers,6)
pick.sort()
print(pick)



#string-interpolation (보간법)
#f-string
print(f'1.오늘의 로또 번호는 {pick} 입니다.')
#print('오늘의 로또 번호는 %f 입니다.' %(pick))
#print('오늘의 로또 번호는 {0}입니다.'.format {pick})

datetime 모듈 서버의 날짜, 시간 추출

