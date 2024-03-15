str_1 = "abc"
str_2 = "xyz"

print(str_1.replace(str_1[:2], str_2[:2]))
print(str_2.replace(str_2[:2], str_1[:2]))
