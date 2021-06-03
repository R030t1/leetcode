#!/usr/bin/env python3

def lengthOfLongestSubstring_slow(s: str) -> int:
    l, t = 0, 0
    for b in range(len(s)):
        for e in range(b + 1, len(s) + 1):
            print('b, e', b, e)
            t = e - b
            w = s[b:e]
            print('w', '"' + w  + '"')
            for c in w:
                print('c', w.count(c))
                if w.count(c) > 1:
                    break
            else:
                if t > l: l = t
            print('l', l)
    return l

def lengthOfLongestSubstring(s: str) -> int:
    l, t = 0, 0
    if len(s) == 1:
        return 1
    for b in range(len(s) - 1):
        for e in range(len(s), b, -1):
            t = e - b
            w = s[b:e]
            print('w', '"' + w  + '"')
            for c in w:
                print('c', w.count(c))
                if w.count(c) > 1:
                    break
            else:
                if t > l: l = t
            print('l', l)
    return l

# Fails on website, exceeds time limit on long string.
# Need to memoize ranges known to contain duplicate characters?

# Go backwards? Nope.
def main():
    #s = 'au'
    #s = ' '
    #s = 'bbbbb'
    #s = 'pwwkew'
    s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ '"
    print(lengthOfLongestSubstring(s))

if __name__ == '__main__':
    main()
