# oceanic
quickly create a digital ocean droplet

## setup 
- python3 -m pip install python-digitalocean
- add digital ocean api to config.py

## running 
- create a new droplet with the name <name>: *python3 oceanic.py -n <name>*
- delete a droplet: *python3 oceanic.py -n <name>*
- get ip address of droplet: *python3 oceanic.py -n <name>*
- list all droplets: *python3 oceanic.py -l*
