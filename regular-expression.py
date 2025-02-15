import re


def read_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
        exit(1)

# this are regex patterns for only 5 data typs
regex_patterns = {
    "email addresses": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
    "URLs": r"https?://(?:www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:[/?#][^\s]*)?",
    "phone numbers": r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}",
    "credit Card numbers": r"\b(?:\d{4}[- ]?){3}\d{4}\b"
}

# dispaly of data types
def extract_data(text):
    for data_type, pattern in regex_patterns.items():
        matches = re.findall(pattern, text)
        print(f" **** EXTRACTED {data_type}: ****")
        for match in matches:
            print(f"  - {match}")
            print()

# Main function
def main():
    file_path = "ls.txt"
    text_content = read_file(file_path)
    extract_data(text_content)

if __name__ == "__main__":
    main()

