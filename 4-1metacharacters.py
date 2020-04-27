import re

# Accept any character between 'v' and 'n'
pattern = r"Iv.n"

if re.match(pattern, "Ivan"):
    print("Match w/o accent")
else:
    print("No match for w/o accent")

if re.match(pattern, "Iván"):
    print("Match w/ accent")
else:
    print("No match for w/ accent")

if re.match(pattern, "Santiago"):
    print("Match last name")
else:
    print("No match for last name")

