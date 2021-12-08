"""
	binary tree implementation
"""


class Node:
	def __init__(self, data):
		self.left = None
		self.right = None
		self.data = data


class BST:
	def __init__(self):
		self.root = None

	def _insert_node(self, curr_node, val):
		""" 
			assists the self.insert function to insert new nodes
			@param curr_node: current node
			@param val: value
		"""

		if val < curr_node.data:
			if curr_node.left is None:
				curr_node.left = Node(val)
			else:
				self._insert_node(curr_node.left, val)
		else:
			if curr_node.right is None:
				curr_node.right = Node(val)
			else:
				self._insert_node(curr_node.right, val)

	def insert(self, val):
		""" inserts a new node (value->val) to the tree """\

		if self.root is None:
			self.root = Node(val)
		else:
			self._insert_node(self.root, val)


	def pre_order_print(self, root):
		if not root:
			return 
		print(root.data)
		self.pre_order_print(root.left)
		self.pre_order_print(root.right)

	def post_order_print(self, root):
		if not root:
			return 
		self.post_order_print(root.left)
		self.post_order_print(root.right)
		print(root.data)


	def in_order_print(self, root):
		if not root:
			return
		self.in_order_print(root.left)
		print(root.data)
		self.in_order_print(root.right)


	def traverse(self):
		""" combines all traversing functions in one """
		print("Pre-order print:")
		self.pre_order_print(self.root)
		print("Post-order print:")
		self.post_order_print(self.root)
		print("In-order print:")
		self.in_order_print(self.root)


	def find_parent(self,root, value):
		""" finds the parent node of the value given """

		if root is None:
			return None

		if root.data == value:
			return None
		if value < root.data:
			if root.left is None:
				return None
			elif value == root.left.data :
				return root
			else:
				return self.find_parent(root.left, value)
		else:
			if root.right is None:
				return None
			elif value == root.right.data:
				return root
			else:
				return self.find_parent(root.right, value)


	def find_node(self, root, value):
		if root is None:
			return None

		if root.data == value:
			return root

		if value < root.data:
			return self.find_node(root.left, value)
		else:
			return self.find_node(root.right, value)

		
	def find_min(self,root):
		if root is None:
			return None

		if root.left is None:
			return root
		else:
			return self.find_min(root.left)


	def find_max(self,root):
		if root is None:
			return None

		if root.right is None:
			return root
		else:
			return self.find_min(root.right)


	def delete(self, root, value):
		""" 
			removes the node with the @param 'value' 

			CASES:
				1. node to remove is a leaf node; or
				2. node to remove has right subtree but not left; or
				3. node to remove has left subtree but not right; or
				4. node to remove has both right and left subtree
					- we can promote the largest value in left subtree
				5. this is an implicit case; node to remove is the only node in the tree

		"""

		count = 1

		node_to_remove = self.find_node(root, value)

		# check if the node exists
		if node_to_remove is None:
			return False

		# node to remove parent
		parent = self.find_parent(root, value)


		if count == 1:
			# only node in bst
			root = None

		elif node_to_remove.left is None and node_to_remove.right is None:
			# case 1

			if node_to_remove.data < parent.data:
				parent.left = None
			else:
				parent.right = None
		elif node_to_remove.left is None and node_to_remove.right is not None:
			# case 2

			if node_to_remove.data < parent.data:
				parent.left = node_to_remove.right
			else:
				parent.right = node_to_remove.right

		elif node_to_remove.left is None and node_to_remove.right is None:
			# case 3

			if node_to_remove.data < parent.data:
				parent.left = node_to_remove.left
			else:
				parent.right = node_to_remove.left
		else:
			# case 4

			largest_value = node_to_remove.left

			while largest_value.right is not None:
				# find the largest value in the left subtree of node_to_remove
				largest_value = largest_value.right

			# set the parent' right pointer of largest_node to None
			largest_value_parent = self.find_parent(root, largest_value.data)
			largest_value_parent.right = None

			node_to_remove.data = largest_value.data

		count -= 1
		return True






if __name__ == "__main__":
	from breadth_first_search import breadth_first
	
	bst = BST()

	# data = [23, 14, 7, 9, 31, 45, 43, 40, 44, 50]
	data  = [4, 2, 1,3, 6, 5, 7]

	for i in data:
		bst.insert(i)

	bst.pre_order_print(bst.root)
	# traverse
	"""bst.traverse()
	print(bst.find_parent(bst.root,7))
	print(bst.find_node(bst.root, 7))
	print("Min node:", bst.find_min(bst.root))
	print("Max node:", bst.find_max(bst.root))
	print("Deleting a node:", bst.delete(bst.root, 23))
	breadth_first(bst.root)"""

