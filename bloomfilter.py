import math
import sys

M = 216091  # M-31th Mersen's number


# def get_comand():
#     for line in sys.stdin:
#         if 'set_size ' in line:
#             # global ss
#             # s=line.replace("set_size ", '')[:-1]
#             if line.replace("set_size ", '')[:-1].isnumeric() and ss == 0:
#                 NewStack = MyStack(int(line[9:]))
#                 ss = 1
#             else:
#                 print('error')
#         elif 'push' in line:
#             if len(line.replace('push', '').strip().split(
#                     ' ')) == 1 and ss != 0:  # line.replace('push ', '')[:-1] != 1 and ss != 0:
#                 print(NewStack.push(line[5:].rstrip()), end='')
#             else:
#                 print('error')
#         elif 'pop' in line:
#             if line.replace("pop", '') != '\n' or ss == 0:
#                 print('error')
#             else:
#                 print(NewStack.pop())
#         elif 'print' in line:
#             if line.replace("print", '') != '\n' or ss == 0:
#                 print('error')
#             else:
#                 print(NewStack.print(), end='')
#         elif line == '\n':
#             continue
#         else:
#             print('error')


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
        print(str(self.m) + ' ' + str(self.num_hashes))

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
                return '0'
        return '1'

    def print(self):
        for i in range(self.m - len(bin(self.bits)[2:])):
            print('0', end='')
        print(bin(self.bits)[:1:-1])


a = BloomFilter(2, 0.250)

a.add(7)
a.add(5)
a.add(14)
a.print()
print(a.search(7))
print(a.search(10))
print(a.search(15))
print(a.search(14))
print(a.search(5))
print(a.search(13))
