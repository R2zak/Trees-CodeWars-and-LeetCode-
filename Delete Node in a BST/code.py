class Solution:
    def deleteNode(self,root, key: int):
        if not root:
            return 
        if root.val!=key:
            if key<root.val:
                root.left=self.deleteNode(root.left,key)
                return root
            else:
                root.right=self.deleteNode(root.right,key)
                return root
        if not root.left and not root.right:
            root=None
        elif not root.left:
            root=root.right
        elif not root.right:
            root=root.left
        else:
            smalest=root.right
            while smalest.left!=None:
                smalest=smalest.left
            root.val=smalest.val
            root.right=self.deleteNode(root.right,smalest.val)
        return root
