def line(cnt, style='*'):
    for i in range(cnt):
        print(style, end="")
    print()
    
#################################################

line()
print("          고객관리 프로그램           ")
line(20, "-")
print("1. 리스트 출력")
print("2. 고객 추가")
print("3. 종료")
line(30, "=")