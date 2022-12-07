QUESTION = ["강아지 vs 고양이", "스핑크스 다리 갯수", "5+5=?"]
ANS = ["강아지", "4", "ㄹㅇㅋㅋ"]
ANS2 = ["Puppy", "Four", "10"]
for i in range(3):
    print(QUESTION[i])
    ans = input()
    if ans == ANS[i] or ans == ANS2[i]:
        print("정답입니다.")
    else:
        print("틀렸습니다.")
