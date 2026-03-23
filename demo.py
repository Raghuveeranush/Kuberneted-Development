
age = int(input("Enter your age: "))
#print(type(age))


phone_num = int(input("What is your phone number? "))

data_type = (type(phone_num))

#print("The data type of the phone number is: ", data_type)  

if (data_type == int) and (len(str(phone_num)) == 10):
    print("Phone number is valid.")
else:
    print("Phone number is not valid.")
