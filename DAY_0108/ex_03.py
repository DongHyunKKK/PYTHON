# -----------------------------------------------------------
# 지역 변수 & 전역 변수
# -----------------------------------------------------------
def foo():
    global x
    x = 20
    print(x)
    print(locals())

# 전역 변수
x = 10

# 함수 호출
foo()
print(x)

print(locals())