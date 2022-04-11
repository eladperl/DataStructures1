#username - complete info
#id1      - complete info
#name1    - complete info
#id2      - 204327258
#name2    - elhadperl

###   DELETE ###
""" AVL STRUCTURE & STRATEGY:
*  Done basic code of functions:
		* retrieve
*  Indexes structure ==> using ranks ad keys maintaining functions by update right.size & left.size fields in nodes.
"""

"""A class representing a node in an AVL tree1"""

class AVLNode(object):
	"""Constructor, you are allowed to add more fields.

	@type value: str
	@param value: data of your node
	"""
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None
		self.parent = None
		self.height = -1
		### More fields ###
		self.size = 1                    # Temp' - might define different
		self.rank = None                     # Temp' - might define different

	"""returns the left child
	@rtype: AVLNode
	@returns: the left child of self, None if there is no left child
	"""
	def getLeft(self):
		return self.left


	"""returns the right child

	@rtype: AVLNode
	@returns: the right child of self, None if there is no right child
	"""
	def getRight(self):
		return self.right

	"""returns the parent 

	@rtype: AVLNode
	@returns: the parent of self, None if there is no parent
	"""
	def getParent(self):
		return self.parent

	"""return the value

	@rtype: str
	@returns: the value of self, None if the node is virtual
	"""
	def getValue(self):
		return self.value

	"""returns the height

	@rtype: int
	@returns: the height of self, -1 if the node is virtual
	"""
	def getHeight(self):
		if not self.isRealNode():
			return -1
		return self.height

	"""sets left child

	@type node: AVLNode
	@param node: a node
	"""
	def setLeft(self, node):
		return None

	"""sets right child

	@type node: AVLNode
	@param node: a node
	"""
	def setRight(self, node):
		return None

	"""sets parent

	@type node: AVLNode
	@param node: a node
	"""
	def setParent(self, node):
		return None

	"""sets value

	@type value: str
	@param value: data
	"""
	def setValue(self, value):
		return None

	"""sets the balance factor of the node

	@type h: int
	@param h: the height
	"""
	def setHeight(self, h):
		return None

	"""returns whether self is not a virtual node 

	@rtype: bool
	@returns: False if self is a virtual node, True otherwise.
	"""
	def isRealNode(self):
		if self.value == "virtual":
			return True
		return False


"""
A class implementing the ADT list, using an AVL tree.
"""

class AVLTreeList(object):

	"""
	Constructor, you are allowed to add more fields.  

	"""
	def __init__(self):
		self.root = None
		self.size = 0
		self.first = None
		self.last = None


	"""returns whether the list is empty

	@rtype: bool
	@returns: True if the list is empty, False otherwise
	"""
	def empty(self):
		if self.size == 0:
			return True
		return False


	"""retrieves the value of the i'th item in the list

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: index in the list
	@rtype: str
	@returns: the the value of the i'th item in the list
	"""
	def retrieve(self, i):
		def retrieve_rec(node, i):
			rank = node.left.size + 1
			if rank == i:
				return node.value
			if i < rank:
				return retrieve_rec(node.getLeft(), i)
			else:
				return retrieve_rec(node.getLeft(), i-rank)

		return retrieve_rec(self.root, i + 1).value


	"""inserts val at position i in the list

	@type i: int
	@pre: 0 <= i <= self.length()
	@param i: The intended index in the list to which we insert val
	@type val: str
	@param val: the value we inserts
	@rtype: list
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	def insert(self, i, val):
		elem = AVLNode(val)
		def retrieve_rec(node, i):
			rank = node.left.size + 1
			if rank == i:
				return node
			if i < rank:
				return retrieve_rec(node.getLeft(), i)
			else:
				return retrieve_rec(node.getLeft(), i-rank)
		pos = retrieve_rec(self.root, i+1)
		if pos.left.isRealNode():
			elem.left = pos.left
			elem.left.parent = elem
			pos.left = elem
			elem.parent = pos
			elem.right = AVLNode("virtual")
			elem.right.parent = pos
			elem.right.size = 0

		else:
			pos = pos.left
			while pos.value != "virtual":
				pos = pos.right
			elem.parent = pos.parent
			elem.parent.right = elem
			elem.right = pos
			pos.parent = elem
			elem.left = elem.left = AVLNode("virtual")
			elem.left.size = 0

		"""if self.empty():
			self.root = AVLNode(val)
			self.root.rank = i+1
			self.root.left = AVLNode("virtual")
			self.root.right = AVLNode("virtual")
		else:
			pos = self.root
			curr_rank = self.root.rank
			while curr_rank != i:
				if i < curr_rank-1:
					pos = pos.getLeft()
				else:
					pos = pos.getRight()
			"""
		return -1


	"""deletes the i'th item in the list

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: The intended index in the list to be deleted
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	def delete(self, i):
		return -1


	"""returns the value of the first item in the list

	@rtype: str
	@returns: the value of the first item, None if the list is empty
	"""
	def first(self):
		return None

	"""returns the value of the last item in the list

	@rtype: str
	@returns: the value of the last item, None if the list is empty
	"""
	def last(self):
		return None

	"""returns an array representing list 

	@rtype: list
	@returns: a list of strings representing the data structure
	"""
	def listToArray(self):
		res = [i for i in range(self.size)]
		### Travel in tree and then add elements by rank as indexes ###
		return res

	"""returns the size of the list 

	@rtype: int
	@returns: the size of the list
	"""
	def length(self):
		return self.size

	"""splits the list at the i'th index

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: The intended index in the list according to whom we split
	@rtype: list
	@returns: a list [left, val, right], where left is an AVLTreeList representing the list until index i-1,
	right is an AVLTreeList representing the list from index i+1, and val is the value at the i'th index.
	"""
	def split(self, i):
		return None

	"""concatenates lst to self

	@type lst: AVLTreeList
	@param lst: a list to be concatenated after self
	@rtype: int
	@returns: the absolute value of the difference between the height of the AVL trees joined
	"""
	def concat(self, lst):
		return None

	"""searches for a *value* in the list

	@type val: str
	@param val: a value to be searched
	@rtype: int
	@returns: the first index that contains val, -1 if not found.
	"""
	def search(self, val):
		return None



	"""returns the root of the tree representing the list

	@rtype: AVLNode
	@returns: the root, None if the list is empty
	"""
	def getRoot(self):
		"""if self.empty():
			return None"""
		return self.root

