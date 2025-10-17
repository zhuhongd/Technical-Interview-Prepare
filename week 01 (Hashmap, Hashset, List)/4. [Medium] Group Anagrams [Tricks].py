"""
Problem: Group Anagrams

Given an array of strings `strs`, group all anagrams together into sublists. 
You may return the output in any order.

An anagram is a word formed by rearranging the letters of another word using 
all original letters exactly once.

🔗 Problem Link: https://neetcode.io/problems/anagram-groups

---

Examples

Input: strs = ["act", "pots", "tops", "cat", "stop", "hat"]
Output: [["act", "cat"], ["pots", "tops", "stop"], ["hat"]]

Input: strs = ["x"]
Output: [["x"]]

Input: strs = [""]
Output: [[""]]
[1,0, ..., 0] -> 26

---

📌 Constraints:
- 1 <= strs.length <= 1000
- 0 <= strs[i].length <= 100
- strs[i] consists of lowercase English letters only

---

🔍 Interview Insight:
This is a very common question used to test whether you understand:
1. Hashing & dictionary key constraints
2. How to build canonical representations (signatures) for grouping
3. Optimizing string grouping problems

"""

# ❌ WRONG APPROACH (Common mistake)
# -------------------------------
# You might try to use a frequency dictionary as a key like:
# {
#   {"a":1, "c":1, "t":1}: ["act"],
#   {"a":1, "c":1, "t":1}: ["cat"],
# }
# But this will FAIL because dictionaries are not hashable and cannot be used as keys.

# Code below will throw TypeError
# ----------------------------------------------------------------
# temp_map = {}
# for word in strs:
#     freq = {}
#     for c in word:
#         freq[c] = freq.get(c, 0) + 1
#     temp_map[freq] = word  # ❌ TypeError: unhashable type: 'dict'

# ✅ Correct Approaches Below
# ============================

from typing import List
from collections import defaultdict


# ✅ Approach 1: Using sorted strings as keys (O(N·KlogK))
# -------------------------------------------------------
# This is intuitive and works well in practice. All anagrams share the same sorted characters.

class SolutionSortKey:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)  # key: sorted string -> list of anagrams
        
        for word in strs:
            # Sort each word to create the anagram "signature"
            key = ''.join(sorted(word))  # e.g. "cat" and "tac" → "act"
            anagram_map[key].append(word)
        
        return list(anagram_map.values())

# Time complexity: O(N·KlogK), where N = len(strs), K = average word length
# Space complexity: O(N·K), storing all characters and groups


# ✅ Approach 2: Using character frequency tuple as keys (O(N·K))
# ---------------------------------------------------------------
# This is more optimal and avoids sorting by using a 26-element character count vector.

class SolutionCharCountKey:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)  # key: character frequency tuple -> list of anagrams
        
        for word in strs:
            # Create frequency vector (size 26 for 'a' to 'z')
            count = [0] * 26
            for char in word:
                count[ord(char) - ord('a')] += 1
            
            key = tuple(count)  # Tuples are hashable
            anagram_map[key].append(word)
        
        return list(anagram_map.values())

# Time complexity: O(N·K)
# Space complexity: O(N·K)

"""
📌 Summary

Two main approaches:
1. **Sorted string as key** — simpler, uses sort (O(N·KlogK))
2. **Character frequency vector** — more optimal, avoids sort (O(N·K))

Both solutions rely on:
✅ Using a canonical form of the word
✅ Hashing that canonical form to group anagrams
✅ Understanding Python’s hashability rules (dicts are unhashable, tuples are hashable)

In interviews, you can start with the sorted-string method and improve to the frequency vector if asked about optimization.

🎓 Tip: `defaultdict(list)` is a great tool to simplify appending in grouped collections.

"""

# -----------------------------
# Inline tests (order-insensitive comparison)
# -----------------------------

def _normalize(groups: List[List[str]]) -> List[tuple]:
    """
    Convert list of groups into a canonical, order-insensitive form:
    - Sort each group internally
    - Convert groups to tuples
    - Sort the list of tuples
    """
    return sorted(tuple(sorted(g)) for g in groups)

def _run_tests() -> None:
    sol = SolutionSortKey().groupAnagrams

    # Each case: (input_strs, expected_groups, label)
    TEST_CASES = [
        # Examples
        (["act", "pots", "tops", "cat", "stop", "hat"],
         [["act", "cat"], ["pots", "tops", "stop"], ["hat"]],
         "example-mixed"),
        (["x"], [["x"]], "single-letter"),
        ([""], [[""]], "single-empty"),

        # Duplicates and repeated words
        (["eat", "tea", "ate", "eat"],
         [["eat", "tea", "ate", "eat"]],
         "with-duplicates"),

        # Multiple groups, including singletons
        (["abc", "bca", "cab", "foo", "oof", "bar", ""],
         [["abc", "bca", "cab"], ["foo", "oof"], ["bar"], [""]],
         "mixed-groups"),

        # Non-anagrams with overlapping letters
        (["ab", "a"], [["ab"], ["a"]], "different-lengths"),

        # Many empties
        (["", "", "a"],
         [["", ""], ["a"]],
         "many-empties"),

        # Large-ish but quick
        (["aaa", "aaa", "aaaa", "aa", "baa", "aba", "aab"],
         [["aaa", "aaa"], ["aaaa"], ["aa"], ["baa", "aba", "aab"]],
         "length-variety"),

        # No mixing across groups
        (["bat", "tab", "tan", "ant", "eat", "tea", "ate"],
         [["bat", "tab"], ["tan", "ant"], ["eat", "tea", "ate"]],
         "canonical-classic"),
    ]

    passed = 0
    for i, (inp, expected, label) in enumerate(TEST_CASES, 1):
        got = sol(inp)
        ok = _normalize(got) == _normalize(expected)
        passed += ok

        def _prev_list(xs, maxlen=70):
            s = str(xs)
            return s if len(s) <= maxlen else s[:maxlen] + "...]"

        print(f"[{i:02d}][{label:<18}] input={_prev_list(inp):<72} "
              f"-> ok={ok} | {'✅' if ok else '❌'}")

        if not ok:
            print("  expected:", _normalize(expected))
            print("  got     :", _normalize(got))

    total = len(TEST_CASES)
    print(f"\nPassed {passed}/{total} tests.")


if __name__ == "__main__":
    _run_tests()
