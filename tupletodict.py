def convert_to_dict(tuple_list):
	dictionary = {}
	for tuple in tuple_list:
		if tuple[0] in dictionary:
			dictionary[tuple[0]].append(tuple[1])
		else:
			dictionary[tuple[0]] = [tuple[1]]
	return dictionary



tuple_list = [("akash", 10), ("gaurav", 12), ("anand", 14),
			("suraj", 20), ("akhil", 25), ("ashish", 30)]

print(convert_to_dict(tuple_list))
