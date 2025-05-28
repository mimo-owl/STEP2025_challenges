'''
This program runs in approximately 15 seconds for the large test case.
'''

from collections import defaultdict, Counter

def find_anagram(word, anagram_map):
    sorted_word = ''.join(sorted(word.strip()))
    letter_dict = Counter(sorted_word)

    for sorted_key, word_list in anagram_map.items():
        dict_letters = Counter(sorted_key)
        # check if the letters in the sorted word can be formed with the letters in the dictionary word
        if all(dict_letters[char] <= letter_dict.get(char, 0) for char in dict_letters):
            return word_list[0] # can be [-1] as well


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

    # sort the anagram map by the score (in descending order)
    sorted_anagram_map = dict(
        sorted(anagram_map.items(), key=lambda item: cal_score(item[0]), reverse=True)
    )

    # for key, words in list(sorted_anagram_map.items())[:5]:
    #     print(f"{key}: {words}")


    # read test cases
    with open('large.txt', 'r') as file:
        for line in file:
            word = line.strip()
            # find an anagram with the maximum score
            max_score_anagram = find_anagram(word, sorted_anagram_map)
            max_score_anagrams.append(max_score_anagram)

    # write results to the output file
    out_file_name = 'large_answer2.txt'
    with open(out_file_name, 'w') as output_file:
        for anagram in max_score_anagrams:
            output_file.write(anagram + '\n')
    print(f"Max score anagrams written to {out_file_name}")

main()

