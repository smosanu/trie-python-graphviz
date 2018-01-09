class Trie(object):
    """ root node """

    # empty constructor
    def __init__(self):
        self.root = Node('*')
        self.nrWords = 0
        self.nrLetters = 0
        self.size = 0

    # 'inherit' the method addWord from Node
    def addWord(self, word):
        self.nrWords = self.nrWords + 1
        self.nrLetters = self.nrLetters + len(word)
        self.size = self.size + self.root.addWord(word)
        return True

    # 'inherit' the method hasWord from Node
    def hasWord(self, word):
        return self.root.hasWord(word)

    # print all information method
    def display(self):
        # print(self.size)
        self.root.display()

    # getter words for nrWords
    def countWords(self):
        return self.nrWords

    # getter method for nrLetters
    def countLetters(self):
        return self.nrLetters

    # getter method for size
    def getSize(self):
        return self.size

    # compute compression
    def compression(self):
        return self.nrLetters / self.size

    # create graphviz Digraph
    def diagram(self, filename, render):
        from graphviz import Digraph
        from queue import Queue
        diagram = Digraph(comment='The Trie')

        i = 0

        diagram.attr('node', fontsize='4')
        diagram.attr('node', height='0.1')
        diagram.attr('node', width='0.1')
        diagram.attr('node', fixedsize='true')
        diagram.attr('node', shape='circle')
        diagram.attr('edge', arrowsize='0.3')
        diagram.node(str(i), self.root.getValue())

        q = Queue()
        q.put((self.root, i))

        while not q.empty():

            node, parent_index = q.get()

            for child in node.getChildren():
                #print('current parent: ', node.getValue(), parent_index)
                i += 1
                #print('current child: ', child.getValue(), i)
                if child.getEnding():
                    diagram.attr('node', shape='diamond')
                    diagram.node(str(i), child.getValue())
                    diagram.attr('node', shape='circle')
                else:
                    diagram.node(str(i), child.getValue())
                diagram.edge(str(parent_index), str(i))
                q.put((child, i))

        o = open(filename + '.gv', 'w')
        o.write(diagram.source)
        # print(diagram.source)
        if render:
            diagram.render(filename + '.gv', view=False)
        o.close()


class Node(object):
    """ any node """

    # empty constructor
    def __init__(self, val):
        self.value = val
        self.children = []
        self.ending = False

    def __str__(self):
        return str(self.value)

    # setter method for value
    def setValue(self, val):
        self.value = val

    # adds a child
    def add_child(self, child):
        self.children.append(child)

    # remove a child
    def rem_child(self, child):
        if self.contains_child(child):
            self.children.remove(child)

    # setter method for ending
    def setEnding(self, T_or_F):
        self.ending = T_or_F

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
        size_increment = 0
        if word == '':
            self.setEnding(True)
            return size_increment  # stops the recursion
        result = None
        for child in self.children:
            if child.value == word[0]:
                result = child
                return size_increment + result.addWord(word[1:])
        if result == None:
            new_child = Node(word[0])
            self.add_child(new_child)
            size_increment = size_increment + 1
            return size_increment + new_child.addWord(word[1:])
        return size_increment

    # checks if word is in the Trie
    def hasWord(self, word):
        if word == '':
            if self.getEnding():
                return True
            else:
                return False
        for child in self.children:
            # print(child.value)
            if child.value == word[0]:
                return True and child.hasWord(word[1:])
        return False

    # prints object
    def display(self):
        if self.getEnding():
            ending = '_'
        else:
            ending = ' '
        print(ending, self.value, ending)

        child_nodes = self.getChildren()
        for node in child_nodes:
            node.display()

        return True
