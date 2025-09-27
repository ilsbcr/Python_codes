# extract_contacts.py
import sys

def extract_tel_and_fn(input_file, output_file):
    results = set()  # use a set to avoid duplicates
    current_name = None
    has_tel_for_current_name = False

    with open(input_file, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()

            # Capture FN (name)
            if line.startswith("FN:"):
                # if previous name had no TEL, warn
                if current_name and not has_tel_for_current_name:
                    print(f"⚠️ Warning: Name '{current_name}' has no phone number")

                current_name = line.replace("FN:", "").strip()
                has_tel_for_current_name = False

            # Capture TEL (phone number)
            elif line.startswith("TEL"):
                number = line.split(":")[-1].replace("-", "").strip()

                if number:
                    if current_name:
                        results.add((current_name, number))  # add to set (dedup)
                        has_tel_for_current_name = True
                    else:
                        print(f"⚠️ Warning: Phone '{number}' has no associated name")

        # end of file check
        if current_name and not has_tel_for_current_name:
            print(f"⚠️ Warning: Name '{current_name}' has no phone number")

    # Sort results by name
    sorted_results = sorted(results, key=lambda x: x[0].lower())

    # Write results to output file
    with open(output_file, "w", encoding="utf-8") as out:
        for name, phone in sorted_results:
            out.write(f"Name: {name}\n")
            out.write(f"Phone: {phone}\n\n")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python extract_contacts.py input.vcf output.txt")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    extract_tel_and_fn(input_file, output_file)
    print(f"✅ Contacts extracted to {output_file}")
