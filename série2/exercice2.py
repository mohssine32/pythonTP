notes = [12, 5.5, 17, 9, 13, 8, 10]
print(min(notes))
print(max(notes))
print(sum(notes) / len(notes))

for i in notes:
    if i >= 10:
        print(i)