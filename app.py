import subprocess

whitelist_domains = (".dk", ".com")

read = input("Enter domain: ")


if read.endswith(whitelist_domains):
    command = "nslookup {}".format(read)
    response = subprocess.check_output(command, shell=True, encoding="UTF-8")
    print(response)
else:
    print("Error")
