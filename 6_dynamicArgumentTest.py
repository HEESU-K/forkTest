def greeting(*name):
    print(name, "안녕하세요")

def info(weight, height, gender, **kwargs):
    print(weight, height, gender)
    print(kwargs)

##########################################

greeting("홍길동")
greeting("임꺽정")
greeting("신돌석")

greeting("신돌석", "홍길동")

greeting("홍길동", "임꺽정", "신돌석")

info(80, 180, '남자')
info(70, 170, '여자', age=20, addr="서울")