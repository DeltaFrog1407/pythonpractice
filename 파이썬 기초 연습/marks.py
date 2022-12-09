#makrs.py
marks = [90, 25, 67, 45, 80]
for number in range(len(marks)):
    if marks[number]>=60:
        print("축하합니다 %d번 학생 %d점으로 합격입니다." % (number+1, marks[number]))
    else: continue
