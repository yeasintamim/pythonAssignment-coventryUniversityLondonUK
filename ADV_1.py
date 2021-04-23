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
    def __init__(self, data = None):                                # parameters is defined
        self.data = data                                            
        self.left = None                                            
        self.right = None                                           

""" BST with insert and display methods. display  the tree
"""

class BinaryTree:                                                   #binary tree class defined where iteration is put
    
    def find_i(self, target):                                       
        cur_node = self.root                                        #cur_node variable defined as self.root
        targetplusone = target+1                                   
        cur_node.value = targetplusone - 1                          
        while cur_node != None:                                     
            if cur_node.value is target:                           
                return True                                         
            elif cur_node.value > target:                           
                cur_node = cur_node.left                            
            else:                                                   
                cur_node = cur_node.right                           
        return False                                                

    def find_r (self, target):                                      
        cur_node = self.root                                        
        if self.root:                                               
            if self._find_r(target,cur_node):                       
                return True                                         
            return False                                           
        else:                                                       
            return None                                             
        
    def _find_r (self, target, cur_node):                   
        if target > cur_node.data and cur_node.right:               
            return self._find_r(target, cur_node.right)             # return recursive function call
        elif target < cur_node.data and cur_node.left:              
            return self._find_r (target,cur_node.left)              # return the same call  with the left cur_node not right
        if target == cur_node.data:                                 
            return True                                             
                
    def remove(tree, target):                                       
        if tree.root is None :                                      
            return False                                            
        elif tree.root.data is target:                              
            if tree.root.left is None and tree.root.right is None:  
                tree.root = None                                    
            elif tree.root.left and tree.root.right is None:        
                tree.root = tree.root.left                          
                
            elif tree.root.left is None and tree.root.right:        
                tree.root = tree.root.right                         
            elif tree.root.left and tree.root.right:                 
                tree.if_left_and_right(tree.root)                   
        parents = None                                              
        node = tree.root                                            
        
                                                                    #case 1:
        while node and node.data != target:                         
            parent = node                                           
            if target < node.data:                                  
                node = node.left                                    
            elif target > node.data:                                
                node = node.right                                   
                
        if node is None or node.data != target:                     
            return False                                            

                                                                    #case 2:
        elif node.left is None and node.right is None:              
            if target < parent.data:                                
                parent.left = None                                  
            else:                                                   
                parent.right = None                                 
            return True                                             

                                                                    #case 3:
        elif node.left and node.right is None:                      
            if target < parent.data:                                
                parent.left = node.left                             
            else:                                                   
                parent.right = node.left                            
            return True                                             
        
                                                                    #case 4:
        elif node.left == None and node.right:                      
            if target < parent.data:                                
                parent.left = node.right                            
            else:                                                   
                parent.right = node.right                           
            return True                                             
        
        else:                                                       
            tree.if_left_and_right(node)                            #executes the if_left_and_right method with node parameter
            
    def if_left_and_right(tree,node):                               
        deNodeParent = node                                         #deNodeParent variable is created and assigned the node value
        deNode = node.right                                         #deNode variable created and assigned 'node.right' data

        while deNode.left:                                          
            deNodeParent = deNode                                   
            deNode = deNode.left                                    
        node.data = deNode.data                                     
        if deNode.right:                                            
            if deNodeParent.data > deNode.data:                     
                deNodeParent.left = deNode.right                    
            elif deNodeParent.data < deNode.data:                   
                deNodeParent.right = deNode.right                   
        else:                                                       
            if deNode.data < deNodeParent.data:                     
                deNodeParent.left = None                           
            else:                                                   
                deNodeParent.right = None                           
                    
    def __init__(self):                                             
        self.root = None                                           

    def insert(self, data):                                         
        if self.root is None:                                       
            self.root = Node(data)                                  
        else:                                                       
            self._insert(data, self.root)                           

    def _insert(self, data, cur_node):                              
        if data < cur_node.data:                                   
            if cur_node.left is None:                               
                cur_node.left = Node(data)                         
            else:                                                  
                self._insert(data, cur_node.left)                   
        elif data > cur_node.data:                                  
            if cur_node.right is None:                              
                cur_node.right = Node(data)                         
            else:                                                   
                self._insert(data, cur_node.right)                  
        else:                                                       
            print("Value already present in tree")                 

    def display(self, cur_node):                                    
        lines, _, _, _ = self._display(cur_node)                    
        for line in lines:                                          
            print(line)                                             

    def _display(self, cur_node):                                   
        if cur_node.right is None and cur_node.left is None:        
            line = '%s' % cur_node.data                             
            width = len(line)                                       
            height = 1                                              
            middle = width // 2                                     
            return [line], width, height, middle                    

        if cur_node.right is None:                                  
            lines, n, p, x = self._display(cur_node.left)           
            s = '%s' % cur_node.data                                
            u = len(s)                                              
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s      
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '     
            shifted_lines = [line + u * ' ' for line in lines]      
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2  
        
        if cur_node.left is None:                                   
            lines, n, p, x = self._display(cur_node.right)          
            s = '%s' % cur_node.data                                
            u = len(s)                                             
            first_line = s + x * '_' + (n - x) * ' '                
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '  
            shifted_lines = [u * ' ' + line for line in lines]      #shifted_lines variable created an values assigned
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2  

        left, n, p, x = self._display(cur_node.left)               
        right, m, q, y = self._display(cur_node.right)              
        s = '%s' % cur_node.data                                    
        u = len(s)                                                  
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '    #first_line variable creation and assignment
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '  #second_line variable created and assigned
        if p < q:                                                    
            left += [n * ' '] * (q - p)                              
        elif q < p:                                                  
            right += [m * ' '] * (p - q)                             
        zipped_lines = zip(left, right)                              
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]   
        return lines, n + m + u, max(p, q) + 2, n + u // 2           
    
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

print("\nthis is the tree before the value is taken out:\n")         
bst.display(bst.root)                                                

print(bst.find_i(19))                                                
print(bst.find_r(30))                                                

bst.remove(8)                                                        

print("\nthis is the tree after the value is taken out:\n")          
bst.display(bst.root)                                                