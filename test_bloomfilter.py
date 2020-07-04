import time
import unittest

from bloomfilter import BitBloomFilter, IntBloomFilter

class TestBitBloomFilter(unittest.TestCase):
    def test_one_million_writes(self):
        bf = BitBloomFilter(10 ** 6)
        t = time.time()

        for i in range(10 ** 6):
            bf.add(i)

        print('took {} seconds'.format(time.time() - t))

    def test_one_million_writes_and_reads(self):
        bf = BitBloomFilter(10 ** 6)
        t = time.time()

        for i in range(10 ** 6):
            bf.add(i)

        for i in range(10 ** 6):
            if not bf.has(i):
                raise ValueError('missing {}'.format(repr(i)))

        print('took {} seconds'.format(time.time() - t))

    def test_one_million_reads(self):
        bf = BitBloomFilter(10 ** 6)
        
        for i in range(10 ** 6):
            bf.add(i)

        t = time.time()

        for i in range(10 ** 6):
            if not bf.has(i):
                raise ValueError('missing {}'.format(repr(i)))

        print('took {} seconds'.format(time.time() - t))


class TestIntBloomFilter(unittest.TestCase):
    def test_one_million_writes(self):
        bf = IntBloomFilter(10 ** 6)
        t = time.time()

        for i in range(10 ** 6):
            bf.add(i)

        print('took {} seconds'.format(time.time() - t))

    def test_one_million_writes_and_reads(self):
        bf = IntBloomFilter(10 ** 6)
        t = time.time()

        for i in range(10 ** 6):
            bf.add(i)

        for i in range(10 ** 6):
            if not bf.has(i):
                raise ValueError('missing {}'.format(repr(i)))

        print('took {} seconds'.format(time.time() - t))

    def test_one_million_reads(self):
        bf = IntBloomFilter(10 ** 6)
        
        for i in range(10 ** 6):
            bf.add(i)

        t = time.time()

        for i in range(10 ** 6):
            if not bf.has(i):
                raise ValueError('missing {}'.format(repr(i)))

        print('took {} seconds'.format(time.time() - t))

if __name__ == '__main__':
    unittest.main()
