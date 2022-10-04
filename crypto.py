# import hashlib
from passlib.hash import sha512_crypt


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


password = "$6$penguins$eP.EvNiF2A.MmRVWNgGj5WSXKK8DAf7oeK8/kkbollee.F0T4KAy.QEgNAX.6wLQY1XHmSID/5VkeFiEaSA2b0"
salt = "penguins"

combos = []
cracked = []
file = open("passwordsCracked.txt", "w+")
for i in range(0, 10):
    for j in range(0, 10):
        for k in range(0, 10):
            combos.append((i, j, k))

for item in range(len(combos)):
    item = str(item)
    hashed_pass = sha512_crypt.using(salt=salt, rounds=5000).hash(item)
    if not hashed_pass == password:
        print("Checked: ", item, "No match")
    if hashed_pass == password:
        print(bcolors.RED + "Cracked:", item, "Hash: ", hashed_pass + bcolors.ENDC)
        cracked.append(item)
        file.write("Hash: " + hashed_pass + "\nCracked Password : " + item)
        file.close()
print(bcolors.OKGREEN + "Finished cracking passwords with", len(cracked),
      "password successfully cracked!" + bcolors.ENDC)
