prix = [9.99, 14.5, 3.2, 29.0]
for price in prix:
    print(price )

total = sum(prix)
print("Total :", total)

moyenne = total / len(prix)
print("Prix moyen :", moyenne)

print("Prix > 10€ :")
for p in prix:
    if p > 10:
        print(p)
    