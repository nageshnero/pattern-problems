#print
#    1
#   123
#  12345
# 1234567
#123456789

n = 5
for i in range(n):
    for j in range(n - i - 1):
        print(' ', end='')
    for k in range(2 * i + 1):
        print(k + 1, end='')
    print()