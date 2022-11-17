import numpy as np
import matplotlib.pyplot as plt

##################################################

# 삼차방정식

dots = [[0, 0], [1, 1], [3, 5], [4,-2]] # 주어진 점들의 리스트(집합), 좌표는 바꿔도 좋으나, (소괄호)가 아닌 [대괄호]로 작성바란다.


def linear_equation(dots): # 계수함수: 주어진 점들의 리스트를 입력받아 일차함수의 계수를 리스트로 묶어 출력
    i = 0 # 반복문의 반복 횟수
    linear_list = []

    while i < len(dots) - 1: # 반복문
        a, b = dots[i] # n 번째 점의 좌표(a, b)
        c, d = dots[i+1] # n+1 번째 점의 좌표(c, d)

        p = (d-b)/(c-a) # 기울기
        q = -a*p + b # y 절편
        
        linear_list.append([p, q])
        i += 1

    return linear_list

linear_list = linear_equation(dots) # 계수함수 호출
print(linear_list) # 일차함수의 계수 리스트의 리스트

##################################################

# 그래프

def func(coef_list, x): # fn(x) = px + q, 계수와 x좌표를 받아 함숫값 출력
    return coef_list[0]*x + coef_list[1]

for i in range(len(dots)-1):
    x1, y1 = dots[i] # n 번째 점의 좌표
    x2, y2 = dots[i+1] # n+1 번째 점의 좌표
    x_ndarray = np.arange(x1, x2, 0.001) # 두 점 사이를 0.001 간격으로 쪼갬
    y_ndarray = func(linear_list[i], x_ndarray) # 쪼개진 x좌표의 함숫값
    plt.plot(x_ndarray, y_ndarray) # 그래프 출력
    plt.grid(color='0.8') # 각 일차함수를 색으로 구분

plt.show()