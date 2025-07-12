'''
Execution example: python wikipedia.py pages.txt links.txt
'''

import sys
import collections
from collections import deque, defaultdict

class Wikipedia:

    # Initialize the graph of pages.
    def __init__(self, pages_file, links_file):

        # A mapping from a page ID (integer) to the page title.
        # For example, self.titles[1234] returns the title of the page whose
        # ID is 1234.
        self.titles = {}

        # A set of page links.
        # For example, self.links[1234] returns an array of page IDs linked
        # from the page whose ID is 1234.
        self.links = {}

        # Read the pages file into self.titles.
        with open(pages_file) as file:
            for line in file:
                (id, title) = line.rstrip().split(" ")
                id = int(id)
                assert not id in self.titles, id
                self.titles[id] = title
                self.links[id] = []
        print("Finished reading %s" % pages_file)

        # Read the links file into self.links.
        with open(links_file) as file:
            for line in file:
                (src, dst) = line.rstrip().split(" ")
                (src, dst) = (int(src), int(dst))
                assert src in self.titles, src
                assert dst in self.titles, dst
                self.links[src].append(dst)
        print("Finished reading %s" % links_file)
        print()


    # Example: Find the longest titles.
    def find_longest_titles(self):
        titles = sorted(self.titles.values(), key=len, reverse=True)
        print("The longest titles are:")
        count = 0
        index = 0
        while count < 15 and index < len(titles):
            if titles[index].find("_") == -1:
                print(titles[index])
                count += 1
            index += 1
        print()


    # Example: Find the most linked pages.
    def find_most_linked_pages(self):
        link_count = {}
        for id in self.titles.keys():
            link_count[id] = 0

        for id in self.titles.keys():
            for dst in self.links[id]:
                link_count[dst] += 1

        print("The most linked pages are:")
        link_count_max = max(link_count.values())
        for dst in link_count.keys():
            if link_count[dst] == link_count_max:
                print(self.titles[dst], link_count_max)
        print()

    def convert_id2word(self, id):
        word = self.titles[id]
        return str(word)

    def convert_word2id(self, word):
        for id, title in self.titles.items():
            if title == word:
                return id

    # Homework #1: Find the shortest path.
    # 'start': A title of the start page.
    # 'goal': A title of the goal page.
    def find_shortest_path(self, start, goal):
        #------------------------#
        # Write your code here!  #
        #------------------------#
        print("find_shortest_path")
        start_id = self.convert_word2id(start)
        goal_id = self.convert_word2id(goal)
        print(start_id, goal_id)
        queue = deque()
        visited = {}
        parent = {}
        queue.append(start_id)
        visited[start_id] = True

        while queue:
            # BFS
            node = queue.popleft()
            visited[node] = True
            if node == goal_id:
                path = self.convert_id2word(node)
                # 最短経路でゴールに辿りついたら、ゴールから親を辿り最短経路を求める
                while node != start_id:
                    parent_of_node = parent[node]
                    parent_word = self.convert_id2word(parent_of_node)
                    # print(f"parent_word: {parent_word}")
                    # print(f"path: {path}")
                    path = str(parent_word + "->" + path)
                    node = parent_of_node
                print(f"見つかった最短経路：{path}")
                return

            for child in self.links[node]:
                if not child in visited:
                    # 親ノードを記憶しておく
                    parent[child] = node
                    queue.append(child)
                    visited[child] = True

        print("経路が見つかりませんでした。")


    # Homework #2: Calculate the page ranks and print the most popular pages.
    def find_most_popular_pages(self):
        #------------------------#
        # Write your code here!  #
        #------------------------#
        # max_iters = 100
        threshold = 0.01
        damping = 0.85
        num_nodes = len(self.links)
        total_diff = float('inf')
        # step1:全部のノードに初期値 1.0 を与える
        ranks = {node: 1.0 for node in self.links}

        # ページランクの更新（total_diff）が収束するまで更新を実行
        while total_diff >= threshold:
            total_diff = 0.0
            # step2: 各ノードのページランクを隣接ノードに均等に振り分ける
            # step3: 各ノードのページランクを、受け取ったページランクの合計値に更新する
            new_ranks = defaultdict(float)
            for node, neighbors in self.links.items():
                # 隣接ノードがある場合
                if neighbors:
                    # 85% をリンク先に均等分配
                    share_85 = ranks[node] * damping / len(neighbors)
                    for neighbor in neighbors:
                        new_ranks[neighbor] += share_85
                    # 残り 15% を全ノードに均等分配
                    share_15 = ranks[node] * (1 - damping) / num_nodes
                    for n in self.links:
                        new_ranks[n] += share_15
                # 隣接ノードがない場合
                else:
                    # 100% を全ノードに均等分配
                    share = ranks[node] / num_nodes
                    for n in self.links:
                        new_ranks[n] += share

            for node in self.links:
                total_diff += (new_ranks[node] - ranks[node]) ** 2
            ranks = new_ranks

            # rankの合計値が一定になっていることを確認
            total_rank = sum(ranks.values())
            print(f"Total PageRank: {total_rank:.4f}")

            if total_diff < threshold:
                break

        # 上位10件を表示
        top_pages = sorted(ranks.items(), key=lambda x: x[1], reverse=True)[:10]
        print("Top 10 pages by PageRank:")
        for rank, (node, score) in enumerate(top_pages, 1):
            print(f"{rank}. Node {node}, Word {self.convert_id2word(node)} - PageRank: {score:.6f}")


    # Homework #3 (optional):
    # Search the longest path with heuristics.
    # 'start': A title of the start page.
    # 'goal': A title of the goal page.
    def find_longest_path(self, start, goal):
        #------------------------#
        # Write your code here!  #
        #------------------------#
        print("find_longest_path")
        start_id = self.convert_word2id(start)
        goal_id = self.convert_word2id(goal)
        print(start_id, goal_id)
        queue = deque()
        visited = {}
        parent = {}
        queue.append(start_id)
        visited[start_id] = True

        while queue:
            # BFS
            node = queue.popleft()
            visited[node] = True
            if node == goal_id:
                path = self.convert_id2word(node)
                # 最短経路でゴールに辿りついたら、ゴールから親を辿り最短経路を求める
                while node != start_id:
                    parent_of_node = parent[node]
                    parent_word = self.convert_id2word(parent_of_node)
                    # print(f"parent_word: {parent_word}")
                    # print(f"path: {path}")
                    path = str(parent_word + "->" + path)
                    node = parent_of_node
                print(f"見つかった最短経路：{path}")
                return

            for child in self.links[node]:
                if not child in visited:
                    # 親ノードを記憶しておく
                    parent[child] = node
                    queue.append(child)
                    visited[child] = True

        print("経路が見つかりませんでした。")


    # Helper function for Homework #3:
    # Please use this function to check if the found path is well formed.
    # 'path': An array of page IDs that stores the found path.
    #     path[0] is the start page. path[-1] is the goal page.
    #     path[0] -> path[1] -> ... -> path[-1] is the path from the start
    #     page to the goal page.
    # 'start': A title of the start page.
    # 'goal': A title of the goal page.
    def assert_path(self, path, start, goal):
        assert(start != goal)
        assert(len(path) >= 2)
        assert(self.titles[path[0]] == start)
        assert(self.titles[path[-1]] == goal)
        for i in range(len(path) - 1):
            assert(path[i + 1] in self.links[path[i]])


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("usage: %s pages_file links_file" % sys.argv[0])
        exit(1)

    wikipedia = Wikipedia(sys.argv[1], sys.argv[2])
    # Example
    # wikipedia.find_longest_titles()
    # Example
    # wikipedia.find_most_linked_pages()
    # Homework #1
    wikipedia.find_shortest_path("渋谷", "パレートの法則")
    # wikipedia.find_shortest_path("A", "E")
    # Homework #2
    wikipedia.find_most_popular_pages()
    # Homework #3 (optional)
    wikipedia.find_longest_path("渋谷", "池袋")
