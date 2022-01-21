#A B C D E 
#F G H I J 
#K L M N O 
#P Q R S T 
#U V W X Y

size = 5
count = 0

for i in range(size):
    for j in range(size):
        print(chr(65 + count), end=" ")
        count += 1
    print()