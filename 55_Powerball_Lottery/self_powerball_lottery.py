import random

# input a tuple with spaces between
input_num = input("enter 5 different num from 1 to 69" + "\n" + ">")
list_num = input_num.split(" ")

compare_num = []
for i in list_num:
    if i.isdecimal() and int(i) > 1 and int(i) < 69:
        compare_num.append(int(i))
    else:
        print("Please input number from 1 to 69")



# input a powerball num from 1 to 26
powerball = input("enter powerball num from 1 to 26" + "\n" + ">")
if powerball.isdecimal():
    powerball = int(powerball)


# input times,max 1000000
input_times = input("enter times and max is 1000000" + "\n" + ">")
if input_times.isdecimal() and int(input_times) >=1 and int(input_times) <=1000000:
    input_times = int(input_times)

# print costs for times,one times is $2
print("one times is $2")
print(f"you will cost ${input_times * 2}")

# compare tuple with random tuple
for times in range(input_times):
    loop = 0
    index = 0
    equal_num = 0
    noEqual_num = 0
    random_list = []
    while True:
        random_list.append(random.randint(1,70))
        if compare_num[index] == random_list[index] and powerball == random.randint(1,27):
            equal_num += 1
            index += 1
        else:
            noEqual_num += 1

        loop += 1
        if loop == 5 :
            if equal_num == 6:
                print("you win")
            else:
                print(f"The winning numbers are: "
                      f"{random_list[0]} {random_list[1]} {random_list[2]} {random_list[3]} {random_list[4]}" + " "
                      f"you lose")

            break





