size = int(input())
lines = []
while True:
    lines.append(int(input()))
    if len(lines) == size:
        break

max_val = lines[1] - lines[0]

# for i in range(len(lines)):
#     for j in range(i, len(lines)):
#         if i == j:
#             continue
#         if max_val < lines[j] - lines[i]:
#             max_val = lines[j] - lines[i]
#
# print(max_val)

min_input = lines[0]
for i in range(1, len(lines)):
    if max_val < lines[i] - min_input:
        max_val = lines[i] - min_input
    if min_input > lines[i]:
        min_input = lines[i]

print(max_val)


