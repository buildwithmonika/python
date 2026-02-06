import os


def clear_folder_clutter(folder_path, extensions_to_rename):
    counter = {ext: 1 for ext in extensions_to_rename }
    with os.scandir(folder_path) as it:
        for file in it:
            print(f"Processing: {file.name}")
            if file.is_file():
                _, file_extension = os.path.splitext(file.name)
                file_extension = file_extension[1:]
                if file_extension in extensions_to_rename:
                    while True:
                        new_name = f"{counter[file_extension]}.{file_extension}"
                        new_path = os.path.join(folder_path, new_name)
                        if os.path.exists(new_path):
                            counter[file_extension] += 1
                        else:
                            os.rename(file.path, new_path)
                            break
                    counter[file_extension] += 1
                    print(f"Renamed: {file.name} to {new_name}")
    
    print("Renaming complete. Summary:")
    for ext, count in counter.items():
        print(f"{ext}: {count-1} files renamed.")

if __name__ == "__main__":
    if not os.path.exists("temp_folder"):
        os.mkdir("temp_folder")
        # Create some test files
        for i in range(50):
            with open(f"temp_folder/test_file_{i}.txt", "w") as f:
                f.write("This is a test file.\n")
            with open(f"temp_folder/test_file_{i}.log", "w") as f:
                f.write("This is a log file.\n")
            with open(f"temp_folder/test_file_{i}.pdf", "w") as f:
                f.write("This is a test file.\n")
            with open(f"temp_folder/test_file_{i}.docx", "w") as f:
                f.write("")
            with open(f"temp_folder/test_file_{i}.xlsx", "w") as f:
                f.write("")

    clear_folder_clutter("temp_folder", ["txt", "log", "pdf", "docx", "xlsx"])