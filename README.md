# assignment_day_10_AM
assignment for week-2 day10

# Day 10 — Part A

## E-Commerce Product Catalog System

### Overview

This program simulates a simple **e-commerce product catalog system** using Python dictionaries.
Each product is stored as a **nested dictionary** with details like name, price, category, stock, rating, and tags.

The catalog structure:

```
catalog = {
   sku: {
       name,
       price,
       category,
       stock,
       rating,
       tags: [...]
   }
}
```

The catalog contains **15 products** across four categories:

* Electronics
* Clothing
* Books
* Food

---

### Functions Implemented

#### 1. `search_by_tag(tag)`

Returns all products that contain a specific tag.

Example:

```
search_by_tag("fashion")
```

Output:

```
['Tshirt', 'Jeans', 'Sneakers']
```

Uses:

* `defaultdict(list)`
* `.get()` for safe access

---

#### 2. `out_of_stock()`

Returns all products where stock is **0**.

Uses:

* Dictionary comprehension
* Filtering condition

---

#### 3. `price_range(min_price, max_price)`

Filters products whose price falls within a given range.

Example:

```
price_range(500, 2000)
```

Uses:

* Dictionary comprehension
* `.get()` safe lookup

---

#### 4. `category_summary()`

Generates a summary for each category including:

* Number of products
* Average price
* Average rating

Uses:

* `defaultdict(list)`
* Aggregation using `sum()` and `len()`

Example output:

```
{
 'electronics': {'count': 4, 'avg_price': 27250, 'avg_rating': 4.35},
 'clothing': {'count': 4, 'avg_price': 1925, 'avg_rating': 4.12},
 'books': {'count': 4, 'avg_price': 675, 'avg_rating': 4.37},
 'food': {'count': 3, 'avg_price': 150, 'avg_rating': 4.13}
}
```

---

### Concepts Used

* Dictionary creation
* Nested dictionaries
* Dictionary comprehension
* `.get()` method
* `defaultdict` from `collections`
* Filtering and aggregation

---

### How to Run

```
python part_A_catalog.py
```

The script will display:

* Products by tag
* Out of stock products
* Price range filter
* Category summary

# Day 10 — Part B

## Log Analyzer using Counter and defaultdict

### Overview

This program simulates a **server log analyzer** that processes log entries and generates useful insights about system activity.

Each log entry is parsed into a dictionary with the following structure:

```
{
 'timestamp': ...,
 'level': ...,
 'module': ...,
 'message': ...
}
```

Example log line:

```
2026-03-06 10:02:11 ERROR db Connection failed
```

After parsing:

```
{
 'timestamp': '2026-03-06 10:02:11',
 'level': 'ERROR',
 'module': 'db',
 'message': 'Connection failed'
}
```

---

### Features Implemented

#### 1. Log Parsing

Each log line is converted into a structured dictionary containing:

* Timestamp
* Log level
* Module
* Message

This makes the logs easier to analyze programmatically.

---

#### 2. Log Level Distribution

Using `collections.Counter`, the program counts how many logs belong to each level:

* INFO
* WARNING
* ERROR
* CRITICAL

Example:

```
INFO: 2
ERROR: 2
WARNING: 1
CRITICAL: 1
```

---

#### 3. Most Common Error Messages

`Counter` is used to determine which error messages appear most frequently.

Example:

```
Connection failed (2)
```

---

#### 4. Most Active Module

The module generating the highest number of log entries is identified.

Example:

```
db
```

---

#### 5. Group Errors by Module

Using `defaultdict(list)`, all error messages are grouped by the module that generated them.

Example:

```
{
 'db': ['Connection failed', 'Connection failed']
}
```

---

### Summary Report

The program generates a summary dictionary containing:

```
{
 'total_entries': 6,
 'error_rate': 33.33,
 'top_errors': [('Connection failed', 2)],
 'busiest_module': 'db'
}
```

---

### Concepts Used

* `collections.Counter`
* `collections.defaultdict`
* Log parsing
* Dictionary creation
* Data aggregation

---

### How to Run

```
python part_B_log_analyzer.py
```

The script will analyze the simulated logs and display the summary statistics.
# Day 10 — Part C

## Interview Ready (Concept + Coding + Debugging)

### Overview

Part C focuses on **interview-level understanding of Python dictionaries** and problem-solving using dictionary-based algorithms.

This section includes:

1. Conceptual explanation of dictionary time complexity
2. Coding problem: grouping anagrams
3. Debugging a dictionary frequency counter

---

## Q1 — Dictionary Time Complexity

Python dictionaries are implemented using **hash tables**, which allow very fast operations.

### Lookup

Average Time Complexity:

```
O(1)
```

A key is passed through a **hash function** which maps it directly to a memory location.

---

### Insert

Average Time Complexity:

```
O(1)
```

The key is hashed and placed into the appropriate bucket.

---

### Delete

