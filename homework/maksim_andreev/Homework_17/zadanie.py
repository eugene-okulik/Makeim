import os
import re
import argparse


def search_text_in_files(folder_path, search_text):
    log_files = [file for file in os.listdir(folder_path) if file.endswith(".log")]

    for log_file in log_files:
        with open(os.path.join(folder_path, log_file), newline='') as file:
            line_number = 0
            for line in file:
                line_number += 1
                if search_text in line:
                    print(f"Error text '{search_text}' from file: {log_file}, line number: {line_number}")
                    words = re.split(r'\s+', line)
                    index = words.index(search_text)
                    start_index = max(0, index - 5)
                    end_index = min(len(words), index + 6)
                    context = " ".join(words[start_index:end_index])
                    print(f"Context: {context}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Search text in log files")
    parser.add_argument("folder", help="Folder containing log files")
    parser.add_argument("--text", required=True, help="Text to search")

    args = parser.parse_args()

    search_text_in_files(args.folder, args.text)
