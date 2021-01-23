class BinaryTreeNode(object):
	def __init__(self, value):
		self.value = value
		self.right = None
		self.left = None

	def insert_left(self, value):
		self.left = BinaryTreeNode(value)
		self.left.node_depth = self.left.node_depth + 1

	def insert_right(self, value):
		self.right = BinaryTreeNode(value)
		self.right.node_depth = self.right.node_depth + 1


	def is_super(root):

		if root == None:
			return True

		depths = []
		nodes = []

		# save the node and its depth
		nodes.append((root, 0))
		
		while len(nodes):
			node, depth = nodes.pop()
			# check if this is a leaf node
			if (not node.left) and (not node.left):
				if depth not in depths:
					depths.append(depth)


					# if more than 2 depts 
					if ((len(depths)> 2) or (len(depths) == 2 and abs(depths[0] - depths[1]) > 1)):
						return False

			else:
				if node.left:
					nodes.append((node.left, depth + 1))
				if node.right:
					nodes.append((node.right, depth + 1))

		return True

if __name__ == "__main__":
	x=0
