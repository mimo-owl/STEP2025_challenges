from collections import defaultdict

def find_anagram(word, anagram_map):
    sorted_word = ''.join(sorted(word.strip()))
    found_anagrams = []
    for dict_word in anagram_map:
        l, r = 0, len(anagram_map) - 1
        while l <= r:
            mid = (l + r) // 2
            if anagram_map[mid][0] == sorted_word:
                return anagram_map[mid][1]
            elif sorted_word < anagram_map[mid][0]:
                r = mid - 1
            else:
                l = mid + 1

def main():
    # make a map of sorted letters to original words
    anagram_map = defaultdict(list)
    with open('../words.txt', 'r') as dictionary:
        for word in dictionary:
            sorted_word = ''.join(sorted(word.strip()))
            anagram_map[sorted_word].append(word.strip())

    anagram_map = sorted(anagram_map.items(), key=lambda x: x[0])

    # for key, words in anagram_map[:5]:
    #     print(f"{key}: {words}")

    # read test cases
    with open('test_cases.txt', 'r') as file:
        for line in file:
            word = line.strip()
            print(find_anagram(word, anagram_map))

main()
