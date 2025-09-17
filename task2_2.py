import re

pattern = r"\b[a-zA-Z]+"
text = "Order123 was placed on 2023-05-01."

print(re.findall(pattern,text))