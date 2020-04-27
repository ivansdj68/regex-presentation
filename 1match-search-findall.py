import re

pattern = r"a"

if re.match(pattern, "Ivan Santiago De Jesus"):
    print("Match")
else:
    print("No match")

if re.search(pattern, "Ivan Santiago De Jesus"):
    print("Search match")
else:
    print("No search match")

find_all = re.findall(pattern, "Ivan Santiago De Jesus")
print(find_all, " '{}' appeared {} times".format(pattern, len(find_all)))
