import re

s = "vishwas"

# find characters between value-value
# print(re.findall('[a-i]',s))

s = "dsk kd $12898.00 dollars"

print(re.findall('[$]+\d',s))
print(re.findall('[$]*[0-9]',s))

# print(re.findall('\d',s))


# print(re.findall('\A\$+\d+.+\d',s))
# print(re.findall('\A\$+\d+.+\d',s))
# s = "12.00 dollars"
# print(re.findall('\A\$|\d+.+\d',s))
