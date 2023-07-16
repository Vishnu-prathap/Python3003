tups = [("akash", 10), ("gaurav", 12), ("anand", 14),
		("suraj", 20), ("akhil", 25), ("ashish", 30)]
def tupletodict(tups):
  dictionary = {}
  for key, val in tups:
    dictionary.setdefault(key, val)
  return dictionary

print("The tuple is converted into the following dictionary",tupletodict(tups))
