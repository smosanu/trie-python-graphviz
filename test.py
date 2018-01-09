from trie_oop import *

trie = Trie()

file_in = 'dict.txt'
f = open(file_in)
for line in f:
    trie.addWord(line.strip())
f.close()

trie.addWord('doughnut')
trie.addWord('donut')
trie.addWord('donald')
trie.addWord('domino')
trie.addWord('dominion')


searched_word = 'second'
print('foud "', searched_word, '":', trie.hasWord(searched_word))
searched_word = 'time'
print('foud "', searched_word, '":', trie.hasWord(searched_word))
searched_word = 'domino'
print('foud "', searched_word, '":', trie.hasWord(searched_word))
searched_word = 'dominique'
print('foud "', searched_word, '":', trie.hasWord(searched_word))

print()
print('#words:', trie.countWords())
print('size:', trie.getSize())
print('#letters:', trie.countLetters())
print('compression:', trie.compression())


print()
trie.display()
trie.diagram('test', True)
