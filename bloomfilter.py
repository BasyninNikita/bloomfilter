import math
import sys

M = 216091  # M-31th Mersen's number


def get_command():
    ss = False
    for line in sys.stdin:
        if 'set' in line:
            if len(line.replace('set', '').strip().split(' ')) == 2 \
                    and ss == 0 and int(line.split()[1]) > 1 and float(line.split()[2]) < 0.7:  # line
                # .replace('push ', '')[:-1] != 1 and ss != 0:
                bf = BloomFilter(int(line.split()[1]), float(line.split()[2]))
                print(str(bf.size()) + ' ' + str(bf.num_hashs()))
                ss = True
            else:
                print('error')
        elif 'add' in line:
            if len(line.replace('add', '').strip().split(
                    ' ')) == 1 and ss :  # line.replace('push ', '')[:-1] != 1 and ss != 0:
                bf.add(int(line.split()[1]))
                print('', end='')
            else:
                print('error')
        elif 'search' in line:
            if len(line.replace('search', '').strip().split(
                    ' ')) == 1 and ss :  # line.replace('push ', '')[:-1] != 1 and ss != 0:
                print(bf.search(int(line.split()[1])), end='')
            else:
                print('error')
        elif 'print' in line:
            if line.replace("print", '') != '\n' or ss == False:
                print('error')
            else:
                print(bf.print(), end='')
        elif line == '\n':
            continue
        else:
            print('error')


def bit_sieve(n):
    if n < 2:
        return []
    bits = [1] * n
    sqrt_n = int(math.sqrt(n)) + 1
    for i in range(2, sqrt_n):
        if bits[i - 2]:
            for j in range(i + i, n + 1, i):
                bits[j - 2] = 0
    return bits


def prime(k):
    if k == 1:
        return 2
    sieve = bit_sieve(int(1.5 * k * math.log(k)) + 1)
    i = 0
    while k:
        k -= sieve[i]
        i += 1
    return (i + 1)


class BloomFilter:

    def __init__(self, n, P):
        self.n = n
        self.P = P
        self.num_hashes = round(-(math.log2(P)))
        self.m = round(- (n * math.log2(P)) / math.log(2))
        self.bits = 0
        # print(str(self.m) + ' ' + str(self.num_hashes))

    def size(self):
        return self.m

    def num_hashs(self):
        return self.num_hashes

    def hashes(self, key):
        hashs = list()  # (((i + 1)*x + pi+1) mod M) mod m ne pi,a p i+1-oe
        for i in range(self.num_hashes):
            hashs.append((((i + 1) * key + prime(i + 1)) % M) % self.m)  # M-31th Mersen's number
        return hashs

    def add(self, key):
        for i in self.hashes(key):
            self.bits = self.bits | 2 ** i

    def search(self, key):
        for i in self.hashes(key):
            if (self.bits & 2 ** i) == 0:
                return '0\n'
        return '1\n'

    def print(self):
        s = ''
        # for i in range(self.m - len(bin(self.bits)[2:])):
        #     s += ('0')
        s += '0' * (self.m - len(bin(self.bits)[2:]))
        s += (bin(self.bits)[:1:-1]) + '\n'
        return s


get_command()

