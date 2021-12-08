from collections import deque


def breadth_first(root):
	queue = deque()

	while root is not None:
		print(root.data)

		if root.left is not None:
			queue.append(root.left)

		if root.right is not None:
			queue.append(root.right)

		if len(queue) > 0:
			root = queue.popleft()
		else:
			root = None

