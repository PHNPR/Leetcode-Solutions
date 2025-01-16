from collections import Counter

class Solution:
    def minimumLength(self, s: str) -> int:
        return sum(1 if val & 1 else 2 for val in Counter(s).values())