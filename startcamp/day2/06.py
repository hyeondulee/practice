# 함수
# 특정 역할을 하는 코드의 집합
# 하나의 함수는 하나의 역할만 해야 한다. 


# 함수 정의
def mul(a, b):
    result = a+b
#   print(result)
    return result
# 함수는 반환값이 있어야 하며, 이게(return) 없으면 NONE임


#def mul(a, b):
#    result = a+b
#    #return result
#    print(result)
# 이렇게 하면 null 나옴! (result를 안했으니까), 또한 return 다음 값은 작동하지 않음.

# 함수 호출( 함수를 할당하는거지 출력하는게 아님. 만약 print(result)가 있었다면 출력이 됐을 것)
result = mul(1, 2)
print( result)

# ( 미니 실습 ) 주어진 양수 n
print(help(len))
