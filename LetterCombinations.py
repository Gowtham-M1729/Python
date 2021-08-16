from itertools import product

class Solution:
    def letterCombinations(self, digits: str):
        if len(digits) == 0:
            return []
        l = ["", "", "abc", "def", 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        li = [l[int(i)] for i in digits]
        print(list(product(*li)))
        return [''.join(args) for args in product(*li)]
st=Solution()
print(st.letterCombinations("234"))
