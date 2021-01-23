def make_change(amount, denoms):

	if amount == 0:
		return 1

	if amount == 1:
		return 0

	print ("checking ways to make {} with {} ".format(
		amount, denoms))
	num_ways = 0
	aug_denoms = denoms[:]

	# for each denomination
	for denom in denoms:
		aug_denoms.remove(denom)
		# for the number of times it divides the amount
		for idx in range(1,int(amount/denom)+1):
			num_ways += make_change(amount-(denom*idx), aug_denoms)

	return num_ways
	# this has an O(m * n) in time and space 


if __name__ == "__main__":
	x = 0
	denoms = [1,2,3]
	print(make_change(4, denoms))
