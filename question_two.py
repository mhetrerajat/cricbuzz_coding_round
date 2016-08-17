import string
import json


# Function to load data from json file
# returns booking chart and prev_booking position
def load_booking_chart():
	in_file = open("booking_data.json", "r")
	data = json.load(in_file)
	in_file.close()
	return data.get('booking_chart'), data.get('prev_booking')


# Function to save data into file
def save_file(booking_chart, prev_booking):
	op_file = open("booking_data.json", 'w')
	data = {
		'prev_booking' : prev_booking,
		'booking_chart' : booking_chart
	}
	json.dump(data, op_file)
	op_file.close()
	
# Function to generate empty booking chart
def generate_booking_char():
	row_lable = list(string.ascii_uppercase)
	booking_chart = {}
	prev_booking = None
	for item in row_lable:
		booking_chart[item] = [0]*40
	return booking_chart, prev_booking


# Function to book ticket
def book_ticket(count, booking_chart, prev_booking):
		# Check if prev booking is present or not
		# if not then, start with A0 booking
		if prev_booking:
			# Get prev booking number i.e if prev_booking is A10 then
			# prev_booking_number is 10
			prev_booking_number = int(prev_booking[1:])
			# check if total extends 40(limit)
			# if yes then break into parts
			if(prev_booking_number + count > 40):
				first_part_booking_number = 40 - prev_booking_number
				
				# book into prev_booking row till possible
				# once 40 limit reached then simply jumps to next row
				booking_row = booking_chart.get(prev_booking[:1])

				# book into prev_booking row as much as possible i.e. till 40
				for i in range(prev_booking_number+1, 40):
					booking_row[i] = 1
				booking_chart.update({ prev_booking[:1] : booking_row })
				prev_booking = ''.join([prev_booking[:1], str(prev_booking_number+count-1)])
				
				# Get new row id
				# i.e if prev_booking row is 'A' then next one will be 'B'
				row_lable = list(string.ascii_uppercase)
				row_label_position = row_lable.index(prev_booking[:1])
				# Check if bookings are full
				# i.e prev_row is 'Z'
				if(row_label_position + 1 > 25):
					# booking full
					print("Booking full.")
				else:
					# if not full then, book as much as possible
					# update booking_chart and prev_booking accordingly.
					new_row_label = row_lable[row_label_position+1]
					remaining_count = count - first_part_booking_number
					booking_row = booking_chart.get(new_row_label)
					for i in range(remaining_count):
						booking_row[i] = 1
					booking_chart.update({ new_row_label : booking_row })
					prev_booking = ''.join([new_row_label, str(remaining_count-1)])


			else:
				booking_row = booking_chart.get(prev_booking[:1])
				for i in range(prev_booking_number+1, count):
					booking_row[i] = 1
				booking_chart.update({ prev_booking[:1] : booking_row })
				prev_booking = ''.join([prev_booking[:1], str(prev_booking_number+count-1)])
		else:
			# Start from first i.e. A0
			booking_row = booking_chart.get("A")
			for i in range(count):
				booking_row[i] = 1
			booking_chart.update({ 'A' : booking_row })
			prev_booking = ''.join(['A', str(count-1)])
		return booking_chart, prev_booking



if __name__ == '__main__':
	EXIT_STATUS = False # Set to True, when user want to exit
	while not EXIT_STATUS:
			try:
				# Load data from file
				booking_chart, prev_booking = load_booking_chart()
			except Exception as e:
				# If file don't exists then, generate empty booking chart.
				booking_chart, prev_booking = generate_booking_char()

			control_query = int(input("1) Book Ticket  2) Exit \n"))
			if control_query == 2:
				EXIT_STATUS = True
			elif control_query == 1:
				booking_quantity = int(input())
				booking_chart, prev_booking = book_ticket(booking_quantity, booking_chart, prev_booking)
				save_file(booking_chart, prev_booking)
			else:
				print("Please provide valid number. [1 or 2] \n")

	