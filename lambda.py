list_num = [1,2,3,4,5,6]
even_num = filter(lambda x:(x%2==0),list_num)
# print(list(even_num))
even_num = list(filter(lambda x:(x%2==0),list_num))
print(list(even_num))