string = 'the quick brown fox jumps over the lazy dog the fox'

frequency = {}


def count_word_frequency(text):
    new_text = text.split(" ")
    for word in new_text:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1


count_word_frequency(string)
print(frequency)
