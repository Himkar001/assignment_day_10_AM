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
