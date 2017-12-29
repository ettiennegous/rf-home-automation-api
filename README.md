# rf-home-automation-api
Use Google Home to control in home RF devices.
This is a Python driven API that calls on PiLight and sends 433 mhz signals to home devices

* Need to install https://www.pilight.org/
* Uses Python 3
* Use this method to capture your 433mhz device signals https://medium.com/@tomwoolway/easily-finding-rf-codes-from-pilight-debug-c93c292b9a03
* Use these instructions to setup IFTTT https://support.google.com/googlehome/answer/7194656?co=GENIE.Platform%3DDesktop&hl=en

# Topology 
Google Home -> IFTTT -> Home Router (NAT Rule) -> Python API (Raspberry PI) -> PiLight -> 433 Mhz RF Device

# To Do
* Implement Security
* Implement IFTT webhook calls for PIR motion events
* Solve how to receive 433 mhz codes and perform actions based on those (Think door sensor)
