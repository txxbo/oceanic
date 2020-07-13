# oceanic
quickly create a digital ocean droplet

## setup 
- python3 -m pip install python-digitalocean
- add ssh public key to your digital ocean account
- add digital ocean api to config.py

## running 
- create a new droplet with the name *droplet_name*: 
```
python3 oceanic.py -n droplet_name
```
- delete a droplet with the name *droplet_name*: 
```
python3 oceanic.py -d droplet_name
```
- get ip address of droplet with the name *droplet_name*: 
```
python3 oceanic.py -i droplet_name
```
- list all droplets: 
```
python3 oceanic.py -l
```
