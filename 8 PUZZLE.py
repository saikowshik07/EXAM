def count_inversions(state):
    """Count the number of inversions in the puzzle state."""
    flat_list = [num for num in state if num != 0]  # Ignore the empty tile (0)
    inversions = 0
    for i in range(len(flat_list)):
        for j in range(i + 1, len(flat_list)):
            if flat_list[i] > flat_list[j]:
                inversions += 1
    return inversions

def is_solvable(state):
    """Check if an 8-puzzle is solvable."""
    return count_inversions(state) % 2 == 0

# Define the initial state of the puzzle
initial_state = (2, 8, 3, 1, 6, 4, 7, 0, 5)

# Check if the puzzle is solvable
if is_solvable(initial_state):
    print("The puzzle is solvable!")
else:
    print("The puzzle is unsolvable.")
