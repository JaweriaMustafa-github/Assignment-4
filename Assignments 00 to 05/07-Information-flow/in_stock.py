def num_in_stock(fruit):
	"""
	This function returns the number of fruit Sophia has in stock.
	"""
	if fruit == 'apple':
		return 24
	if fruit == 'mango':
		return 78
	if fruit == 'pear':
		return 1000
	else:
		# this fruit is not in stock.
		return 0

def main():
    fruit : str = input("Enter a fruit: ")
    stock = num_in_stock(fruit)
    if stock == 0:
        print("This fruit is not in stock!")

    else:
        "This fruit is in stock! Here is how many : "
        print(stock)
		
if __name__ == '__main__':
	main()