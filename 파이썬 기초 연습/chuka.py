#chuka.py
jumsus = [24, 88, 12, 64, 66]
number = 0
for i in jumsus:
    number = number + 1
    if i >= 60:
        print("%d번 축하합니다! %d 점으로 패스하셨습니다" % (number, i))
    else: continue
