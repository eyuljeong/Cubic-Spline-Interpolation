import numpy as np
import matplotlib.pyplot as plt

##################################################

# 삼차방정식

dots = [[0, 0], [1, 1], [2, 8]] # 주어진 점들의 리스트(집합)

condition = [0, 0] # 선택조건: 첫번째 점(a, b) 에서 [f'(a), f"(a)]


def cubic_equation(dots, condition): # 계수함수: 주어진 점들의 리스트와 선택조건을 받아 각 삼차함수의 계수를 리스트로 묶어 출력
    i = 0 # 반복문의 반복 횟수
    cubic_list = []

    while i < len(dots) - 1: # 반복문
        a, b = dots[i] # n번째 점의 좌표(a, b)
        c, d = dots[i+1] # n+1번째 점의 좌표(c, d)

        if  i==0: # i=0 일 때
            e = condition[0] # 첫번째 점의 미분계수
            f = condition[1] # 첫번째 점의 이계미분계수
        elif i!=0: # i≠0 일 때
            x = dots[i][0]
            e = 3*p*x**2 + 2*q*x + r # n번째 점의 미분계수
            f = 6*p*x + 2*q # n번째 점의 이계미분계수

        # fn(x) = px^3 + qx^2 + rx + s
        p = (f*(a-c)**2 - 2*e*(a-c) + 2*(b-d))/ 2*(a-c)**3
        q = f/2 - 3*a*p
        r = e - 3*a**2*p - 2*a*q
        s = b - p*a**3 - q*a**2 - r*a

        cubic_list.append([p, q, r, s])
        i += 1

    return cubic_list

cubic_list = cubic_equation(dots, condition) # 계수함수 호출
print(cubic_list) # 각 삼차함수의 계수 리스트의 리스트

##################################################

# 그래프

def func(coef_list, x): # fn(x) = px^3 + qx^2 + rx + s, 계수와 x좌표를 받아 함숫값 출력
    return coef_list[0]*x**3 + coef_list[1]*x**2 + coef_list[2]*x + coef_list[3]

for i in range(len(dots)-1):
    x1, y1 = dots[i] # n번째 점의 좌표
    x2, y2 = dots[i+1] # n+1번째 점의 좌표
    x_ndarray = np.arange(x1, x2, 0.001) # 두 점 사이를 0.001 간격으로 쪼갬
    y_ndarray = func(cubic_list[i], x_ndarray) # 쪼개진 x좌표의 함숫값
    plt.plot(x_ndarray, y_ndarray) # 그래프 출력
    plt.grid(color='0.8') # 각 삼차함수를 색으로 구분

plt.show()