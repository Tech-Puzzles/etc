from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp=[False]*(len(s)+1)
        dp2=[0]*(len(s)+1)
        print('tracking',dp)
        dp[0]=True
        print('tracking',dp)
        for i in range(1,len(s)+1):
            for j in range(0,i):
                print('iterate', s[j:i])
                print('test','j',j,'i',i,dp[j] , s[j:i] , 'in', wordDict, s[j:i] in wordDict)
                print('lookat', s[j:i], s[j:i] in wordDict)
                print('is back item true', dp[j], 'j',j, 'i',i)
                if dp[j] and s[j:i] in wordDict:
                    dp[i]=True
                    dp2[i]=1
                print('tracking',dp2)
        return dp[-1]                

    def wordBreak2(self, s: str, wordDict: List[str]) -> bool:
        queue=[]
        start=0
        queue.append((0,wordDict))
        for startitem in queue:
        # while start < len(s):
                print('startitem',startitem,s[start:])
                wordDict=startitem[1]
                start=startitem[0]
                for item in range(len(wordDict)):
                    print('item',wordDict[item])
                    if wordDict[item] == s[start:start+len(wordDict[item])]:
                        print('found',wordDict[item])
                        print('copy',wordDict.copy())
                        #print('remove',wordDict.copy())
                        dict=wordDict.copy()
                        #dict.remove(wordDict[item])
                        queue.append((start+len(wordDict[item]),dict))
            
            
                
test=Solution()
#print(test.wordBreak("catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]))
#print(test.wordBreak2("catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]))
#print(test.wordBreak2("catsanddog", wordDict = ["cats", "dog", "sand", "and", "cat"]))
#print(test.wordBreak2("leetcode",  ["leet","code"]))
# print(test.wordBreak2( "bb", ["a","b","bbb","bbbb"]))
# print(test.wordBreak2("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]))
# print(test.wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]))
# print(test.wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", ["a"]))
# print(test.wordBreak("aaaab", ["a"]))
# print(test.wordBreak("axaxx", ["a"]))
#print(test.wordBreak("abc", ["a","abc"]))
print(test.wordBreak("abcde", ["a","abc"]))
