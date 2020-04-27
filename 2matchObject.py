import re

pattern = r"a"
search = re.search(pattern, "Ivan Santiago De Jesus")  # Returns a match object if successful

if search:
    print("Search match")
    print(search.group())
    print(search.start())
    print(search.end())
    print(search.span())
else:
    print("No search match")
