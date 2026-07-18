# Two Sum

# Strategy:
# Store every number and its index inside a hash map.
# For each number, check whether its complement
# (target - number) already exists.

# Time Complexity: O(n)
# Space Complexity: O(n)


def two_sum(nums, target):

    lookup = {}

    for i, num in enumerate(nums):

        complement = target - num

        if complement in lookup:
            return [lookup[complement], i]

        lookup[num] = i

    return []


print(two_sum([2,7,11,15],9))
print(two_sum([3,2,4],6))
print(two_sum([3,3],6))


# Is Anagram

# Strategy:
# Count every character using a hash map.
# Compare both maps.

# Time Complexity: O(n)
# Space Complexity: O(n)


def is_anagram(s, t):

    if len(s) != len(t):
        return False

    count = {}

    for ch in s:
        count[ch] = count.get(ch,0)+1

    for ch in t:

        if ch not in count:
            return False

        count[ch] -= 1

        if count[ch] == 0:
            del count[ch]

    return len(count)==0


print(is_anagram("listen","silent"))
print(is_anagram("rat","car"))
print(is_anagram("evil","vile"))


# First Unique Character

# Strategy:
# Count frequency of every character using a hash map.
# Traverse again to find first character with frequency 1.

# Time Complexity: O(n)
# Space Complexity: O(n)


def first_unique_character(s):

    freq = {}

    for ch in s:
        freq[ch] = freq.get(ch,0)+1

    for i,ch in enumerate(s):

        if freq[ch]==1:
            return i

    return -1


print(first_unique_character("leetcode"))
print(first_unique_character("loveleetcode"))
print(first_unique_character("aabb"))