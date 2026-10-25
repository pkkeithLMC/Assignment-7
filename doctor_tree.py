class DoctorNode:
    def __init__(self, value):
        self.name = value
        self.left = None
        self.right = None




class DoctorTree:
    def __init__(self):
        self.root = None


    def insert(self, doctor_name, report_name, side, current_node = None):

        #Case #1: Empty Tree
        if self.root is None:
            print("Tree is empty.  Cannot insert with a team lead.")
            return False

        #Start at root if this is the first call
        if current_node is None:
            current_node = self.root

        #Case 2:  Found the Doctor
        if current_node.name == doctor_name:

            if side == "left" and current_node.left is None:
                current_node.left = DoctorNode(report_name)
                print(f"{report_name} added to the LEFT of {doctor_name}")
                return True

            elif side == "right" and current_node.right is None:
                current_node.right = DoctorNode(report_name)
                print(f"{report_name} added to the RIGHT of {doctor_name}")
                return True

            elif side not in ("left", "right"):
                print("Invalide side.  Choose left or right")
                return True

            else:
                print("{doctor_name} already has an employee of the {side}.")
                return True

        #Case 3:  Recursivley search the subtrees
        found_left = False
        found_right = False

        if current_node.left:
            found_left = self.insert(
                doctor_name,
                report_name,
                side,
                current_node.left
            )

        if current_node.right and not found_left:
            found_right = self.insert(
                doctor_name,
                report_name,
                side,
                current_node.right
            )

        # Case 4: Manager not found
        if not (found_left or found_right):
            if current_node == self.root:
                print(f"❌ Doctor {doctor_name} not found in the tree.")
            return False

        return True

    def print_tree(self, node=None, level=0):

        if node is None:
            if level == 0:
                node = self.root
            else:
                return

        if node is None:
            print("The Doctor directory is empty.")
            return

        indent = "    " * level
        print(f"{indent}- {node.name}")

        # Recursively print left and right subtrees
        self.print_tree(node.left, level + 1)
        self.print_tree(node.right, level + 1)


    def preorder(self, node):
        #Visit the current node
        #Traverse the left subtree first and append results
        #Traverse the right subtree second and append results
        if node is None:
            return []

        result = [node.name]

        result += self.preorder(node.left)
        result += self.preorder(node.right)

        return result


    def inorder( self, node):
        #Traverse the left tree recursively and append results to the list
        #Visit the current node (root node) and add the value
        #Travers the right subtree and append results
        if node is None:
            return[]

        result = []
        result += self.inorder(node.left)
        result.append( node.name)
        result += self.inorder(node.right)

        return result


    def postorder(self, node):
        #Left sub tree is visited first
        #Then the right sub tree is visited
        #Finally the root is processed

        if node is None:
            return []

        result = []
        result += self.postorder(node.left)
        result += self.postorder(node.right)
        result.append(node.name)

        return result
    
# Test your DoctorTree and DoctorNode classes here

tree = DoctorTree()
tree.root = DoctorNode("Dr. Croft")

tree.insert("Dr. Croft", "Dr. Goldsmith", "right")
tree.insert("Dr. Croft", "Dr. Phan", "left")
tree.insert("Dr. Phan", "Dr. Carson", "right")
tree.insert("Dr. Phan", "Dr. Morgan", "left")

#tree.print_tree()
print(f"Preorder {tree.preorder(tree.root)}")
print(f"Inorder {tree.inorder(tree.root)}")
print(f"Postorder {tree.postorder(tree.root)}")