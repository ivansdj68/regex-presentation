import re

# Match for zero or more repetitions of space character
patternAst = r"Ivan( )*Santiago"

# Match for one or more repetitions of space character
patternPlus = r"Ivan( )+Santiago"

# Match for zero or one repetitions of space character
patternQMark = r"Ivan( )?Santiago"

if re.match(patternAst, "IvanSantiago"):
    print("Match with *")
else:
    print("No match with *")

if re.match(patternPlus, "IvanSantiago"):
    print("Match with +")
else:
    print("No match with +")

if re.match(patternQMark, "Ivan  Santiago"):
    print("Match with ?")
else:
    print("No match with ?")
