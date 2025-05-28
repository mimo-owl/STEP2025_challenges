from collections import defaultdict

def find_anagram(word, anagram_map):
    sorted_word = ''.join(sorted(word.strip()))
    if sorted_word not in anagram_map:
        return False, None
    else:
        return True, anagram_map[sorted_word]

def main():
    # make a map of sorted letters to original words
    anagram_dict = {}
    with open('../words.txt', 'r') as dictionary:
        for word in dictionary:
            sorted_word = ''.join(sorted(word.strip()))

            if sorted_word not in anagram_dict:
                anagram_dict[sorted_word] = [word.strip()]
            else:
                anagram_dict[sorted_word].append(word.strip())

    # anagram_map = sorted(anagram_map.items(), key=lambda x: x[0])
    # print(anagram_map[:5])  # Print first 5 entries for debugging

    print(anagram_dict)

    # for key, words in anagram_map[:5]:
    #     print(f"{key}: {words}")

    # read test cases
    with open('test_cases.txt', 'r') as file:
        for line in file:
            word = line.strip()
            found, anagrams = find_anagram(word, anagram_dict)
            if found:
                print(f"Anagrams for '{word}': {anagrams}")
            else:
                print(f"No anagrams found for '{word}'.")


main()
