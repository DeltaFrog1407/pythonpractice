# adddata .py
f = open("C:\doit\새파일.txt", 'a')
for i in range(11,20):
    data = "%d 번째 줄입니다.\n" % i
    f.write(data)
f.close()
