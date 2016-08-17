def find_string(input_string):
    alphabet = "zyxwvutsrqponmlkjihgfedcba"
    result = ""
    for char in alphabet:
        i = input_string.find(char)
        if i != -1:
            result = result + input_string[i]
            input_string = input_string[i:]
            continue
    return result
 
if __name__ == '__main__':
	N = int(input().rstrip("\n"))
	input = input().rstrip("\n")
	print(find_string(input))