class Solution(object):
    def maxScoreWords(self, words, letters, score):
        """
        :type words: List[str]
        :type letters: List[str]
        :type score: List[int]
        :rtype: int
        """
        # Helper function to calculate the score of a word
        
        def word_score(word):
            return sum(score[ord(char) - ord('a')] for char in word)

        # Helper function to count the letters in a word
        def count_letters(word):
            counts = [0] * 26
            for char in word:
                counts[ord(char) - ord('a')] += 1
            return counts

        # Helper function to check if we can form a word with available letters
        def can_form(word_count, available_count):
            for i in range(26):
                if word_count[i] > available_count[i]:
                    return False
            return True

        # Recursive function to find the maximum score
        def find_max_score(index, available_count):
            if index == len(words):
                return 0

            # Option 1: Skip the current word
            max_score = find_max_score(index + 1, available_count)

            # Option 2: Include the current word (if possible)
            word = words[index]
            word_count = count_letters(word)

            if can_form(word_count, available_count):
                # Update the available count
                for i in range(26):
                    available_count[i] -= word_count[i]

                # Recur with the current word included
                max_score = max(max_score, word_score(word) + find_max_score(index + 1, available_count))

                # Backtrack the available count
                for i in range(26):
                    available_count[i] += word_count[i]

            return max_score

        # Initial letter count
        letter_count = [0] * 26
        for char in letters:
            letter_count[ord(char) - ord('a')] += 1

        return find_max_score(0, letter_count)

# Example Usage
solution = Solution()
words1 = ["dog", "cat", "dad", "good"]
letters1 = ["a", "a", "c", "d", "d", "d", "g", "o", "o"]
score1 = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]

print(solution.maxScoreWords(words1, letters1, score1))  # Output: 23

words2 = ["xxxz", "ax", "bx", "cx"]
letters2 = ["z", "a", "b", "c", "x", "x", "x"]
score2 = [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10]
#print(solution.maxScoreWords(words2, letters2, score2))  # Output: 27

words3 = ["leetcode"]
letters3 = ["l", "e", "t", "c", "o", "d"]
score3 = [0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0]
#print(solution.maxScoreWords(words3, letters3, score3))  # Output: 0
