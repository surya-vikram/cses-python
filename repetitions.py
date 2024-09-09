seq = input()
max_rep = 0
count = 0
prev = None
for i in range(len(seq)):
    if seq[i] == prev:
        count += 1
    else:
        max_rep = max(max_rep, count)
        prev = seq[i]
        count = 1
print(max(max_rep, count))