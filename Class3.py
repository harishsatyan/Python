# SalesData.csv (Use Split Method)
# Find whether the word Sales available or not 
# Find whether the word csv available or not 
# Set a variable called file_validation = True 
# If file_validation equals true print as  file arrived

""" filename = "SalesData.csv"

split_value = filename.split(".")
file_validation = False
if "Sales" in split_value[0] and "csv" in  split_value[1]:
    file_validation = True
    print("File arrived")
else:
    print("Doesn't exist")
 """

my_array = [1,2,3,4,5,6,7,8]
my_array = [x + 1 if i % 2 == 0 else x for i, x in enumerate(my_array)]
# for index,value in enumerate(my_array):
#     if index/2==0:
#         my_array[index]=value+1

# print(my_array)

phase1_topic = {
   "Topic":"Python",
   "Day":"Thursday",
   "Month":10,
   "Year":2024,
   "Year":"2024"
}

phase2_topic = {
   "Topic":"Spark Programming",
   "Month":11,
   "Year":2024,
}

topics = []
topics.append(phase1_topic)
topics.append(phase2_topic)
# Iterate the Dict -> Print all the Values for the key and if the Key is equal to Month then Update the Month as 09 -> Year 2023
# my_dict = [phase2_topic['Month']=9 if 'Month' in i.keys() else x for i, x in enumerate(topics)]
# print(my_dict)
for iter in topics:
    # print(iter)
    if 'Month' in iter.keys():
        #  print(iter.values)    
         iter.update([('Month',9)])
    if 'Year' in iter.keys():
        #  print(iter.values)    
         iter.update([('Year',2023)])
    # if 'Year' in iter.keys():
    #     iter.values=2023
print(topics)
# my_dict = [i.update([('Month',9)]) if 'Month' in i.keys() else i for i in enumerate(topics)]
# print(my_dict)
# for index,value in enumerate(my_array):
#     if index/2==0:
#         my_array[index]=value+1

