to_do_list =["Josh", "Kalu", "Emma"]
value = "doe"
print(value == to_do_list[0])
print(value==to_do_list[1])
print(value==to_do_list[2])

#or
to_do_list =["Josh", "Kalu", "Emma"]
value = "doe"
if value == to_do_list[0] :
    print("next")

else :
    print("error")
if value == to_do_list[1] :
    print ("next")

else :
    print("error")

if value == to_do_list[2] :
    print("next")

else :
    print("error")

#or
user_list=["josh", "Kalu", "Emma"]
value = "doe"
if value==user_list[0]:
    print("yes, index 0")
elif value==user_list[1]:
    print("yes, index 1")  
elif value==user_list[2]:
    print("yes, index 2")
else:
    print("no")

if value in user_list:
    print("yes")
else:
    print("no")  