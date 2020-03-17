def monitor(data):
	try:
		if len(data)!=3:
			print("wrong input length")
		else:
			output_type = ["Pulse", "BP", "OL"]
			for i in range(0,3):
				if str(data[output_type[i]]).isdigit():
					print(output_type[i] + ": " + str(data[output_type[i]]))
				else:
					print(output_type[i] + " has wrong input type")
					break

			print()
	except:
		print("input is not array")


# test cases:
# a = { "Pulse" : 12,  "BP" : 120, "OL" : 340}
# monitor(a)