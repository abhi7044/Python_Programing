# Ques 1: find the greatest of 4 number enter by the user
# a1 = int(input("Enter the number 1: "))
# a2 = int(input("Enter the number 2: "))
# a3 = int(input("Enter the number 3: "))
# a4 = int(input("Enter the number 4: "))

# if(a1>a2 and a1>a3 and a1>a4):
#     print("Greater number is a1: ", a1)
# elif(a2>a1 and a2>a3 and a2>a4):
#     print("Greater number is a2: ", a2)
# elif(a3>a1 and a3>a2 and a3>a4):
#     print("Greater number is a3: ", a3)
# else:
#     print("Greater number is a4: ", a4)

# Ques 2: WAP to find whether a srudent has passed or failed if it requires a toral of 40% and at least 33% in each subject to pass. Assume 3 subject and take marks as an input from users
# s1 = int(input("Enter marks 1: "))
# s2 = int(input("Enter marks 2: "))
# s3 = int(input("Enter marks 3: "))

# total_percentage = (100*(s1 + s2 + s3))/300
# if(total_percentage >= 40 and s1 >= 33 and s2 >= 33 and s3 >= 33):
#     print("You are passed:", total_percentage)

# else:
#     print("You failed , try again next year:", total_percentage)

# Ques 3: Spam problem 

# p1 = "Make a lot of Money"
# p2 = "buy now"
# p3 = "subscribe this"
# p4 = "Click this"

# message = input("Enter your comment: ")
# if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message));
#     print("This comment is a spam")\
    
# else:
#     print("This comment is not spam")

# Ques 4: WAP to find character less than 10 which would be freater than 10

# username = input("Enter username")
# if(len(username) < 10):
#     print("Your username contains less than 10 characterss")
# else:
#     print("Your username contains more than or equal to 10 characters")

# Ques 5: WAP to find out wether the given post is ttalking about "Harry" or not

post = input("Enter the post:")

if("Abhijeet".lower() in post.lower()):
    print("This post is talking aboiut abhijeet")

else:
    print("This post is not talking about Abhijeet")