# 성적 관리 프로그램

'''
score = int(input("점수를 입력해 주세요: "))

if score >= 90:
    print("A학점")

elif score >= 80:
    print("B학점")

elif score >= 70:
    print("C학점")

elif score >= 60:
    print("D학점")

else:
    print("F학점")
'''


# 1부터 n까지 합 구하기 프로그램

'''
n = int(input("n의 값: "))
total = 0

for i in range(0, n+1):
    total += i
print(total)
    
'''


# 구구단 출력 프로그램

'''
dan = int(input("단을 입력해 주세요: "))

for i in range(1,10):
    print("{} x {} = {}".format(dan,i,dan*i))
'''


# 동전교환기 프로그램
# 투입금액을 입력받는다
# 투입금액을 500원으로 몇개, 100원 몇개, 50원 몇개, 10원 몇개로 나누는지...
'''
money = int(input("투입 금액: "))

money_500 = int(money/500)
current_money = money%500

money_100 = int(current_money/100)
current_money %= 100

money_50 = int(current_money/50)
current_money %= 50

money_10 = int(current_money/10)
current_money %= 10

print("투입 금액: {} \n 500원 동전: {}개 \n 100원 동전: {}개 \n 50원 동전: {}개 \n 10원 동전: {}개 \n 나머지: {}원".format(money, money_500, money_100, money_50, money_10, current_money))

'''
# 별 그리기

i = 0

while i < 9:
    if i<5:
        k=0
        while k < 4-i:
            print('  ', end ='')
            k += 1
        k=0
        while k < i*2+1:
            print("\u2605", end = ' ')
            k += 1
    else:
        k=0
        while k < i-4:
            print('  ', end ='')
            k += 1
        k=0
        while k < (9-i)*2-1:
            print("\u2605", end = ' ')
            k += 1
    print()

    i += 1
    
