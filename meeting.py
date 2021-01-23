def merge_ranges(meetings):
	if len(meetings) < 1:
		return False

	# sort based on start time
	sorted_meetings = sorted(meetings)

	merged_meetings = [sorted_meetings[0]]

	for curr_start, curr_end in  sorted_meetings[1:]:
		# get the last element in the merged array
		last_start, last_end = merged_meetings[-1]

			# criteria for overlap
		if (curr_start <= last_end) or (curr_end <= last_end) or (curr_start == last_start):
			merged_meetings[-1] = (last_start, max(curr_end, last_end))
		else:
			merged_meetings.append((curr_start, curr_end))

	return merged_meetings



if __name__ == "__main__":
	x = 0
	meetings =   [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
	print(	merge_ranges(meetings))
