import os

def search_files(directory, filenames, case_sensitive=True):
    """
    Search recursively for specified filenames within the given directory and its subdirectories.

    Args:
        directory (str): The path to the directory to search.
        filenames (list): A list of filenames to search for.
        case_sensitive (bool): Whether the search should be case-sensitive.

    Returns:
        dict: A dictionary with filenames as keys and a list of full paths where the file was found.
    """
    # Use a set for case-insensitive filename matching and a dict to store results
    filename_set = set(filenames if case_sensitive else [f.lower() for f in filenames])
    matches = {filename: [] for filename in filenames}  # Dictionary to store file matches

    def recursive_search(current_dir):
        try:
            with os.scandir(current_dir) as entries:
                for entry in entries:
                    if entry.is_dir(follow_symlinks=False):
                        recursive_search(entry.path)  # Recursive call for directories
                    elif entry.is_file(follow_symlinks=False):
                        # Normalize based on case-sensitivity
                        entry_name = entry.name if case_sensitive else entry.name.lower()
                        if entry_name in filename_set:
                            original_name = entry.name if case_sensitive else next(
                                fn for fn in filenames if fn.lower() == entry_name
                            )
                            matches[original_name].append(os.path.abspath(entry.path))
        except PermissionError:
            print(f"Permission denied: {current_dir}")
        except Exception as e:
            print(f"Error accessing {current_dir}: {e}")

    # Start the search from the given directory
    if os.path.isdir(directory):
        recursive_search(directory)
    else:
        print(f"The specified directory '{directory}' does not exist.")
        return {}  # Return an empty dictionary instead of None

    # Display results
    for filename, paths in matches.items():
        if paths:
            print(f"Found '{filename}' {len(paths)} time(s):")
            for path in paths:
                print(f"  - {path}")
        else:
            print(f"'{filename}' was not found in the directory '{directory}'.")

    return matches  # Return the matches dictionary




