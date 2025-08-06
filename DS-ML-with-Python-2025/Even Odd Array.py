AR = []
EAR = []
OAR = []

print("Enter 10 numbers:")
for _ in range(10):
    val = int(input())
    AR.append(val)
    if val % 2 == 0:
        EAR.append(val)
    else:
        OAR.append(val)

print("Even numbers (EAR):", EAR)
print("Odd numbers (OAR):", OAR)
