# print the horizontal number labels:
print('  |  0   1   2   3   4   5   6   7   8   9  10  11  12')
print('--+---------------------------------------------------')

# display each row of products
for num1 in range(0,13):

    # print the vertical numbers labels
    print(str(num1).rjust(2),end="")

    # print a separate bar
    print('|',end="")

    for num2 in range(0,13):
        # print the product followed by a space
        print(str(num1 * num2).rjust(3),end=" ")
    print()

for i in range(1,10):
    for j in range(1,10):
        sum = i * j
        print(str(sum).rjust(4),end=" ")
    print()

for i in range(1,10):
    for j in range(1,i+1):
        sum = i * j
        print(f"{i} * {j} = {sum}",end=" " * 3)
    print()

