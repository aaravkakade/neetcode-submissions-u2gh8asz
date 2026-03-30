class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # create a list of 26 0s for each word
        #iterate through each letter, ascii of a - ascii of letter
        # increment respective spot in list by 1

        anagrams = defaultdict(list)

        for word in strs:
            freq = [0] * 26
            for char in word:
                freq[ord(char) - ord('a')] += 1

            anagrams[tuple(freq)].append(word)

        return list(anagrams.values())

         





