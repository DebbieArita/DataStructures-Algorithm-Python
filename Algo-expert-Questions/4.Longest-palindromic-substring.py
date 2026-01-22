"""
✔ A substring is a continuous block of characters (not skipping).
✔ A palindrome reads the same forwards and backwards.
Eg:
Input: "babad"
Output: "bab"  (or "aba")
"""

#Solution1
def longest_palindromic_substring(string):
    current_longest = [0, 1]
    for i in range(1, len(string)):
        odd = get_longest_palindrome_from(string, i - 1, i + 1)
        even = get_longest_palindrome_from(string, i - 1, i)
        longest = max(odd, even, key = lambda x: x[1] - x[0])
        current_longest = max(longest, current_longest, key = lambda x: x[1] - x[0])
    return string[current_longest[0]:current_longest[1]]

def get_longest_palindrome_from(string, left_idx, right_idx):
    while left_idx >= 0 and right_idx < len(string):
        if string[left_idx] != string[right_idx]:
            break
        left_idx -= 1
        right_idx += 1
    return [left_idx + 1, right_idx]


#Solution2
def longest_palindrome(s: str) -> str:
    if not s:
        return ""

    start, end = 0, 0

    def expand(l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return l+1, r-1  # return bounds of the palindrome

    for i in range(len(s)):
        # Odd-length
        l1, r1 = expand(i, i)
        # Even-length
        l2, r2 = expand(i, i+1)

        # Update longest
        if r1 - l1 > end - start:
            start, end = l1, r1
        if r2 - l2 > end - start:
            start, end = l2, r2

    return s[start:end+1]


#Solution3 - Dynamic programming
def longest_palindrome_dp(s: str) -> str:
    n = len(s)
    if n < 2:
        return s

    dp = [[False] * n for _ in range(n)]
    start, max_len = 0, 1

    for i in range(n):
        dp[i][i] = True  # single chars

    for length in range(2, n + 1):
        for l in range(n - length + 1):
            r = l + length - 1

            if s[l] == s[r]:
                if length == 2 or dp[l+1][r-1]:
                    dp[l][r] = True
                    if length > max_len:
                        start = l
                        max_len = length

    return s[start:start + max_len]

