def generate_permutations(string):
    # Error handling for empty strings or None
    if string is None:
        raise ValueError("Input string cannot be None.")
    if string == "":
        raise ValueError("Input string cannot be empty.")

    # Set to store all unique permutations
    permutations = set()
    generate_permutations_helper("", string, permutations)
    return list(permutations)  # Convert the set back to a list before returning

def generate_permutations_helper(prefix, remaining, result):
    # Base case: if no characters are left, store the permutation
    if remaining == "":
        result.add(prefix)  # Use a set to store unique permutations
    else:
        # Iterate through each character in the remaining string
        for i in range(len(remaining)):
            # Choose the current character
            current_char = remaining[i]
            # Form a new remaining string without the current character
            new_remaining = remaining[:i] + remaining[i+1:]
            # Recur with the current character added to the prefix
            generate_permutations_helper(prefix + current_char, new_remaining, result)

if __name__ == "__main__":
    input_string = input("Enter a string to generate its permutations: ")  # Prompt user for input
    try:
        permutations = generate_permutations(input_string)
        print(f"Permutations of \"{input_string}\": {permutations}")
    except ValueError as e:
        print(e)
