# letters = ['a', 'b', 'd', 'e', 'i', 'j', 'o']
# letters = ('a', 'b', 'd', 'e', 'i', 'j', 'o')
letters = {'a', 'b', 'd', 'e', 'i', 'j', 'o'}
# Filter vowels - a, e, i, o, u

def filter_vowel(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return letter in vowels

vowel_filter_list = filter(filter_vowel, letters)
# print(list(vowel_filter_list))
# print(tuple(vowel_filter_list))
print(set(vowel_filter_list))