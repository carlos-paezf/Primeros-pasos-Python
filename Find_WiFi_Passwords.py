import subprocess

# now we will store the profiles data in "data" variable by
# running the 1st cmd command using subprocess.check_output
data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')


profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
for i in profiles:
	# running the 2nd cmd command to check password
	results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
	# storing password after converting then to list
	results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
	# printing the profiles(wifi name) with their passwors using
	# try and except method
	try:
		print("{:<30}| {:<}".format(i, results[0]))
	except IndexError:
		print("{:<30}| {:<}".format(i, ""))

'''
netsh wlan show profile (wifiname) key = clear
'''