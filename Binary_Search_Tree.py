class BinarySearchTree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def Insert_value_into_Tree(self, val):
        if self.val == val:
            # if Value is already in Tree Return None
            return
        if self.val > val:
            # left
            if self.left is not None:
                # call recursion
                self.left.Insert_value_into_Tree(val)
            else:
                # create a Node
                self.left = BinarySearchTree(val)
        else:
            # right
            if self.right is not None:
                # call recursion
                self.right.Insert_value_into_Tree(val)
            else:
                # create a Node
                self.right = BinarySearchTree(val)

    def Inorder_Traversal(self):
        # First Visit Left Node --> After Visit Root Node --> finally Visit Right Node
        elements = []
        if self.left:
            elements += self.left.Inorder_Traversal()
        elements.append(self.val)
        if self.right:
            elements += self.right.Inorder_Traversal()
        return elements

    def PreOrder_Traversal(self):
        # First Visit root Node --> After Visit Left Node --> Finally Visit Right
        elements = [self.val]
        if self.left:
            elements += self.left.PreOrder_Traversal()
        if self.right:
            elements += self.right.Inorder_Traversal()
        return elements

    def PostOrder_Traversal(self):
        # First Visit Left Node --> After Visit Right Node --> Finally Visit Root Node
        elements = []
        if self.left:
            elements += self.left.PostOrder_Traversal()
        if self.right:
            elements += self.right.PostOrder_Traversal()
        elements.append(self.val)
        return elements

    def Searching(self, val):
        if self.val == val:
            return f"{val} is in our Tree"
        elif self.val > val:
            if self.left:
                return self.left.Searching(val)
            else:
                return f"{val} is not in our Tree"
        else:
            if self.right:
                return self.right.Searching(val)
            else:
                return f"{val} is not in our Tree"
    def Find_max_value_in_the_Tree(self):
        if self.right:
            return self.right.Find_max_value_in_the_Tree()
        else:
            return self.val

    def Find_min_value_in_the_Tree(self):
        if self.left:
            return self.left.Find_min_value_in_the_Tree()
        else:
            return self.val

def Convert_List_Items_Into(elements):
    # Create a Tree by using List Elements
    root = BinarySearchTree(elements[0])
    for i in range(1, len(elements)):
        root.Insert_value_into_Tree(elements[i])
    return root


r"""
# Create a Tree Object
tree = BinarySearchTree(50)
tree.Insert_value_into_Tree(25)
tree.Insert_value_into_Tree(15)
tree.Insert_value_into_Tree(35)
tree.Insert_value_into_Tree(75)
tree.Insert_value_into_Tree(65)
tree.Insert_value_into_Tree(100)

print(tree.Inorder_Traversal())

                    50
                   /  \
                 25    75
                /  \   / \
              15   35 65 100



"""

list_items = [500, 250, 100, 300, 50, 450, 400, 600, 700, 800, 950, 910, 670]
tree = Convert_List_Items_Into(list_items)
print("Inorder Traversal: ", tree.Inorder_Traversal())
print("Preorder Traversal: ", tree.PreOrder_Traversal())
print("Postorder Traversal: ", tree.PostOrder_Traversal())
print(tree.Searching(1))
print("Maximum Value in out Tree is: ", tree.Find_max_value_in_the_Tree())
print("Minimum Value in our tree is: ", tree.Find_min_value_in_the_Tree())

r"""
Our Tree Seems Like Below 

                                    500
                                  /     \
                                250     600
                               /  \        \
                             100  300      700
                            /        \     /  \  
                          50         450 670  800
                                    /            \
                                  400            910
                                                    \
                                                    950


Output:
    Inorder Traversal:  [50, 100, 250, 300, 400, 450, 500, 600, 670, 700, 800, 910, 950]
    Preorder Traversal:  [500, 250, 100, 50, 300, 400, 450, 600, 670, 700, 800, 910, 950]
    Postorder Traversal:  [50, 100, 400, 450, 300, 250, 670, 910, 950, 800, 700, 600, 500]
    1 is not in our Tree
    Maximum Value in out Tree is:  950
    Minimum Value in our tree is:  50

"""