# CiscoFTD-Object
use Python for adding Network Object to Cisco FTD

In script you need to insert your actual information:

- your login to Cisco FTD in user_name:
user_name = "mylogin"

- your login to Cisco FTD in password:
password = "mypassword"

- your IP Address of Cisco FTD in {MY_IPADD_OF_FTD} for driver.get("https://MY_IPADD_OF_FTD/#/login")
 for example:
driver.get("https://10.10.10.10/#/login")

- change path to file with ip addresses in line 30 to your location:
 with open(r"C:\Python\TP\66.txt") as f:--

## Requirements:
 - python 3
 - pip
 - time
 - selenium
 
 ## Installation:
	pip install time
 	pip install selenium
  
## Examples:
python add_net_object_ftd.py 
