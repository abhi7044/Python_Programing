#1 write a python program to display a user intered naem followed by 
name = input("Enter your naem: ")
print(f"Good afternoon {name} ")

#2 write a program to fill in a letter template given below with name and date
letter = '''Dear <|Name|>,
you are selexted!
    <|Date|>'''
print(letter.replace("<|Name|>", "abhijeet").replace("<|Date|>", "24 september 2050"))  # chaining in this problem

#3 double space in string
name = "i am  good"
# print(name.find("  "))
print(name.replace("  "," "))