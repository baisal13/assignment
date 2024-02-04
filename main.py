#Question 1
# myfamily = ("mother", "father", "sister", "brother", "sister") 
#1)print(type(myfamily))
#2)print(myfamily[-1])
#3)we can`t use append() in tuple, but we can turn the tuple into a list and only then we can add elements
#myfamily = ("mother", "father", "sister", "brother", "sister")
#y = list(myfamily)
#y.append("me")
#myfamily= tuple(y)
#print(myfamily)
#4)we can`t use pop() in tuple, but we can turn the tuple into a list and only then we can remove elements
#myfamily = ("mother", "father", "sister", "brother", "sister")
#myfamily_list = list(myfamily)
#myfamily_list.pop(3)
#print(myfamily_list)
#Question 2
#laptop = { "brand": "dell", "model": "alienware", "year": 2010 }
#1)print(laptop['brand'])
#2)laptop["home"] = True
#print(laptop)
#laptop["year"] = 2019
#print(laptop)
#Question 3
# Create an empty dictionary to store user information
user_info = {}

# Prompt the user for their name and store it in the dictionary
user_info['name'] = input("What is the user's name? ")

# Prompt the user for their age and store it in the dictionary
user_info['age'] = input("What is the user's age? ")

# Prompt the user for their country of birth and store it in the dictionary
user_info['country_of_birth'] = input("What is the user's country of birth? ")

# Prompt the user for what they are known for and store it in the dictionary
user_info['known_for'] = input("What is the user known for? ")

# Display the user information stored in the dictionary
print("\nUser Information:")
for key, value in user_info.items():
    print(f"{key.capitalize()}: {value}")
