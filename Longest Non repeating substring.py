def longestNonRepeatingSubstring(s):
    n = len(s)
    HashLen = 256
    
    last = [-1] * HashLen   # last seen index of each char
    
    l = 0
    maxLen = 0
    
    for r in range(n):
        if last[ord(s[r])] != -1:
            l = max(l, last[ord(s[r])] + 1)

        maxLen = max(maxLen, r - l + 1)
        last[ord(s[r])] = r

    return maxLen


s = "abcabcbb"
print(longestNonRepeatingSubstring(s))
