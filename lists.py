my_list = [1 , 2.5, 'a']
print(my_list)

length = len(my_list)
print("The length of the list is: {}".format(length))

print("The contents of the list is:")
for item in my_list:
	print(item)

hello_list = list('hello')
print(hello_list)

my_sentence = "I am a lumberjack and I am OK. I sleep all night and I work all !"
print(my_sentence)

split = my_sentence.split()
print(split)

# split = '_'.join(split)
# print(split)

split = ' '.join(split)
print(split)