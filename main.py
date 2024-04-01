import hashlib
from itertools import permutations

def find_hash(original_hash):
    word_file = open("words.txt","r")
    word_file = list(word_file)

    anagram = "i move lads"
    words = anagram.count(' ')
    words += 1

    char_list = list(set(anagram))

    if ' ' in char_list:
        char_list.remove(' ')

    final_words = []

    for i in word_file:
        flag = False # assuming that the characters of the words exist in the characters of the anagram
        temp_word = i.replace('\n', '')
        temp_char = list(set(temp_word))

        for j in temp_char:
            # setting flag to True if the letter is NOT present in the anagram
            if j not in char_list:
                flag = True
                break
        # appending the words containing the anagram's letters to save time
        if flag is False:
            final_words.append(temp_word)

    print(len(final_words))

    for elem in permutations(final_words, words):
        hash_elem = " ".join(elem)
        
        # checking if message length = anagram length
        # if not, then this combo can't be the message
        if len(hash_elem) != len(anagram):
            continue
        
        m = hashlib.md5()
        m.update(hash_elem.encode('utf-8'))
        word_hash = m.hexdigest()

        if word_hash == original_hash:
            return hash_elem

hash = '149ea698c08e57a5b9c41447ecbcd9cf'
answer = find_hash(hash)
print(f"The word corresponding to the given hash is '{answer}'")