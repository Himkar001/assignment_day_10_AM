# Day 10 — Part D (AI Augmented Task)

## Prompt Used

Write a Python function that takes two dictionaries representing student grades from two semesters and produces a merged report showing combined GPA, grade trend (improving/declining/stable), and subjects common to both semesters. Use defaultdict and dict comprehension.

---

# AI Generated Code

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
Critical Evaluation
Does it handle missing subjects?

Partially.
The code uses .get() which prevents errors, but it does not properly analyze missing subjects.

Does it safely use .get()?

Yes, .get() prevents KeyError.

Is the trend calculation correct?

No.
The AI code does not calculate grade trend (improving / declining / stable).

Edge Case Handling

The AI code does not handle:

empty dictionaries

single semester input

GPA calculation

Pythonic Code

The code partially follows Pythonic practices but does not use dictionary comprehension fully.

Improved Version
from collections import defaultdict

def merge_grades(sem1: dict, sem2: dict) -> dict:

    report = defaultdict(dict)

    subjects = set(sem1) | set(sem2)

    for sub in subjects:

        g1 = sem1.get(sub)
        g2 = sem2.get(sub)

        if g1 and g2:
            if g2 > g1:
                trend = "improving"
            elif g2 < g1:
                trend = "declining"
            else:
                trend = "stable"
        else:
            trend = "insufficient data"

        report[sub] = {
            "semester1": g1,
            "semester2": g2,
            "trend": trend
        }

    common_subjects = list(set(sem1) & set(sem2))

    return {
        "subjects": dict(report),
        "common_subjects": common_subjects
    }
Concepts Used

defaultdict

.get() safe dictionary access

dictionary merging

edge case handling

trend analysis