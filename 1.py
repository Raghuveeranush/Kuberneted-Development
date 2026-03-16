#print("Hellp")

arn = "arn:aws:iam::123456789012:user/johndNodoe"

username = (arn.split("/")[1])

length = len(arn)
id = arn.split(":")[4]

#print(arn.split("::"))

new_text = arn.replace("john","Jaanav")
lower = arn.upper()
upper = arn.upper()
print("User details:")
print("username is:", username)
#print("Upper case of arn is:", lower)
print("Id of user:", id)
#print("Upeer case of arn is:", upper)
print("length of arn is:",length)
print("Modified text is", new_text)