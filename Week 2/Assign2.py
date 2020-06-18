import re

print(sum([int(i) for i in re.findall('[0-9]+', open("Week 2\Assign2.txt").read())]))
