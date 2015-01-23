full_name = "John da Eira"
print(full_name)

name_list = full_name.split()
print(name_list)

greeting_list = "Hi, I'm Treehouse".split()
print(greeting_list)

greeting_list[2] = name_list[0]
print(greeting_list)
print(' '.join(greeting_list))

