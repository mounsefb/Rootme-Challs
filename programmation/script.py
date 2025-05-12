import requests
response = requests.get('http://challenge01.root-me.org/programmation/ch1/')
print (response.status_code)
print (response.content)
import re
x = re.findall(r"U.*</sub>", response.text)
x = re.sub(r"<sub>(.*?)</sub>", x)
print(x)
