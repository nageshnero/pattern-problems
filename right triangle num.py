#    1 #print
#   12
#  123
# 1234
#12345


n = 5
for i in range(n):
    for j in range(1, n - i):
        print(" ", end="")
    for k in range(1, i + 2):
        print(k, end='')
    print()