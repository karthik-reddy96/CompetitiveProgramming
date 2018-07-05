import unittest

class QueueTwoStacks(object):

    # Implement the enqueue and dequeue methods
    def __init__(self):
        self.stack1=[]
        self.stack2=[]

    def enqueue(self, item):
        self.stack1.append(item)
        
    def dequeue(self):
        if len(self.stack1)==0 and len(self.stack2)==0:
            raise IndexError("except")
        if len(self.stack2)==0:
            while (len(self.stack1)!=0):
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()


















# Tests

class Test(unittest.TestCase):

    def test_queue_usage(self):
        queue = QueueTwoStacks()

        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        actual = queue.dequeue()
        expected = 1
        self.assertEqual(actual, expected)

        actual = queue.dequeue()
        expected = 2
        self.assertEqual(actual, expected)

        queue.enqueue(4)

        actual = queue.dequeue()
        expected = 3
        self.assertEqual(actual, expected)

        actual = queue.dequeue()
        expected = 4
        self.assertEqual(actual, expected)

        with self.assertRaises(Exception):
            queue.dequeue()


unittest.main(verbosity=2)