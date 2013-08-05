# Pagination
## Pagination made easy!

If you are at 94th of 1000 items and set limit to 5, and outputs 10 items per page,

It should return list like this...

	[1, 2, 3, 4, 5, '..', 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, '..', 96, 97, 98, 99, 100]


## Demo Code

	# generate 1000 items.

	items = [item for item in range(0,1000)]

	# set per page to 10
	pagination = Pagination(items,10)

	# set limit to 5
	pagination.limit = 5

	# set idx to 94
	pagination.set_idx(94)

	# if it has prev and next, then show it .

	if pagination.has_prev() and pagination.has_next():
		print pagination.show_iter()
	else:
		print "out of range"



