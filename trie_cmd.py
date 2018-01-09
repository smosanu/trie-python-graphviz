from trie_oop import *

trie = Trie()

file_in = 'top5000.txt'
f = open(file_in)
for line in f:
    trie.addWord(line.strip())
f.close()

searched_word = 'nationwide'
print('foud "', searched_word, '":', trie.hasWord(searched_word))
searched_word = 'statistical'
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
trie.diagram('top5000', True)
