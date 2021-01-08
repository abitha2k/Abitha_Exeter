import fileinput

#save the code in the path ,where the text file is available
text = "filename.txt"
fields = {"about": "sur", "alone": "seul", "already": "dÃ©jÃ", "after": "aprÃ¨s", "birth": "naissance", "bless": "bÃ©nir"}


for line in fileinput.input(text, inplace=True):
    line = line.rstrip()
    if not line:
        continue
    for f_key, f_value in fields.items():
        if f_key in line:
            line = line.replace(f_key, f_value)
    print(line)
