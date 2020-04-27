import re

# Match if there is a vowel on the string
vowels_class = r"[aeiou]"

# If the 5 is not written two times, no match
curly_pattern = r"85{2,2}19"

# From beginning to end, check if last name repeats 1 or more times
group_pattern = r"^Ivan (Santiago)+$"

if re.search(vowels_class, "Ivan Santiago"):
    print("Match vowels")
else:
    print("No match for vowels")

if re.match(curly_pattern, "85519"):
    print("Match repetitions")
else:
    print("No match repetitions")

if re.match(group_pattern, "Ivan Santiag"):
    print("Match group")
else:
    print("No match for group")
