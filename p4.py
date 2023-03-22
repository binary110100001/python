import random

gnum= 0
com= random.randrange(3)
user= int(input('가위0 바위1 보2 선택: '))

if user == com:
    print('user= %d, com= %d' % (user, com))
    print('비겼습니다!')
    gnum += 1
elif (user == 0 and com == 2) or (user == 1 and com == 0) or (user == 2 and com == 1) :
    print('user= %d, com= %d' % (user, com))
    print('이겼습니다!')
    gnum += 1
elif (user == 0 and com == 1) or (user == 1 and com == 2) or (user == 2 and com == 0) :
    print('user= %d, com= %d' % (user, com))
    print('졌습니다!')
    gnum += 1
else:
    print("가위바위보를 "+gnum+" 번 했습니다.")