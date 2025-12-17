files = ["abc.txt", "def.csv", "ghi.docx", "jkl.csv", "-mno.csv",
         "abc.txd", "dlf.csv", "gei.docx", "jel.csv", "!mno.csv",
         "abc..csv", "abc.2025.csv", ".csv", "abc."]

valid_filetypes = (".txt", ".csv")

accepted_files = []
rejected_files = []

for file in files:
    if not file.endswith(valid_filetypes):
        reason = "invalid extension"
        rejected_files.append((file, reason))
        print(file, "Rejected:", reason)

    elif file.count(".") != 1:
        reason = "invalid filename structure (must contain exactly one dot)"
        rejected_files.append((file, reason))
        print(file, "Rejected:", reason)

    elif not file.replace(".", "").isalnum():
        reason = "invalid characters (only letters/numbers allowed in name)"
        rejected_files.append((file, reason))
        print(file, "Rejected:", reason)

    else:
        accepted_files.append(file)
        print(file, "Accepted")

print("\nSummary")
print("Total files processed:", len(files))
print("Files accepted:", len(accepted_files))
print("Files rejected:", len(rejected_files))

print("\nRejected details:")
for file, reason in rejected_files:
    print("-", file, "→", reason)
