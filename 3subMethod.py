import re

greeting = "Hola, usuario. ¿Como estas, usuario?"
pattern = r"usuario"
sub = re.sub(pattern, "Ivan", greeting)

print(greeting)
print(sub)
