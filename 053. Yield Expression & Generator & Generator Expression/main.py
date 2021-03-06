# Generator는 iterator의 일종인 generator iterator를 반환하는 함수를 의미한다
# yield 표현식을 포함하고, next() 함수로 한 번에 하나씩 요소에 접근할 수 있다는 점만 제외하면 일반적인 함수와 동일하다
def gen(n):
    for i in range(n):
        yield i

# 일반적인 함수는 return문을 포함하여, 해당 값이 반환된 후 함수가 종료되고 메모리에서 제거되나
# 함수에서 yield expression을 만나면, 그 상태로 호출자에게 제어를 넘기며 next()가 호출될 때까지 정지
# 따라서 next()를 통해 yield 구문을 실행시킬 수 있어 원하는 시점에 데이터를 받을 수 있음
g = gen(5)

print(type(g))
# <class 'generator'>
print(next(g))
# 0
print(next(g))
# 1
print(next(g))
# 2
print(next(g))
# 3
print(next(g))
# 4
print(next(g))
# StopIteration
# 일반적인 iterator와 동일하게, 더이상 접근할 요소가 없으면 StopIteration이 발생한다
# 이처럼 yield에서 함수의 실행이 멈추고, next를 호출할 때마다 다시 해당 라인으로 진입한다. 이를 코루틴, 진입점이 여러 개인 함수라고 한다
# 순서대로 쭉 내려오다 return을 만나고 결과를 리턴하는 '함수'는 서브루틴(subroutine)이라고 한다

# 위와 같이 함수 형태의 generator를 정의할 수도 있고, 아래처럼 Python에서 지원하는 generator expression을 사용할 수도 있다
g = (i for i in range(5))
# 소괄호를 사용한다는 점만 다르고, List Comprehension과 동일
print(next(g))
# 0
print(next(g))
# 1
