#coding: utf-8


class Pagination(object):
	def __init__(self,items,per_page,limit = 2):
		self.pages = len(items) / per_page
		self.per_page = per_page
		self.joined_edge =[]
		self.left_edge = []
		self.right_edge = []
		self.center = []
		# default settings
		self.limit = limit


	def set_idx(self,idx):
		self.idx = idx

	def inject_list(self):
		if self.idx < self.pages - self.limit:
			for i in range(self.pages-self.limit+1,self.pages+1):
				self.right_edge.append(i)

		if (self.idx - self.limit > 0 and self.idx + self.limit < self.pages ):
			_range = [self.idx - self.limit,self.idx + self.limit]
			_from = _range[0]
			_end = _range[1]
			self.center =  [".."] + range(0,self.pages)[_from:_end] + [".."]

		if self.idx - self.limit >  0:
			for i in range(0+1,self.limit+1):
				self.left_edge.append(i)
		self.joined_edge = list(self.left_edge + self.center + self.right_edge)



	def format_list(self):
		""" ..が意味をなさなかったら削除 """
		diff_left = self.joined_edge[self.limit+1] - self.joined_edge[1]
		if diff_left == 1:
			del self.joined_edge[self.limit]
		elif diff_left == -1:
			del self.joined_edge[:3]
			del self.joined_edge[0]

		elif diff_left == 0:
			del self.joined_edge[1:3]


		diff_right = self.joined_edge[-self.limit] - self.joined_edge[-2+self.limit]
		if diff_right == 1:
			del self.joined_edge[-3]
		return self.joined_edge

	def has_prev(self):
		if self.idx -self.limit > 0:
			return True
		else:
			return False

	def has_next(self):
		if self.idx  + self.limit < self.pages:
			return True
		else:
			return False

	def show_iter(self):
		self.inject_list()
		return self.format_list()


	def __repr__(self):
		return self.current_dx


# demo
def main():
	# 1000個のアイテム
	items = [item for item in range(0,1000)]

	# アイテムを10ページに分けて表示する
	pagination = Pagination(items,10)

	# 右端、左端にそれぞれ5この値を表示する
	pagination.limit = 5

	# 94番目のidxにセット
	pagination.set_idx(94)
	# if show_iter has prev and next, then show it .
	if pagination.has_prev() and pagination.has_next():
		print pagination.show_iter()
	else:
		print "out of range"

if __name__ == '__main__':
	main()