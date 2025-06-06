n = int(input())
courses = []

for _ in range(n):
    parts = input().split()
    name = parts[0]
    start = float(parts[1])
    end = float(parts[2])
    courses.append((start, end))

# 按结束时间排序
courses.sort(key=lambda x: x[1])

count = 0
current_end = 0

for start, end in courses:
    if start >= current_end:
        count += 1
        current_end = end

print(count)
