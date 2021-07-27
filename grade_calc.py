list1 = []


for i in range(0,3):
        name = input("이름: ")
        kor = int(input("국어점수 입력:"))
        eng = int(input("영어점수 입력:"))
        math = int(input("수학점수 입력:"))
        sum1 = kor + eng + math
        avg = (kor + eng + math) / 3
        list1.append([name, kor, eng, math, sum1, avg])
        

for i in range(0, 3):
    for k in range (0, 6):
        print(list1[i][k], end = " ")
    print("")


    


