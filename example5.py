import re

pattern = r"\d+"
text = "Order123 was placed on 2023-05-01."

print(re.findall(pattern,text))