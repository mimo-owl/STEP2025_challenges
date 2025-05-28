'''
This program runs in approximately 1+ minute for the large test case.
'''

from collections import defaultdict, Counter

def find_anagram(word, anagram_map):
    sorted_word = ''.join(sorted(word.strip()))
    letter_dict = Counter(sorted_word)
    max_score = 0
    max_score_word = ''
    # print(anagram_map)


    for dict_letters, word_list in anagram_map:
        # check if the letters in the sorted word can be formed with the letters in the dictionary word
        if all(dict_letters[char] <= letter_dict.get(char, 0) for char in dict_letters):
            # see if the candidate word has the maximum score
            for candidate in word_list:
                cur_score = cal_score(candidate)
                if cur_score > max_score:
                    max_score = cur_score
                    max_score_word = candidate

    return max_score_word

        # l, r = 0, len(anagram_map) - 1
        # while l <= r:
        #     mid = (l + r) // 2
        #     if anagram_map[mid][0].keys() in letter_dict.keys():
        #         return anagram_map[mid][1]
        #     elif sorted_word < anagram_map[mid][0]:
        #         r = mid - 1
        #     else:
        #         l = mid + 1

# return score of the candidate word
def cal_score(word):
    score = 0
    scores_1 = {'a', 'e', 'h', 'i', 'n', 'o', 'r', 's', 't'}
    scores_2 = {'c', 'd', 'l', 'm', 'u'}
    scores_3 = {'b', 'f', 'g', 'p', 'v', 'w', 'y'}
    scores_4 = {'j', 'k', 'q', 'x', 'z'}
    for char in word:
        if char in scores_1:
            score += 1
        elif char in scores_2:
            score += 2
        elif char in scores_3:
            score += 3
        elif char in scores_4:
            score += 4
    return score

def main():
    max_score_anagrams = []
    # make a map of sorted letters to original words
    anagram_map = defaultdict(list)
    with open('../words.txt', 'r') as dictionary:
        for word in dictionary:
            sorted_word = ''.join(sorted(word.strip()))
            anagram_map[sorted_word].append(word.strip())

    anagram_map = sorted(anagram_map.items(), key=lambda x: x[0])

    # make a letter dictionary for each sorted word
    for i in range(len(anagram_map)):
        sorted_word, word_list = anagram_map[i]
        letter_dict = {}
        for char in sorted_word:
            if char not in letter_dict:
                letter_dict[char] = 1
            else:
                letter_dict[char] += 1
        print(letter_dict)
        anagram_map[i]  = (letter_dict, word_list)


    for key, words in anagram_map[:5]:
        print(f"{key}: {words}")

    # read test cases
    with open('large.txt', 'r') as file:
        for line in file:
            word = line.strip()
            max_score_anagram = find_anagram(word, anagram_map)
            max_score_anagrams.append(max_score_anagram)
            # print(find_anagram(word, anagram_map))

    # write results to the output file
    with open('large_answer.txt', 'w') as output_file:
        for anagram in max_score_anagrams:
            output_file.write(anagram + '\n')
    print("Max score anagrams written to max_score_anagrams.txt")

main()

