
import re

ss = ["b'30.27'\r\n"]

result = "-"

for s in ss:
	result = re.findall("[-+]?\d+[\.]?\d*[eE]?[-+]?\d*", s)

print result