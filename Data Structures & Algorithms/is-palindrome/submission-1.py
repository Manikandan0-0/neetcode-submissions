class Solution:
    def isPalindrome(self, s: str) -> bool:
        string="".join(ch.lower() for ch in s if ch.isalnum())
        l=0
        r=len(string)-1
        while(l<r):
            if string[l]!=string[r]:
                return False
            else:
                l+=1
                r-=1
        return True

        