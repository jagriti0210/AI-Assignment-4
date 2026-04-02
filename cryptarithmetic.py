from itertools import permutations

print("=" * 40)
print("  Cryptarithmetic: TWO + TWO = FOUR")
print("=" * 40)
print()
print("         T W O")
print("     +   T W O")
print("     -----------")
print("     = F O U R")
print()
print("Finding the solution...\n")

for perm in permutations(range(10), 6):

    T, W, O, F, U, R = perm

    if T == 0 or F == 0:
        continue

    TWO  = 100*T + 10*W + O
    FOUR = 1000*F + 100*O + 10*U + R

    if TWO + TWO == FOUR:
        print("Solution found!\n")
        print("  Letter  -->  Digit")
        print("  " + "-" * 20)
        letters = ['T', 'W', 'O', 'F', 'U', 'R']
        for letter, digit in zip(letters, perm):
            print(f"    {letter}     -->   {digit}")

        print()
        print("  Verification:")
        print(f"    TWO  = {TWO}")
        print(f"    FOUR = {FOUR}")
        print(f"\n    {TWO} + {TWO} = {FOUR}  ✓")
        break