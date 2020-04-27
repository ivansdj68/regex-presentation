import re

# The string must match "Ivan" from start to finish
pattern = r"^Ivan$"

if re.match(pattern, "Ivan"):
    print("Match w/o accent")
else:
    print("No match for w/o accent")

if re.match(pattern, "Iván"):
    print("Match w/ accent")
else:
    print("No match for w/ accent")

if re.match(pattern, "IvanSantiago"):
    print("Match last name")
else:
    print("No match for last name")

