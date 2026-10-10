# Word Frequency Counter
def word_frequency(sentence):
    freq = {}
    for word in sentence.lower().split():
        freq[word] = freq.get(word, 0) + 1
    return freq


# Tests
print(word_frequency("the cat and the dog"))  
print(word_frequency("Hello hello HELLO"))     
print(word_frequency(""))                      