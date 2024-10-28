import time

def generate_permutations(string, include_duplicates=True):
    """Generate all permutations of a given string using a recursive approach."""
    if not string:
        return []

    chars = list(string)
    unique_permutations = set()

    def recursive_permute(current_index):
        if current_index == len(chars) - 1:
            permutation = ''.join(chars)
            if include_duplicates or permutation not in unique_permutations:
                unique_permutations.add(permutation)
        else:
            for i in range(current_index, len(chars)):
                # Swap characters
                chars[current_index], chars[i] = chars[i], chars[current_index]
                recursive_permute(current_index + 1)
                # Backtrack
                chars[current_index], chars[i] = chars[i], chars[current_index]

    recursive_permute(0)
    return list(unique_permutations) if not include_duplicates else list(unique_permutations)


def get_all_permutations(s, include_duplicates=True):
    """Generate all permutations of a given string using an iterative approach."""
    if not s:
        return []

    s = ''.join(sorted(s))
    n = len(s)
    permutations = set()

    while True:
        if include_duplicates or s not in permutations:
            permutations.add(s)
            print(s)  # Print the current permutation

        # Step 1: Find the largest index i such that s[i-1] < s[i]
        i = n - 1
        while i > 0 and s[i - 1] >= s[i]:
            i -= 1
        
        # If no such index exists, we are done
        if i == 0:
            break
        
        # Step 2: Find the largest index j such that s[j] > s[i-1]
        j = n - 1
        while s[j] <= s[i - 1]:
            j -= 1
        
        # Step 3: Swap the pivot s[i-1] with s[j]
        s_list = list(s)  # Convert to list for swapping
        s_list[i - 1], s_list[j] = s_list[j], s_list[i - 1]
        s = ''.join(s_list)  # Convert back to string
        
        # Step 4: Reverse the sequence from s[i] to the end
        s = s[:i] + s[i:][::-1]

    return list(permutations) if not include_duplicates else list(permutations)


if __name__ == "__main__":
    try:
        user_input = input("Enter a string to generate permutations: ")
        if user_input.strip() == "":
            raise ValueError("Input string cannot be empty.")
        
        include_duplicates = input("Include duplicate permutations? (yes/no): ").strip().lower()
        if include_duplicates not in ["yes", "no"]:
            raise ValueError("Please enter 'yes' or 'no'.")
        
        include_duplicates = include_duplicates == "yes"
        
        # Measure execution time for recursive method
        start_time = time.time()
        recursive_perms = generate_permutations(user_input, include_duplicates)
        recursive_time = time.time() - start_time
        
        print(f"Recursive permutations ({len(recursive_perms)}): {recursive_perms}")
        print(f"Recursive time: {recursive_time:.6f} seconds")

        # # Measure execution time for iterative method
        # start_time = time.time()
        # iterative_perms = get_all_permutations(user_input, include_duplicates)
        # iterative_time = time.time() - start_time
        
        # print(f"Iterative permutations ({len(iterative_perms)}): {iterative_perms}")
        # print(f"Iterative time: {iterative_time:.6f} seconds")

    except Exception as e:
        print(f"Error: {e}")
