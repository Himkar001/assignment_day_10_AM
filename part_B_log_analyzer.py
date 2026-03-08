from collections import Counter, defaultdict

# Simulated logs
logs = [
"2026-03-06 10:00:01 INFO auth User login successful",
"2026-03-06 10:02:11 ERROR db Connection failed",
"2026-03-06 10:03:45 WARNING api Slow response",
"2026-03-06 10:04:10 ERROR db Connection failed",
"2026-03-06 10:05:20 INFO api Request processed",
"2026-03-06 10:06:22 CRITICAL server Out of memory"
]

parsed_logs = []

# Parse logs
for line in logs:
    parts = line.split(" ",4)

    log_dict = {
        "timestamp": parts[0] + " " + parts[1],
        "level": parts[2],
        "module": parts[3],
        "message": parts[4]
    }

    parsed_logs.append(log_dict)

# Counters
level_counter = Counter()
error_messages = Counter()
module_counter = Counter()

errors_by_module = defaultdict(list)

for log in parsed_logs:

    level = log["level"]
    module = log["module"]
    message = log["message"]

    level_counter[level] += 1
    module_counter[module] += 1

    if level == "ERROR":
        error_messages[message] += 1
        errors_by_module[module].append(message)

summary = {
    "total_entries": len(parsed_logs),
    "error_rate": (level_counter["ERROR"] / len(parsed_logs)) * 100,
    "top_errors": error_messages.most_common(3),
    "busiest_module": module_counter.most_common(1)[0][0]
}

print(summary)
print(errors_by_module)