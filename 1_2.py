#coding=utf-8
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class TreePrinter:
    def printTree(self,root):
        import Queue
        q=Queue.Queue(500)
        last = root
        nlast =root
        tree_save=[]
        tree_save_line=[]
        q.put(root)
        while q.empty() !=True:
            s = q.get()
            tree_save_line.append(s.val)
            if s.left != None:
                q.put(s.left)
                nlast = s.left
            if s.right != None:
                q.put(s.right)
                nlast = s.right
            if s == last:
                tree_save.append(tree_save_line)
                tree_save_line=[]
                last = nlast
            return tree_save



