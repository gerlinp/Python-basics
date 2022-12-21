first_name = input("What is your first name?   ")

print("Hello", first_name)
if first_name == "Gerlin":
    print(first_name, "is learning python")
elif first_name == "Steven":
    print(first_name, "is learning with fellow students in the Community! Me too!")
else:
    #This is just in case we have a younger user who can't yet read
    age = int(input("How old are you?  "))
    if age <= 6:
        print("Wow if you're {}! If you're confident with your reading already...".format(age)) 
    print("You should totally learn Python, {}!".format(first_name))
print("Have a great day {}!".format(first_name))

