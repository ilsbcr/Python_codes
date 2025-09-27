# find_duplicates.py
import sys
from collections import defaultdict

def find_duplicate_numbers(input_file):
    entries = []
    phone_map = defaultdict(list)

    # Read entries
    with open(input_file, "r", encoding="utf-8") as f:
        current_name = None
        current_phone = None

        for line in f:
            line = line.strip()
            if line.startswith("Name:"):
                current_name = line.replace("Name:", "").strip()
            elif line.startswith("Phone:"):
                current_phone = line.replace("Phone:", "").strip()

                if current_name and current_phone:
                    entries.append((current_name, current_phone))
                    phone_map[current_phone].append(current_name)

                # reset
                current_name = None
                current_phone = None

    # Find duplicates
    for phone, names in phone_map.items():
        if len(names) > 1:
            print(f"⚠️ Phone {phone} exists {len(names)} times:")
            for name in names:
                print(f"  Name: {name}\n  Phone: {phone}\n")
            print("-" * 30)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python find_duplicates.py file.txt")
        sys.exit(1)

    input_file = sys.argv[1]
    find_duplicate_numbers(input_file)
