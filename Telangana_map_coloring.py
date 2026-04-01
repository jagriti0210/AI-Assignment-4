districts = [
    "Adilabad", "Komaram Bheem", "Mancherial", "Nirmal", "Nizamabad",
    "Jagtial", "Peddapalli", "Karimnagar", "Rajanna Sircilla", "Kamareddy",
    "Medak", "Sangareddy", "Siddipet", "Jangaon", "Jayashankar",
    "Mulugu", "Bhadradri Kothagudem", "Khammam", "Suryapet", "Nalgonda",
    "Yadadri", "Rangareddy", "Hyderabad", "Mahabubnagar", "Nagarkurnool",
    "Wanaparthy", "Gadwal", "Narayanpet", "Vikarabad", "Medchal",
    "Mahabubabad", "Warangal Urban", "Hanamkonda"
]

colors = ["Red", "Green", "Blue", "Yellow", "Orange", "Purple"]

neighbors = {
    "Adilabad": ["Komaram Bheem", "Nirmal", "Mancherial"],
    "Komaram Bheem": ["Adilabad", "Mancherial"],
    "Mancherial": ["Adilabad", "Komaram Bheem", "Nirmal", "Jagtial", "Peddapalli"],
    "Nirmal": ["Adilabad", "Mancherial", "Nizamabad", "Kamareddy", "Jagtial"],
    "Nizamabad": ["Nirmal", "Kamareddy", "Medak"],
    "Jagtial": ["Mancherial", "Nirmal", "Karimnagar", "Rajanna Sircilla", "Peddapalli"],
    "Peddapalli": ["Mancherial", "Jagtial", "Karimnagar", "Jayashankar"],
    "Karimnagar": ["Jagtial", "Peddapalli", "Rajanna Sircilla", "Siddipet", "Jangaon", "Warangal Urban"],
    "Rajanna Sircilla": ["Jagtial", "Karimnagar", "Kamareddy", "Siddipet", "Nizamabad"],
    "Kamareddy": ["Nizamabad", "Nirmal", "Medak", "Sangareddy", "Rajanna Sircilla"],
    "Medak": ["Nizamabad", "Kamareddy", "Sangareddy", "Siddipet"],
    "Sangareddy": ["Kamareddy", "Medak", "Siddipet", "Medchal", "Vikarabad", "Rangareddy"],
    "Siddipet": ["Rajanna Sircilla", "Kamareddy", "Medak", "Sangareddy", "Karimnagar", "Jangaon", "Yadadri"],
    "Jangaon": ["Karimnagar", "Siddipet", "Warangal Urban", "Hanamkonda", "Yadadri", "Mahabubabad"],
    "Jayashankar": ["Peddapalli", "Mulugu", "Bhadradri Kothagudem", "Mahabubabad", "Warangal Urban"],
    "Mulugu": ["Jayashankar", "Bhadradri Kothagudem"],
    "Bhadradri Kothagudem": ["Mulugu", "Jayashankar", "Khammam", "Mahabubabad"],
    "Khammam": ["Bhadradri Kothagudem", "Suryapet", "Nalgonda", "Mahabubabad"],
    "Suryapet": ["Khammam", "Nalgonda", "Yadadri"],
    "Nalgonda": ["Suryapet", "Khammam", "Yadadri", "Rangareddy"],
    "Yadadri": ["Siddipet", "Jangaon", "Suryapet", "Nalgonda", "Rangareddy", "Medchal"],
    "Rangareddy": ["Sangareddy", "Yadadri", "Nalgonda", "Hyderabad", "Vikarabad", "Mahabubnagar"],
    "Hyderabad": ["Rangareddy", "Medchal"],
    "Mahabubnagar": ["Rangareddy", "Wanaparthy", "Nagarkurnool", "Narayanpet", "Vikarabad"],
    "Nagarkurnool": ["Mahabubnagar", "Wanaparthy", "Gadwal", "Nalgonda"],
    "Wanaparthy": ["Mahabubnagar", "Nagarkurnool", "Gadwal"],
    "Gadwal": ["Wanaparthy", "Nagarkurnool", "Narayanpet"],
    "Narayanpet": ["Mahabubnagar", "Gadwal", "Vikarabad"],
    "Vikarabad": ["Sangareddy", "Rangareddy", "Mahabubnagar", "Narayanpet"],
    "Medchal": ["Sangareddy", "Hyderabad", "Yadadri"],
    "Mahabubabad": ["Jayashankar", "Jangaon", "Bhadradri Kothagudem", "Khammam", "Warangal Urban"],
    "Warangal Urban": ["Karimnagar", "Jayashankar", "Jangaon", "Hanamkonda", "Mahabubabad"],
    "Hanamkonda": ["Warangal Urban", "Jangaon"],
}

def is_safe(district, color, assignment):
    for neighbor in neighbors[district]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def solve(assignment):
    if len(assignment) == len(districts):
        return assignment

    for district in districts:
        if district not in assignment:
            next_district = district
            break

    for color in colors:
        if is_safe(next_district, color, assignment):
            assignment[next_district] = color
            result = solve(assignment)
            if result:
                return result
            del assignment[next_district]

    return None

print("=" * 45)
print("  Telangana Districts Map Coloring (CSP)")
print("=" * 45)

solution = solve({})

if solution:
    print(f"\nSolution found! All {len(solution)} districts colored.\n")
    print(f"{'District':<30} Color")
    print("-" * 40)
    for district, color in solution.items():
        print(f"{district:<30} {color}")
else:
    print("No solution found!")