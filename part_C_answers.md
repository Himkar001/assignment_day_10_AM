# Day 10 — Part C (Interview Ready)

## Q1 — Time Complexity of Dictionary Operations

### Lookup
Average Case: **O(1)**

Python dictionaries use a **hash table**.  
The key is converted into a hash value which directly points to a memory location.

### Insert
Average Case: **O(1)**

The key is hashed and placed in the corresponding bucket.

### Delete
Average Case: **O(1)**

Python locates the key using hashing and removes it.

### Worst Case Complexity

Worst case becomes **O(n)** when many **hash collisions** occur.

This happens when multiple keys map to the same hash bucket.

Python handles collisions using **open addressing**.

---

### Hash Function

For integers:

hash(x) = x


For strings:

Python computes a polynomial rolling hash based on characters.

---

### When to Use Dictionary Instead of List

Use a dictionary when:

- Fast lookups are needed
- Data is stored as **key-value pairs**
- Unique identifiers exist

Use lists when:

- Order matters
- Access by index is required
- Duplicate values are allowed

---

# Q2 — Group Anagrams

```python
from collections import defaultdict

def group_anagrams(words):

    groups = defaultdict(list)

    for word in words:
        key = ''.join(sorted(word))
        groups[key].append(word)

    return dict(groups)


print(group_anagrams(['eat','tea','tan','ate','nat','bat']))

Output

{
 'aet': ['eat','tea','ate'],
 'ant': ['tan','nat'],
 'abt': ['bat']
}
Q3 — Debug Code

Original buggy code:

def char_freq(text):
    freq = {}
    for char in text:
        freq[char] += 1
    sorted_freq = sorted(freq, key=freq.get, reverse=True)
    return sorted_freq
Bug 1

KeyError occurs because the key does not exist initially.

Bug 2

The function returns only keys instead of (key,count) pairs.

Fixed Version
def char_freq(text):

    freq = {}

    for char in text:
        freq[char] = freq.get(char,0) + 1

    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    return sorted_freq