Str_eg = "DataEngineering"
print(Str_eg)
print(Str_eg[:5])
print(Str_eg[-3:])
print(Str_eg[::-1])
programming_languages = ["Python", "Swift","Java", "C++", "Go", "Rust"]
Lower_conv = [x.lower() for x in programming_languages]
print(Lower_conv)
Upper_conv = [x.upper() for x in programming_languages]
print(Upper_conv)
str_rep = Str_eg.replace('Data','File')
print(str_rep)
str_list = ['Apple','Banana','Orange','PineApple','JackFruit']
str_val=''
for str in str_list:
    str_val += str + " "
print(str_val)
str_val = ' '.join(str_list)
print(str_val)