Average Time Complexity:

```
O(1)
```

The dictionary finds the key using hashing and removes it.

---

### Worst Case Complexity

Worst case becomes:

```
O(n)
```

This happens when **many hash collisions occur**, meaning multiple keys map to the same index.

Python handles collisions using **open addressing and probing**.

---

### Hash Function Behavior

For integers:

```
hash(x) = x
```

For strings:

Python computes a **polynomial rolling hash** based on character values.

---

### When to Use a Dictionary Instead of a List

Use a **dictionary** when:

* Fast lookups are required
* Data is stored as **key → value pairs**
* Unique identifiers are used

Use a **list** when:

* Order matters
* Access is index-based
* Duplicate values are allowed

---

## Q2 — Group Anagrams

Two words are **anagrams** if they contain the same characters in a different order.

Example:

```
eat → tea → ate
```

### Python Implementation

```python
from collections import defaultdict

def group_anagrams(words):

    groups = defaultdict(list)

    for word in words:
        key = ''.join(sorted(word))
        groups[key].append(word)

    return dict(groups)


print(group_anagrams(['eat','tea','tan','ate','nat','bat']))
```

### Output

```
{
 'aet': ['eat','tea','ate'],
 'ant': ['tan','nat'],
 'abt': ['bat']
}
```

Concepts used:

* `defaultdict`
* sorting characters to build a unique key
* grouping values by dictionary key

---

## Q3 — Debugging Character Frequency Code

### Buggy Code

```python
def char_freq(text):
    freq = {}
    for char in text:
        freq[char] += 1
    sorted_freq = sorted(freq, key=freq.get, reverse=True)
    return sorted_freq
```

---

### Problems

**Bug 1 — KeyError**

`freq[char] += 1` fails when the character appears for the first time.

**Bug 2 — Incorrect Return Value**

The code returns only keys instead of `(character, frequency)` pairs.

---

### Corrected Version

```python
def char_freq(text):

    freq = {}

    for char in text:
        freq[char] = freq.get(char,0) + 1

    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    return sorted_freq
```

This version safely updates dictionary values and correctly returns sorted frequency pairs.

---

### Concepts Used

* Dictionary hashing
* `defaultdict`
* Sorting dictionaries
* Debugging common Python dictionary errors

# Day 10 — Part D

## AI-Augmented Task

### Overview

In this section, an AI tool was used to generate Python code for merging student grade dictionaries from two semesters.
The task required analyzing the AI-generated code, evaluating its correctness, and improving it to handle real-world cases.

The goal was to produce a report containing:

* Combined student grade information
* Grade trend (improving / declining / stable)
* Subjects common to both semesters

---

## Prompt Used

```
Write a Python function that takes two dictionaries representing student grades from two different semesters and produces a merged report showing: combined GPA, grade trend (improving/declining/stable), and subjects common to both semesters. Use defaultdict and dict comprehension.
```

---

## AI Generated Code

```python
from collections import defaultdict

def grade_report(sem1, sem2):

    report = defaultdict(dict)

    subjects = set(sem1) | set(sem2)

    for sub in subjects:
        g1 = sem1.get(sub)
        g2 = sem2.get(sub)

        report[sub]["sem1"] = g1
        report[sub]["sem2"] = g2

    return report
```

---

## Critical Evaluation

### Handling Missing Subjects

The AI code uses `.get()` which avoids `KeyError`, but it does not explicitly handle missing subjects in the final report.

---

### Safe Dictionary Access

Yes.
The code uses `.get()` which safely retrieves values even when the key does not exist.

---

### Trend Calculation

The generated code does **not calculate the grade trend** (improving, declining, or stable).
This is a major requirement missing from the AI solution.

---

### Edge Case Handling

The AI code does not handle:

* Empty dictionaries
* Cases where a subject appears in only one semester
* GPA calculation

---

### Code Quality

The code structure is reasonable but it does not fully use **dictionary comprehensions** or provide a complete report structure.

---

## Improved Implementation

```python
from collections import defaultdict

def merge_grades(sem1: dict, sem2: dict) -> dict:

    report = defaultdict(dict)

    subjects = set(sem1) | set(sem2)

    for subject in subjects:

        g1 = sem1.get(subject)
        g2 = sem2.get(subject)

        if g1 is not None and g2 is not None:
            if g2 > g1:
                trend = "improving"
            elif g2 < g1:
                trend = "declining"
            else:
                trend = "stable"
        else:
            trend = "insufficient data"

        report[subject] = {
            "semester1": g1,
            "semester2": g2,
            "trend": trend
        }

    common_subjects = list(set(sem1) & set(sem2))

    return {
        "subjects": dict(report),
        "common_subjects": common_subjects
    }
```

---

## Concepts Used

* `defaultdict`
* Safe dictionary access using `.get()`
* Dictionary merging
* Set operations
* Edge case handling
* Trend analysis


