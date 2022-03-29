import subprocess

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')

# for each in data: 
#     print(each)

profiles = [i.split(": ") for i in data if "All User Profile" in i]

for i in profiles: 
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', str(i[1][:-1]), 'key=clear']).decode('utf-8').split('\n')
    for b in results:
        if "Key Content" in b:
            print(f"{str(i[1][:-1])} : {b.split(':')[1]}")
