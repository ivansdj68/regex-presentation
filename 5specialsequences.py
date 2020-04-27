import re

pattern = r"Ivan( )+Santiago"
if re.match(pattern, "Ivan Santiago"):
    print("Match group")
else:
    print("No match for group")

pattern_ss = r"Ivan\s+Santiago"
if re.match(pattern_ss, "Ivan Santiago"):
    print("Match whitespace special sequence")
else:
    print("No match for whitespace special sequence")

pattern_ssd = r"santiago_\d\d\d\d\d"
if re.match(pattern_ssd, "santiago_85519"):
    print("Match digit special sequence")
else:
    print("No match for digit special sequence")


pattern_ssw = r"\wvan" #
if re.match(pattern_ssw, "|van"):
    print("Match word character special sequence")
else:
    print("No match for word character special sequence")
