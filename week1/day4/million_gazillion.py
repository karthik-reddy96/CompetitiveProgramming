import unittest
 
class TrieNode:
    def __init__(self):
        self.child = [None]*26
        self.is_endWord = False
 
class Trie(object):
    def __init__(self):
        self.root = self.getNode()
 
    def getNode(self):
        return TrieNode()
 
    def toIndex(self,ch):
        return ord(ch)-ord('a')
 
 
    def add_word(self,key):
        if self.search(key):
            return False
        else:
            pCrawl = self.root
            length = len(key)
            for level in range(length):
                index = self.toIndex(key[level])
                if not pCrawl.child[index]:
                    pCrawl.child[index] = self.getNode()
                pCrawl = pCrawl.child[index]
            pCrawl.is_endWord = True
            return True
            
    def search(self, key):
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self.toIndex(key[level])
            if not pCrawl.child[index]:
                return False
            pCrawl = pCrawl.child[index] 
        return pCrawl != None and pCrawl.is_endWord


# Tests

class Test(unittest.TestCase):

    def test_trie_usage(self):
        trie = Trie()

        result = trie.add_word('catch')
        self.assertTrue(result, msg='new word 1')

        result = trie.add_word('cakes')
        self.assertTrue(result, msg='new word 2')

        result = trie.add_word('cake')
        self.assertTrue(result, msg='prefix of existing word')

        result = trie.add_word('cake')
        self.assertFalse(result, msg='word already present')

        result = trie.add_word('caked')
        self.assertTrue(result, msg='new word 3')

        result = trie.add_word('catch')
        self.assertFalse(result, msg='all words still present')

        result = trie.add_word('')
        self.assertTrue(result, msg='empty word')

        result = trie.add_word('')
        self.assertFalse(result, msg='empty word present')


unittest.main(verbosity=2)
