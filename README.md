# STEP2025_challenges

## Week 1: Anagram
### Challenge 1
Create a program that searches for anagrams of a given string from a dictionary file and returns all found anagrams.
Make your own test cases to verify it.

### Challenge 2
Upgrade the function so that it does not require using all characters from the given string.

Input: small.txt, medium.txt, large.txt
Output: A file that lists, for each word, the anagram with the highest score.

## Week2: Data structure & algorithm 1
#### Content: Time / space complexity, Tree, Hash table

## Challenge 1
Implement a hash table from scratch \(Implement Python's dictionary from scratch" \)

Hint 1: Implement delete(key)
Hint 2: Implement rehashing
Hint 3: Improve the hash function
The goal is to make the hash table work with mostly O(1) without depending on the number of items in the hash table.

## Challenge 2
The complexity of searching / adding / removing an element is mostly O(1) with a hash table, whereas the complexity is O(log N) with a tree. This means that a hash table is more efficient than a tree. However, real-world large-scale database systems tend to prefer a tree to a hash table. Why? List as many reasons as possible.

## (Extra:) QUIZ!
Does a data structure exist such that...
You can insert/remove/search in O(1)?

## Challenge 3
Design a cache that achieves the following operations with mostly O(1)
When a pair of \< URL, Web page \> is given, find if the given pair is contained in the cache or not
If the pair is not found, insert the pair into the cache after evicting the least recently accessed pair

## (Extra:) Challenge 4
Implement the cache.

The goal is to implement the data structure yourself without using any existing libraries (e.g., collections.*)
Use the HashTable you implemented in Homework 1

## Week3:

## Challenge 1
### 問題<br>
モジュール化されたプログラムを変更して、「*」「/」に対応しよう<br>
例： 3.0 + 4 * 2 − 1 / 5<br>
不正な入力はないと仮定してよい<br>
細かい仕様は好きに定義してください<br>

## Challenge 2
## 問題<br>
書いたプログラムが正しく動いていることを確認するためのテストケースを追加しよう<br>
できるだけ網羅的に<br>

## Challenge 3
## 問題<br>
括弧に対応しよう<br>
例:  (3.0 + 4 * (2 − 1)) / 5<br>
テストケースも追加してください<br>
いろいろな解き方があります（5 種類以上）<br>

## Challenge 4
## 問題<br>
abs(), int(), round() に対応しよう<br>
abs(-2.2) => 2.2 （絶対値）<br>
int(1.55) => 1（小数を切捨てる）<br>
round(1.55) => 2（四捨五入）<br>

テストケースも追加してください <br>
例: 12 + abs(int(round(-1.55) + abs(int(-2.3 + 4)))) <br>
