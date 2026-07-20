# name = '''Mynameisjagrati,I am data engineer
# '''
# print(name[0])
# print(name[1])
# print(name[2])

# name = "Jagrati"
# print(name[0:2]) #0 to 2-1 which is 0 to 1
# print(name[3:-2])
# print(name[0:7:2])

# name="jagrati mathe"
# print(len(name))
# print(name.upper(), name)
# print(name.capitalize(), name)

template="Hey {} you are great, please take {}$"
user1="jack"
price1=1000

user2="ria"
price2=3000

user3="jagrati"
price3=50000

s1=template.format(user3,price3)
print(s1)

#or

print(f"Hey {user2} you are great, please take {price2}$")