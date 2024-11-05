import pathlib

my_path_input = pathlib.Path('.', 'exc', 'alice_in_wonderland_ch_1.txt')
my_path_output = pathlib.Path('.', 'exc', 'output_statistics.txt')


vowels = set('aeiou')

with open(my_path_input, mode='r', encoding='utf-8') as alice_file:

    all_lines = alice_file.readlines()

    word_count = 0
    vowels_count = 0
    consonant_count = 0

    for line in all_lines:

        word_count += len(line.split(' '))
        list_per_line = line.split('\n')

        for word in list_per_line:

            for c in word:
                if c.lower() in vowels:
                    vowels_count += 1
                elif c not in vowels and c.isalpha():
                    consonant_count += 1
print(vowels_count, consonant_count, word_count)


with open(my_path_output, mode='w', encoding='utf-8') as output_file:
    output_file.write(f"Number of vowels: {vowels_count}\n")
    output_file.write(f"Number of consonants: {consonant_count}\n")
    output_file.write(f"Number of words: {word_count}\n")
