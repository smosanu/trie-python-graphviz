from trie_oop import *
import random

trie=Trie()

file_in='words_linux.txt'
f=open(file_in)
cnt=0
for line in f:
	line=line.strip()
	trie.addWord(line)
	cnt+=1
f.close()

trie.display()

print('#words:',trie.countWords())
print('size:',trie.getSize())
print('#letters:',trie.countLetters())
print('compression:',trie.compression())

trie.diagram()