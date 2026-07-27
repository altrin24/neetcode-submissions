class Solution:
    def isPalindrome(self, s: str) -> bool:
        frSt =  "".join(ch.lower() for ch in s if ch.isalnum())

        secSt = frSt[::-1]

        print(frSt)
        print(secSt)

        return frSt == secSt
        