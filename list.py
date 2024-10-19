
# print("Range Function Output:",sample_list)


# While Loop 
# The loop will run until the undex reaches the list (len(data))
# print('Hema')
# print("Hema")

# Slicing - Breaking the String
# String  -> Sridhar  Sri   dhar
# Slicing Operator [start:stop]
# I want to get the Characters starting from S -> h (including)
name = "Sridhar"
# S -> 0
# r -> 1
# i -> 2
# d -> 3
# h -> 4
# print("Sliced Value:",name[0:5])
# Reversing 
# rahdirS
# print("Reverse:",name[::-1])


# Sridhar  -> S i h r
# print("Pattern 1:",name[::2])

#Pattern 2 -> dr 
# print("D R Output:",name[3::3])

#Pattern 2 -> r d a
# R -> 1
# d -> 2
# a -> 2
# print(" R D A Output:",name[1::2])

# Direction: Positive -> Forward 
# Negative -> Reverse 
# [start:stop:step]
# start not given -> default start index is 0 
# stop not given -> default stop index is len(list)
# step not given -> by fefault it is 1 
print("Sridhar")
# Print in Reverse Order 

# Pattern 3 - > r h i S
# print(name[::-1][::2])


# SalesData.csv (Use Split Method)
fileName = "SalesData.csv" #daily arriving file
fileName1 = "SalesData csv"
# I want to process only the file which meets the following condition 
    # 1. The File Name Should starts with Sales
    # 2. The File should be a type of CSV File 
 # Split Method -> Input ->   Split By .
# print(fileName.split("."))
# print(fileName1.split(" "))

# global file_validation 
# if "Sales"  in fileName.split(".")[0]:
#     if "csv" in fileName.split(".")[1]:
#         file_validation = True
#     else:
#         file_validation = False
# print("File Validation:",file_validation)
        
# Find whether the word Sales available or not 
# Find whether the word csv available or not 
# Set a variable called file_validation = True 
# If file_validation equals true print as  file arrived 
# print(fileName.split("."))
# print(fileName.split(".")[0])
# print(fileName.split(".")[1])

def file_validator(file_name):
    status = False
    if "Sales"  in file_name.split(".")[0]:
     if "csv" in file_name.split(".")[1]:
        status = True
    else:
        status = False
    return status

# print(file_validator(fileName))

# a = 100 

# print((a))

# List Comprehension 
sample_list = [1,2,3,4,5,6]
even_list_array = [ value * 2 if index %2 ==0 else value * index for index,value in enumerate(sample_list)]
# print("List Comprehension Type Output:",even_list_array)

# List Comprehension
# 1 For Loop  2 Condition Check 3 Value Assignment

# print(even_list_array)

# Using Range and Index
# Range Function accepts three parameters similar to slicing technique (start index, stop index, step)
for value in range(0, len(sample_list),2):
    sample_list[value] *=2


# Tuples 
# -> List is mutable (Modification allowed) [1,2,4,5,6]
# -> Tuple is immutable (No Modification allowed) sample_tuple = (1,2,3,4,5)

# Github 

# Dictionaries
# It is made up of Key Value Pairs.
# -> Key is used to identify the item and the value holds the value of the item.
# -> Key is unique and no duplication allowed in keys , but in values duplicates are allowed
# -> Dictionaries are created using {}
# "Hello How ara you ?"
# {
#    "message":"Hello How ara you ?"
# }
phase1_topic = {
   "Topic":"Python",
   "Day":"Thursday",
   "Month":10,
   "Year":2024,
   "Year":"2024"
}
print(type(phase1_topic))

# Find the keys in the dict 
# print(sample_dict.keys())
print(phase1_topic.values())
# print(type(sample_dict.items()))

# Update the value in dict
phase1_topic["Day"] = "Friday"
print("After Update:",phase1_topic)

# How to read the value from Dict 
print("Getting the year from the dict:",phase1_topic.get("Year"))

# Iterate the Dict -> Print all the Values for the key and if the Key is equal to Month then Update the Month as 09 -> Year 2023
phase2_topic = {
   "Topic":"Spark Programming",
   "Month":11,
   "Year":2024,
}

topics = []
topics.append(phase1_topic)
topics.append(phase2_topic)
# Iterate the list topics -> store the dict in a variable -> try to print all the values by using the keys 
# Topic
for topic in topics:   # 2 times
   if 'Day' in topic.keys():
    print("Topic:",phase1_topic['Day'])
   else:
      print("Topic is future")
#    for key in topic.keys(): # 1st Iteration phase1_Topics and its keys will be iterated here -> 2nd time phase2_topics
#       if 'Day' in key:  # phase1_topic['Day']
#         #  print(topic[key])
#     #   if 'Day' not in key:
#     #      print("Topic:",topic," is a future class")


# if 'Day' in phase1_topic.keys():
#    print("Topic:",phase1_topic['Day'])


# While Loop
# It will run till the condition is met

stop_execution = "False"

# We will get the input from Keyboard

while stop_execution.lower() != "true":  #Costliest loop 
   user_input = input("Enter the execution command:")
   print("user_input:",user_input)
   if user_input == "True":
    stop_execution = "True" 
    print("Loop Continues")
   
