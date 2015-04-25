class Trie(object):
    """ root node """

    # empty constructor
    def __init__ (self):
        self.root=Node('*')
        # the root will always containt the * symbol
        # the roon is an object of class Node, and will be used throughout this class
        self.size=0
        self.nrWords=0
        self.nrLetters=0

    # 'inherit' the method addWord from Node
    def addWord(self, word):
        self.nrWords=self.nrWords+1
        self.nrLetters=self.nrLetters+len(word)
        # adds the word to the Node root
        self.size=self.size+self.root.addWord(word)
        return True

    # 'inherit' the method hasWord from Node
    def hasWord(self, word):
        return self.root.hasWord(word)

    # print all information method
    def display(self):
        print(self.size)
        self.root.display()

    # getter method for size
    def getSize(self):
        return self.size

    # getter method for nrLetters
    def countLetters(self):
        return self.nrLetters

    # getter words for nrWords
    def countWords(self):
        return self.nrWords

    # compute compression
    def compression(self):
        return self.nrLetters/self.size

    # create graphviz Digraph
    # requires the python graphviz library!
    def diagram(self):
        from graphviz import Digraph
        from queue import Queue
        diagram=Digraph(comment='The Trie')

        i=0

        diagram.attr('node', shape='circle')
        diagram.node(str(i), self.root.getValue())

        q=Queue()
        q.put((self.root, i))
        
        while not q.empty():

            node, parent_index=q.get()

            for child in node.getChildren():
                i+=1
                if child.getEnding():
                    diagram.attr('node', shape='doublecircle')
                    diagram.node(str(i), child.getValue())
                    diagram.attr('node', shape='circle')
                else:
                    diagram.node(str(i), child.getValue())
                diagram.edge(str(parent_index), str(i))
                q.put((child, i))

        o=open('trie_dot.gv', 'w')
        o.write(diagram.source)
        o.close()
        diagram.render('trie_dot.gv', view=True)
        'trie_dot.gv.pdf'





class Node(object):
    """ any node in the Trie"""

    # empty constructor
    def __init__ (self, val):
        self.value=val
        self.children=[]
        self.ending=False
        self.di=0

    # toStr for a node will return it's value
    def __str__ (self):
        return str(self.value)

    # setter method for value
    def setValue(self, val):
        self.value=val
    
    # adds a child
    def add_child(self, child):
        self.children.append(child)

    # remove a child
    def rem_child(self, child):
        if self.contains_child(child):
            self.children.remove(child)

    # setter method for ending
    def setEnding(self, T_or_F):
        self.ending=T_or_F

    # check if a letter of interest is already a child
    def contains_child(self, letter):
        if letter in self.children:
            return True
        return False

    # getter method for value
    def getValue(self):
        return self.value

    # getter method for children
    def getChildren(self):
        return self.children

    # getter method for ending
    def getEnding(self):
        return self.ending

    def addWord(self, word):
        size_increment=0
        if word=='':
            self.setEnding(True)
            return size_increment # stops the recursion
        result=None
        for child in self.children:
            if child.value==word[0]:
                result=child
                return size_increment + result.addWord(word[1:])
        if result==None:
            new_child=Node(word[0])
            self.add_child(new_child)
            size_increment=size_increment+1
            return size_increment + new_child.addWord(word[1:])
        return size_increment

    # checks if word is in the Trie
    def hasWord(self, word):
        if word=='':
            if self.getEnding():
                return True
            else:
                return False
        for child in self.children:
            if child.value==word[0]:
                return True and child.hasWord(word[1:])
        return False

    # prints object
    def display(self):
        if self.getEnding():
            ending='#'
        else:
            ending=' '
        print(ending, self.value, ending)

        child_nodes=self.getChildren()
        for node in child_nodes:
            node.display()
        return True