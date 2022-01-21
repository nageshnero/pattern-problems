#123456789
#1234567
# 12345
#  123
#   1

n = 5
for i in range(n): 
    for j in range(i):
        print(' ', end='')
    for j in range(2*(n-i)-1):
        print(j+1, end='')
    print()