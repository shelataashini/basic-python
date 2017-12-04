name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
ans = dict()
newwords = list()

for line in handle:
	line = line.rstrip()
	if not line.startswith('From '): continue
	words = line.split()
	new = words[1]
	newwords.append(new)

for word in newwords:
	ans[word] = ans.get(word,0)+1
		
bigcount = None
bigword = None
for (yes,count) in ans.items():
	if bigcount is None or count>bigcount:
		bigword= yes
		bigcount= count

print (bigword, bigcount)