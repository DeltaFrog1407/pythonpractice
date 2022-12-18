file = open('test2.txt', 'rt', encoding='UTF8')
rl = file.readlines()
file.close()
for i in rl:
    print(i.rstrip("\n"))
