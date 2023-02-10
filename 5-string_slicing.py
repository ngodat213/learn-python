name = "Ngo Van Tien Dat"

first_name = name[:3]
last_name = name[3:]
step_name = name[::2]
reverse_name = name[::-1]

print("first_name= " + first_name + 
        ", last_name= " + last_name + 
        ", name_step= " + step_name + 
        ", reverse_name= " + reverse_name)

website1 = "https://google.com"
website2 = "https://facebook.com"
slice = slice(8,-4)
print(website1[slice])
print(website2[slice])