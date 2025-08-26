class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        only_letters = []
        for char in s:
            if char.isalnum():
                only_letters.append(char)

        left = 0
        right = len(only_letters) - 1

        while left < right:
            if only_letters[left] != only_letters[right]:
                return False
            left += 1
            right -= 1

        return True

obj = Solution()
print(obj.isPalindrome("A man, a plan, a canal: Panama"))
