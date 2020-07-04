__all__ = ['BloomFilter']

class BitBloomFilter(object):
    def __init__(self, m=1024, k=3):
        self.m = m
        self.k = k
        self.items = [0] * m

    def __repr__(self):
        return '<BloomFilter {}>'.format(self.items)

    def add(self, item):
        h = hash(item)

        for i in range(self.k):
            p = (h >> i) % self.m
            self.items[p] = 1

    def remove(self, item):
        h = hash(item)

        for i in range(self.k):
            p = (h >> i) % self.m
            self.items[p] = 0

    def has(self, item):
        h = hash(item)

        for i in range(self.k):
            p = (h >> i) % self.m
            
            if not self.items[p]:
                return False

        return True

class IntBloomFilter(object):
    def __init__(self, m=1024, k=3):
        self.m = m
        self.k = k
        self.items = [0] * m

    def __repr__(self):
        return '<BloomFilter {}>'.format(self.items)

    def add(self, item):
        h = hash(item)

        for i in range(self.k):
            p = (h >> i) % self.m
            self.items[p] += 1

    def remove(self, item):
        h = hash(item)

        for i in range(self.k):
            p = (h >> i) % self.m
            
            if not self.items[p]:
                raise ValueError('Bloom filter\'s field is ZERO. This item was not added before.')

            self.items[p] -= 1

    def has(self, item):
        h = hash(item)

        for i in range(self.k):
            p = (h >> i) % self.m
            
            if not self.items[p]:
                return False

        return True

if __name__ == '__main__':
    # bit
    bf = BitBloomFilter(16)
    bf.add((1, '1'))
    bf.add((2, '2'))
    print(bf)
    print(bf.has((0, '0')))
    print(bf.has((1, '1')))

    # int
    bf = IntBloomFilter(16)
    bf.add((1, '1'))
    bf.add((2, '2'))
    print(bf)
    print(bf.has((0, '0')))
    print(bf.has((1, '1')))
