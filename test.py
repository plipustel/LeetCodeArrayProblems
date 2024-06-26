class Solution(object):
    def maxScoreWords(self, words, letters, score):
        """
        :type words: List[str]
        :type letters: List[str]
        :type score: List[int]
        :rtype: int
        """
        #sort
        sort = sorted(letters)
        c_score =[s for s in score if s != 0]
        c_letters = []
        
        c_sc = {}
        c_words = []
        
        c_length_words = []
        
        cur_str = ''
    
        for i in range(len(sort)):
            if sort[i] not in c_letters:
                c_letters.append(sort[i])
                
        for i in range(len(c_letters)):
            c_sc[c_letters[i]] = c_score[i]
        
        for i in range(len(words)):
            if all(chars in c_letters for chars in words[i]):
                c_words.append(words[i])
        
        #print(c_words)
        for i in range(len(c_words)):
            cur_str = ''
            for j in range(i, len(c_words)):
                cur_str = cur_str + c_words[j]  
                c_length_words.append(cur_str)
        
        #print(letters)
        #print(c_length_words)
        
        final_scores = []
        count = 0
        for w in range(len(c_length_words)):
           # print(c_length_words[w])
            for char in letters:
                #if char in c_length_words[w]:
                    char_in_words = c_length_words[w].count(char)
                    char_in_letters = letters.count(char)
                    if (char_in_words > char_in_letters) and (c_length_words[w] not in final_scores):
                        final_scores.append(c_length_words[w])
                    #print(char, letters.count(char), char_in_words)
                    
        #print(final_scores)
        result = [item for item in c_length_words if item not in final_scores]
        
        
        #print(c_sc)
        total = {}
        for i in range(len(result)):
            #print(result[i])
            res = 0
            for a in result[i]:
                res += c_sc[a]
                total[result[i]] = res
           
        if total:
            return max(total.values())
        else:
            return 0  
       
        
        
words = ["dog","cat","dad","good"]
letters = ["a","a","c","d","d","d","g","o","o"]
score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]

sol = Solution()
print(sol.maxScoreWords(words, letters, score))