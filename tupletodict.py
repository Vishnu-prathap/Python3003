def convert_to_dict(tuple_list):
	dictionary = dict((key, value) for key, value in tuple_list)
	return dictionary


tuple_list = [("akash", 10), ("gaurav", 12), ("anand", 14),
			("suraj", 20), ("akhil", 25), ("ashish", 30)]

print(convert_to_dict(tuple_list))
