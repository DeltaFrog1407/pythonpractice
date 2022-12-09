import sys
print(sys.argv)
a = sys.argv[1:]
result = 0
for i in a:
    result += int(i)
print(result) 
