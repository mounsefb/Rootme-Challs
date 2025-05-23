import requests
import re

session = requests.Session()

url = "http://challenge01.root-me.org/programmation/ch1/"
response = session.get(url)  # Le cookie est stocké automatiquement ici
html = response.text

recurrence = re.search(r"U<sub>n\+1</sub> = \[ ([-+]?\d+) \+ U<sub>n</sub> \] ([+-]) \[ n \* (\d+) \]", html)
u0_match = re.search(r"U<sub>0</sub> = ([-+]?\d+)", html)
target_matches = re.findall(r"U<sub>(\d+)</sub>", html)
target = max(map(int, target_matches))

if not recurrence or not u0_match or not target_matches:
    print("Erreur de parsing")
    exit()

a = int(recurrence.group(1))
op = recurrence.group(2)
b = int(recurrence.group(3))
u0 = int(u0_match.group(1))
n = target

sum_n = n * (n - 1) // 2
if op == '+':
    result = u0 + a * n + b * sum_n
else:
    result = u0 + a * n - b * sum_n

result_url = f"http://challenge01.root-me.org/programmation/ch1/ep1_v.php?result={result}"
res = session.get(result_url)  # utilise toujours la même session (donc le même cookie)

print(f"Suite : U(n+1) = {a} + Un {op} n * {b}")
print(f"U0 = {u0}, n = {n}")
print(f"Résultat : U{n} = {result}")
print("Réponse du serveur :", res.text)
