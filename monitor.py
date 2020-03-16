def monitor(data):
	try:
		if len(data)!=3:
			print("wrong input length")
		else:
			output_type = ["Pulse", "Blood Pressure", "Oxygen Level"]
			for i in range(0,3):
				if str(data[i]).isdigit():
					print(output_type[i] + ": " + str(data[i]))
				else:
					print(output_type[i] + " has wrong input type")
					break

			print()
	except:
		print("input is not array")


# test cases:
# monitor([23, 4, 5])
# monitor([3])
# monitor([12, "ff", 3])