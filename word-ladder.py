from collections import deque, defaultdict
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        # Step 1: Build the pattern adjacency list
        # e.g., "*ot": ["hot", "dot", "lot"]
        neighbors = defaultdict(list)
        wordList.append(beginWord)
        
        L = len(beginWord)
        for word in wordList:
            for j in range(L):
                pattern = word[:j] + "*" + word[j+1:]
                neighbors[pattern].append(word)

        # Step 2: BFS queue storing (current_word, level_length)
        queue = deque([(beginWord, 1)])
        visited = {beginWord}

        while queue:
            word, level = queue.popleft()

            if word == endWord:
                return level

            # Check all intermediate patterns of the current word
            for j in range(L):
                pattern = word[:j] + "*" + word[j+1:]
                for neighbor in neighbors[pattern]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, level + 1))
                # Clear pattern list to prevent duplicate scans
                neighbors[pattern] = []

        return 0