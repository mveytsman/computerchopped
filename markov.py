import nltk
import random
f = open("salads.txt")
s = f.read()
def get_next_word(freq, uniqs):
    if not freq:
        print "cache missmsb"
        return random.choice(uniqs)
    rand = random.random() # 0.3419402677707398
    cur = 0
    idx = 0
    while cur < rand:
        cur += freq[idx]
        idx += 1
    return uniqs[idx]

def generate_text(corpus):
    tokens = nltk.word_tokenize(s)
    trigrams = [tokens[i:i+3] for i in range(len(tokens) - 2)]
    uniqs = list(set(tokens))
    indexes = {} 
    for i, u in enumerate(uniqs):
        indexes[u] = i

    freqs = {}

    print "generating freqs"
    for (a,b,c) in trigrams:
        if not freqs.get((a,b)):
            freqs[(a,b)] = [0] * len(uniqs)
        freqs[(a,b)][indexes[c]] += 1

    for key, freq in freqs.iteritems():
        freq_sum = sum(freq)
        freqs[key] = [n / freq_sum for n in freq]

    word, word2 = random.choice(freqs.keys())

    while True:
        yield word2
        word, word2 = word2, get_next_word(freqs.get((word, word2)), uniqs)
