def bracket_checker(code):
	''' use a stack to define last in, last out 
	'''

	''' define a dictionary to hold the pairs'''
	bracket_pairs = {
	'(':')',
	'{':'}',
	'[':']'}

	openers = set(bracket_pairs.keys())
	closers = set(bracket_pairs.values())


	openers_stack = []
	for char in code:
		if char in openers:
			openers_stack.append(char)
		
		elif char in closers:
			# if theres nothing in the stack, return false
			if not openers_stack:
				return False
			else:
				last_unclosed_opener = openers_stack.pop()
				if bracket_pairs[last_unclosed_opener] != char:
					return False

	return openers_stack == []
			



if __name__ == "__main__":

	valid = bracket_checker("(){}){(){}[]")
	print(valid)


