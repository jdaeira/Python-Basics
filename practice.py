import random

def add_list(add):
	total = 0
	for items in add:
		total += items
	return total


def summarize(add):
	sum = 0
	for items in add:
		sum += items
	return "The sum of {} is {}".format(add, sum)

numbers = list([1, 2, 3])
total = add_list(numbers)
sum = summarize(numbers)

print(total)
print(sum)

random = random.randint(1,10)
print(random)