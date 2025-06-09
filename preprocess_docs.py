import os

def preprocess_markdown_files(directory="docs"):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".html.md"):
                filepath = os.path.join(root, file)
                print(f"Processing: {filepath}")
                with open(filepath, "r", encoding="utf-8") as f:
                    lines = f.readlines()
                
                cleaned_lines = []
                for line in lines:
                    # Remove lines that start with <?xml or contain <!DOCTYPE html>
                    if not line.strip().startswith("<?xml") and not line.strip().startswith("<!DOCTYPE html>"):
                        cleaned_lines.append(line)
                
                with open(filepath, "w", encoding="utf-8") as f:
                    f.writelines(cleaned_lines)

if __name__ == "__main__":
    preprocess_markdown_files()
    print("Preprocessing complete.") 