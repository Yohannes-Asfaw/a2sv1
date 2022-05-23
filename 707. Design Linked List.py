class Node:
	def __init__(self, val, next_):
		self.val = val 
		self.next = next_
class MyLinkedList:

	def __init__(self):
		self.head = None

	def get(self, index: int) -> int:
		if not self.head: return -1
		root = self.head
		while root and index:
			root = root.next
			index -= 1
		return root.val if root else -1 

	def addAtHead(self, val: int) -> None:
		new = Node(val, None)
		if self.head:
			new.next = self.head
			self.head = new
		else: self.head = new

	def addAtTail(self, val: int) -> None:
		if self.head:
			root = self.head
			prev = root
			while root:
				root, prev = root.next, root
			prev.next = Node(val,None)
		else: self.addAtHead(val)

	def addAtIndex(self, index: int, val: int) -> None:
		if not index:
			self.addAtHead(val)
			return None 
		if self.head:
			root = self.head
			prev = root
			while root and index:
				root, prev = root.next, root
				index -= 1
			if not index: 
				temp = prev.next 
				prev.next = Node(val,temp)
		else: 
			if not index: self.addAtHead(val)
	def deleteAtIndex(self, index: int) -> None:
		if self.head:
			if not index: 
				self.head = self.head.next
				return None
			root = self.head
			prev = root
			while root and index:
				root, prev = root.next, root
				index -= 1
			if not index: 
				if root: prev.next = root.next
				else: prev.next = root



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
