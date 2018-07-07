# python application that blocks certain websites in certain time
import time
from datetime import datetime as dt

hosts_temp = "hosts"
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = '127.0.0.1'
website_list = ["facebook.com", "www.facebook.com"]

# to run program as on Windows background process: change extension to '.pyw', create Task using Windows Task Scheduler

# to run program as on Linux background process:
# 1. change hosts_path='/etc/hosts'
# 2. in terminal: sudo crontab -e -> @reboot python3 /path_to_script/website_blocker.py

while True:
	if( dt( dt.now().year, dt.now().month, dt.now().day, 8 ) < dt.now() < dt( dt.now().year, dt.now().month, dt.now().day, 16 ) ):
		print( "Working hours ..." )
		with open( hosts_path, 'r+' ) as file:
			content = file.read()
			for website in website_list:
				if website in content:
					pass
				else:
					file.write( redirect + " " + website + "\n" )
	else:
		print( "Fun hours ..." )
		with open( hosts_path, 'r+' ) as file:
			content = file.readlines()
			file.seek(0)
			for line in content:
				if not any(website in line for website in website_list):
					file.write(line)
			file.truncate()
	time.sleep(5)
