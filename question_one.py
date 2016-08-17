# Function takes input string
# and calculates frequency of each character
def run_length_encode(input):
	count_map = {}
	item_order = []
	for item in input:
		if(item in count_map):
			prev_count = count_map[item]
			count_map[item] = prev_count + 1
		else:
			item_order.append(item)
			count_map[item] = 1
	return count_map, item_order

# Print proper output
def print_output(count_map, item_order):
	for item in item_order:
		print(item,end="")
		print(count_map[item], end="")

if __name__ == '__main__':
	input = input()
	count_map, item_order = run_length_encode(input)
	print("input :", input)
	print("output : ", end="")
	print_output(count_map, item_order)