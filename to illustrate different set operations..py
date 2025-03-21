# Define two sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Union of sets
union_set = set1.union(set2)
print("Union:", union_set)

# Intersection of sets
intersection_set = set1.intersection(set2)
print("Intersection:", intersection_set)

# Difference of sets
difference_set = set1.difference(set2)
print("Difference (set1 - set2):", difference_set)

# Symmetric difference of sets
symmetric_difference_set = set1.symmetric_difference(set2)
print("Symmetric Difference:", symmetric_difference_set)

# Subset check
is_subset = set1.issubset(set2)
print("Is set1 a subset of set2?:", is_subset)

# Superset check
is_superset = set1.issuperset(set2)
print("Is set1 a superset of set2?:", is_superset)

# Adding an element to a set
set1.add(10)
print("After adding 10 to set1:", set1)

# Removing an element from a set
set1.remove(3)
print("After removing 3 from set1:", set1)

# Discarding an element (does not raise error if element is missing)
set2.discard(7)
print("After discarding 7 from set2:", set2)

# Clearing a set
set1.clear()
print("After clearing set1:", set1)
