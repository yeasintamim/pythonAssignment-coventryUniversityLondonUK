""" Basic BST code for inserting (i.e. building) and printing a tree

    Your ***second standard viva task*** (of 5) will be to implement a find method into
    the class BinaryTree from pseudocode. See the lab task sheet for Week 4. 

    Your ***first advanced viva task*** (of 3) will be to implement a remove (delete) method
    into the class Binary Tree from partial pseudocode. See the lab task sheet for Week 4.

    Since the given code is in python it is strongly suggested you stay with python; but
    if you want to reimplement as C++ this is also OK (see the lab sheet guidance). 
"""

import math                                                         #imports the math module

""" Node class                                                      #doc string
"""

class Node:                                                        
    def __init__(self, data = None):                                #class initialiser with parameters is defined
        self.data = data                                            #data is assigned to self.data
        self.left = None                                            #value 'none' assigned to self.left
        self.right = None                                           #value 'none' assigned to self.left

""" BST class with insert and display methods. display pretty prints the tree
"""

class BinaryTree:                                                   #binary tree class defined where iteration is put
    
    def find_i(self, target):                                       
        cur_node = self.root                                        #cur_node variable defined as self.root
        targetplusone = target+1                                    #targetplusone variable defined and assigned as target incremented
        cur_node.value = targetplusone - 1                          #cur_node.value is set to 1 less than targetplusone
        while cur_node != None:                                     #while loop runs if cur_node is not equal to none
            if cur_node.value is target:                            #if cur_node.value is equal to target
                return True                                         
            elif cur_node.value > target:                           #if cur_node.value is more than target
                cur_node = cur_node.left                            #make cur_node the same as cur_node.left's value
            else:                                                   
                cur_node = cur_node.right                           #this will then append cur_node as the same as cur_node.right's value
        return False                                                #function call as false

    def find_r (self, target):                                      
        cur_node = self.root                                        #the cur_node variable is assigned the self.root value
        if self.root:                                               #if statement will run based on self.root
            if self._find_r(target,cur_node):                       #if target is found using recursive function then
                return True                                         
            return False                                            #otherwise it will return as false
        else:                                                       
            return None                                             #this will then return 'None' to the user
        
    def _find_r (self, target, cur_node):                   
        if target > cur_node.data and cur_node.right:               #if the target is more than both cur_node.data and cur_node.right
            return self._find_r(target, cur_node.right)             #then return recursive function call with self
        elif target < cur_node.data and cur_node.left:              #else if the target is less than the cur_node.data and cur_node.left
            return self._find_r (target,cur_node.left)              #then return the same call but with the left cur_node not right
        if target == cur_node.data:                                 #if the target is the same as the cur_node.data
            return True                                             
                
    def remove(tree, target):                                       
        if tree.root is None :                                      #if 'tree.root' data is empty
            return False                                            
        elif tree.root.data is target:                              #if 'tree.root' data is the same as the target variable's
            if tree.root.left is None and tree.root.right is None:  #and if the root's left is none and root right's is none
                tree.root = None                                    #then the tree.root is assigned 'None'
            elif tree.root.left and tree.root.right is None:        #if the 'tree.root's' left and right is none
                tree.root = tree.root.left                          #the tree.root value is assigned the left value
                
            elif tree.root.left is None and tree.root.right:        #if the left is none but the right isn't
                tree.root = tree.root.right                         #'tree.root' is assigned the right value
            elif tree.root.left and tree.root.right:                #else if the left and right contain data 
                tree.if_left_and_right(tree.root)                   #the function "if_left_and_right" is called with the parameter
        parents = None                                              #parent variable is assigned the 'None' value
        node = tree.root                                            #the node variable is parsed the tree.root data
        
                                                                    #case 1:
        while node and node.data != target:                         #if the node and 'node.data' hold values equal to the target
            parent = node                                           #the parent variable stores the node value
            if target < node.data:                                  #if the target is less than the 'node.data' data
                node = node.left                                    #then the node variable is assigned 
            elif target > node.data:                                #if target is more than the value in node.data
                node = node.right                                   #node variable is given 'node.right' value
                
        if node is None or node.data != target:                     #if the node is empty, or node.data is not equal to target
            return False                                            

                                                                    #case 2:
        elif node.left is None and node.right is None:              #if 'node.left' value is empty and 'node.right' value is empty
            if target < parent.data:                                #if the target is less than the parent.data value
                parent.left = None                                  #make 'parent.left' value equal to none
            else:                                                   
                parent.right = None                                 #this will make the 'parent.right' value none
            return True                                             

                                                                    #case 3:
        elif node.left and node.right is None:                      #if 'node.left' and 'node.right' data is none
            if target < parent.data:                                #if the target is less than the data for the parent
                parent.left = node.left                             #the node.left data is added to the parent.left node
            else:                                                   
                parent.right = node.left                            #this appends the left node data to the 'parent.right'
            return True                                             
        
                                                                    #case 4:
        elif node.left == None and node.right:                      #if 'node.left' is empty none and equals node.right
            if target < parent.data:                                #and if target is less than parent.data value
                parent.left = node.right                            #then the node.right value is assigned to parent.left
            else:                                                   
                parent.right = node.right                           #the 'parent.right' node stores the node.right data
            return True                                             
        
        else:                                                       
            tree.if_left_and_right(node)                            #executes the if_left_and_right method with node parameter
            
    def if_left_and_right(tree,node):                               
        deNodeParent = node                                         #deNodeParent variable is created and assigned the node value
        deNode = node.right                                         #deNode variable created and assigned 'node.right' data

        while deNode.left:                                          #while loop if deNode.left stores data
            deNodeParent = deNode                                   #deNodeParent is assigned the deNode value
            deNode = deNode.left                                    #deNode variable is assigned deNode.left value
        node.data = deNode.data                                     #the node.data variable is assigned the deNode.data value
        if deNode.right:                                            #if deNode.right stores data
            if deNodeParent.data > deNode.data:                     #if the deNodeParent.data value more than the deNode.data value
                deNodeParent.left = deNode.right                    #the deNodeParent.left is assigned the deNode.right value
            elif deNodeParent.data < deNode.data:                   #else if deNodeParent.data is less than the deNode.data value then
                deNodeParent.right = deNode.right                   #the deNodeParent.right stores the deNode.right data
        else:                                                       
            if deNode.data < deNodeParent.data:                     #if the deNode.data is less than the deNodeParent.data values
                deNodeParent.left = None                            #then deNodeParent.left is none, this section removes left node
            else:                                                   #the else case for if deNode.data is not less than deNodeParent.data
                deNodeParent.right = None                           #the deNodeParent.right is made equal to none, this removes right node
                    
    def __init__(self):                                             
        self.root = None                                            #self.root assigned empty value

    def insert(self, data):                                         
        if self.root is None:                                       #if self.root has value none
            self.root = Node(data)                                  #then 'self.root' is assigned the Node data
        else:                                                       
            self._insert(data, self.root)                           #insert the data and self.root data parameters through function

    def _insert(self, data, cur_node):                              
        if data < cur_node.data:                                    #if data value is less than cur_node.data then
            if cur_node.left is None:                               #and if the cur_node.left is empty then
                cur_node.left = Node(data)                          #the cur_node.left is assigned the Node data value
            else:                                                  
                self._insert(data, cur_node.left)                   #the insert function is called 2 parameters, data and cur_node.left
        elif data > cur_node.data:                                  #if the data's value is more than the cur_node.data value then
            if cur_node.right is None:                              #if the cur_node.right is empty or None then
                cur_node.right = Node(data)                         #the cur_node.right is created with the Node(data) value
            else:                                                   
                self._insert(data, cur_node.right)                  #the insert function is called with 2 parameters
        else:                                                       
            print("Value already present in tree")                  #this then prints that the value is present in the tree already

    def display(self, cur_node):                                    
        lines, _, _, _ = self._display(cur_node)                    #variables defined from the cur_node display method
        for line in lines:                                          #for each of the individual lines in the line variable
            print(line)                                             #the line variable is printed out to the screen

    def _display(self, cur_node):                                   
        if cur_node.right is None and cur_node.left is None:        #if both cur_node.right is none and the cur_node.left is none
            line = '%s' % cur_node.data                             #the line variable is created with the cur_node.data value
            width = len(line)                                       #width variable created with the length of the line value
            height = 1                                              #height variable created with the height value 1
            middle = width // 2                                     #middle variable created and assigned width value floor divided
            return [line], width, height, middle                    #this returns the the variables from the function call

        if cur_node.right is None:                                  #if statement if cur_node.right is empty
            lines, n, p, x = self._display(cur_node.left)           #then the 4 variables are assigned output from the function call
            s = '%s' % cur_node.data                                #s variable declaration and assigned cur_node.data value
            u = len(s)                                              #u variable created and assigned the length of the s variable
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s      #first_line variable takes values needed to print the first line
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '     #second_line takes values, nessesary for second line
            shifted_lines = [line + u * ' ' for line in lines]      #the shifted line variable is assigned values
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2  #this returns the variables needed from statement
        
        if cur_node.left is None:                                   #cur_node.left is empty or none then
            lines, n, p, x = self._display(cur_node.right)          #variable creation and assignment from function call
            s = '%s' % cur_node.data                                #s variable creation from cur_node.data values
            u = len(s)                                              #u variable created and assigned length of s variable
            first_line = s + x * '_' + (n - x) * ' '                #first_line variable created and assigned
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '  #second line variable created and assigned
            shifted_lines = [u * ' ' + line for line in lines]      #shifted_lines variable created an values assigned
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2  #this returns the variables needed from call

        left, n, p, x = self._display(cur_node.left)                #creation of various variables and data assignment from function call
        right, m, q, y = self._display(cur_node.right)              #creation of variables and another assignmend from function call
        s = '%s' % cur_node.data                                    #s variable creation and assignment from cur_node.data value
        u = len(s)                                                  #u variable creation and assignment from s length
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '    #first_line variable creation and assignment
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '  #second_line variable created and assigned
        if p < q:                                                   #if statement for when p is less than q
            left += [n * ' '] * (q - p)                             #then left variable had variabled added to assignment
        elif q < p:                                                 #else if the q is less than p then
            right += [m * ' '] * (p - q)                            #right is assigned the additional data
        zipped_lines = zip(left, right)                             #zippered_lines variable creation and assignment
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]  #the lines variable is assigned values
        return lines, n + m + u, max(p, q) + 2, n + u // 2          #the return statement returns the variables needed from function call
    
bst = BinaryTree()                                                  #variabe object created from class
bst.insert(4)                                                       #objects called with function to insert the numbers into the binary tree
bst.insert(6)                                                       
bst.insert(2)                                                       
bst.insert(6)                                                       
bst.insert(1)                                                       
bst.insert(3)                                                       
bst.insert(5)                                                      
bst.insert(7)                                                       
bst.insert(8)                                                       
bst.insert(9)                                                       
#bst.insert(10)
#bst.insert(11)
#bst.insert(12)
#bst.insert(13)
#bst.insert(14)
#bst.insert(15)
#bst.insert(100)
#bst.insert(200)

print("\nthis is the tree before the value is taken out:\n")        #print statement to tell user what the next display is for
bst.display(bst.root)                                               #display function call to display tree before removal of 8

print(bst.find_i(19))                                               #here the iterative function is called and output is printed
print(bst.find_r(30))                                               #here the recursive function is valled and output is printed

bst.remove(8)                                                       #object is called to remove value '8' from the tree

print("\nthis is the tree after the value is taken out:\n")         #print statement for after the value is removed from tree
bst.display(bst.root)                                               #bst object called with display to show tree after removal