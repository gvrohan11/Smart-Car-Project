# Smart-Car-Project

App that allows me to control my smart car from anywhere in the world
- The smart car is made with a raspberry pi
- Created a flask app to control the car remotely
- Used AWS EC2 to facilitate commands to move the car

# Important Information

Local: Server that anyone can run from their laptop/computer/machine; Sends control directions to and receives status updates from Cloud 
- To run, change directory to Local (cd Local)
- execute "python3 -m flask run"

Cloud: server hosted on the cloud with AWS EC 2 that receives and send back information to Local, and receives information from Raspberry Pi

Raspberrypi: Code used to retrieve and send information to the cloud