def pref_func(s):
    n = len(s)
    prefix = [0] * n
    for i in range(1, n):
        curr = prefix[i - 1]
        while curr > 0 and s[i] != s[curr]:
            curr = prefix[curr - 1]
        if s[i] == s[curr]:
            curr += 1
        prefix[i] = curr
    return prefix


s = str(input())
print(*pref_func(s))


