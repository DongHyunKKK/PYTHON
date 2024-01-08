# -----------------------------------------------------------
#
# -----------------------------------------------------------
def print_hello():
    hello = 'Hello~!'

    def print_message():
        msg = hello + '^^'
        print(msg)

    print_message()

def ff():
    x = 100
    def a():
        x = 10  # 함수 a의 지역변수 x

        def b():
            nonlocal x  # 가장 가까운 바깥 함수에서 변수 x를 찾음
            x = 20  # 함수 b의 지역변수 x

        # 호출
        b()
        print(x)

# 함수 호출
ff()



def foo():
    x = 10
    def test():
        return x

    return test

x = foo()
print(x(), x)