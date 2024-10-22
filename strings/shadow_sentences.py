def are_shadow_sentences(sentence1, sentence2):
    words1 = sentence1.split()
    words2 = sentence2.split()
    if (len(words1) != len(words2)):
        return False
    for word1, word2 in zip(words1, words2):

        if len(word1) != len(word2):
            return False

        if set(word1) & set(word2):
            return False
    return True


print(are_shadow_sentences("they are round", "fold two times"))
# Expected output: True

print(are_shadow_sentences("his friends", "our company"))
# Expected output: False

print(are_shadow_sentences("black coat", "funny pigs"))
# Expected output: True

print(are_shadow_sentences("short sentence", "longer text"))
# Expected output: False

print(are_shadow_sentences("code hard", "mash jump"))
# Expected output: True

print(are_shadow_sentences("blue bell", "bad luck"))
# Expected output: False

print(are_shadow_sentences("a b c", "x y z"))
# Expected output: True
