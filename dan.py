# 구구단의 단을 입력받고 그의 맞는 구구단을 출력하는 알고리즘
dan = int(input("단을 입력하시오: "))

for i in range(1,10):
    print("{} * {} = {}".format(dan, i, dan*i))
