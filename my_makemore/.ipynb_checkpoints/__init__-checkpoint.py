words = open('names.txt','r').read().splitlines()
print(words[:10])
print(len(words))

b = {}
for w in words:
    chs = ['<S>'] + list(w) + ['<E>']
    for ch1, ch2 in zip(chs, chs[1:]):
        bigram = (ch1,ch2)
        b[bigram] = b.get(bigram,0) + 1
print(sorted(b.items(), key = lambda kv: -kv[1]))

import torch
a = torch.zeros((3,5), dtype = torch.int32)
print(a)
a[1,3] += 1
print(a)
# create tensor to hold all the data 
N = torch.zeros((28,28), dtype = torch.int32)
# create lookup table to convert characters to integers to store into the tensor
chars = sorted(list(set(''.join(words)))) # created a sorted list of all the possible characters
stoi = {s:i for i,s in enumerate(chars)} # create a mapping of characters to integers
stoi['<S>'] = 26
stoi['<E>'] = 27
 
for w in words:
    chs = ['<S>'] + list(w) + ['<E>']
    for ch1, ch2 in zip(chs, chs[1:]):
        ix1 = stoi[ch1]
        ix2 = stoi[ch2]
        N[ix1,ix2] += 1

print(N)

import matplotlib.pyplot as plt 
