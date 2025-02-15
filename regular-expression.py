import re

def read_file(file_path):
    try:
        with open(file_path, "r") as file:
           return file.read()
       #only extracts 5 data types
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        exit(1)
    #this are the regex to be used
regex_patterns = {
    "email addresses": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
    "URLs": r"https?://(?:www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:[/?#][^\s]*)?",
    "phone numbers": r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}",
    "credit card numbers": r"\b\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}\b",
    "Hashtags": r"#\w+",
}

def extract_data(text, pattern):
    return re.findall(pattern, text)

# this is the main function 
def main():
    # it will use data wich are located in ls.txt
    file_path = "ls.txt"
    text_content = read_file(file_path)

    # display extracted data types
    selected_data_types = [
        "email addresses",
        "URLs",
        "phone numbers",
        "credit card numbers",
        "Hashtags",
    ]

    for data_type in selected_data_types:
        print(f" **** EXTRACTED {data_type}: ****")
        matches = extract_data(text_content, regex_patterns[data_type])
        for match in matches:
            print(f"  - {match}")
            print()

if __name__ == "__main__":
    main()
