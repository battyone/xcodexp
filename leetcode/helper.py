# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Tree(object):

    @staticmethod
    def deserialize(lst):
        root = TreeNode(lst[0])
        q = [ root ]
        i = 1
        while i < len(lst):
            n = q.pop(0)
            if lst[i] != '#':
                n.left = TreeNode(lst[i])
                q.append(n.left)
            i += 1
            if i >= len(lst):
                break
            if lst[i] != '#':
                n.right = TreeNode(lst[i])
                q.append(n.right)
            i += 1
        return root

    @staticmethod
    def serialize(root):
        if not root: return []
        result = []
        q = [ root ]
        while q:
            n = q.pop(0)
            if not n:
                result.append('#')
            else:
                result.append(n.val)
                if n.left or n.right:
                    q.append(n.left)
                    q.append(n.right)
        while result and result[-1] == '#':
            result = result[:-1]
        return result


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class List(object):

    @staticmethod
    def build(L):
        if not L: return None
        head = ListNode(L[0])
        curr = head
        for v in L[1:]:
            curr.next = ListNode(v)
            curr = curr.next
        return head

    @staticmethod
    def extract(head):
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return res

