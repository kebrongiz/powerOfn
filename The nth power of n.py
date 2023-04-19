def nth_power_of_n(num):
    return num.__pow__(num)
num= int(input("Enter the number:"))
print("The {}th power of {} is: {}".format(num, num, nth_power_of_n(num)))