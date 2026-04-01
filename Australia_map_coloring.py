regions = ["WA", "NT", "SA", "Q", "NSW", "V", "T"]

colors = ["Red", "Green", "Blue"]

neighbors = {
    "WA":  ["NT", "SA"],
    "NT":  ["WA", "SA", "Q"],
    "SA":  ["WA", "NT", "Q", "NSW", "V"],
    "Q":   ["NT", "SA", "NSW"],
    "NSW": ["SA", "Q", "V"],
    "V":   ["SA", "NSW"],
    "T":   []
}

def is_safe(region, color, assignment):
    for neighbor in neighbors[region]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def solve(assignment):
    if len(assignment) == len(regions):
        return assignment

    for region in regions:
        if region not in assignment:
            next_region = region
            break

    for color in colors:
        if is_safe(next_region, color, assignment):
            assignment[next_region] = color
            result = solve(assignment)
            if result:
                return result
            del assignment[next_region]

    return None

print("=" * 35)
print("  Australia Map Coloring (CSP)")
print("=" * 35)

solution = solve({})

if solution:
    print("\nSolution found!\n")
    for region, color in solution.items():
        print(f"{region} --> {color}")
else:
    print("No solution found!")