def find_missing(a, b):
	if len(a) == 0 and len(b) == 0:
		return 0
	elif len(a) == len(b):
		if len(set(a) - set(b)) == 0:
			return 0
	elif len(a) > len(b):
		num = set(a) - set(b)
	else:
		num = set(b) - set(a)
	return next(iter(num))