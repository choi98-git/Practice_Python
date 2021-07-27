# 입력값의 각 자리의 숫자의 합을 리턴하는 함수
def sum(num):
    num1 = str(num)
    total = 0
    for i in range(len(num1)):
        total += int(num1[i])
    return total

while True:
    try:   
        num = int(input("정수를 입력하시오: "))
        print("각 자리수의 합: {}".format(sum(num)))
        
        # 입력값이 0일경우 종료
        if(num == 0):
            break
        
     # 입력값이 정수가 아닐경우    
    except ValueError:
            print("[Error]정수를 입력해주세요!!")     
            


