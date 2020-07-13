import digitalocean
import argparse
import config
import time


class Ocean:
    def __init__(self):
        self.api = config.api_key
        self.manager = digitalocean.Manager(token=self.api)

    def create(self,name,region,image,size_slug):
        if self.find(name):
            return None
        droplet = digitalocean.Droplet(token=self.api, name=name, region=region, image=image, size_slug=size_slug, ssh_keys=self.get_keys())
        droplet.create()
        actions = droplet.get_actions()
        for action in actions:
            while(action.status != 'completed'):
                time.sleep(1)
                action.load()
        return droplet

    def destroy(self,name):
        droplet = self.find(name)
        if droplet and droplet.destroy():
            while self.find(name):
                time.sleep(1)
            return True
        return None

    def get_all(self):
        return self.manager.get_all_droplets()
    
    def get_keys(self):
        return self.manager.get_all_sshkeys()

    def find(self, name):
        for d in self.get_all():
            if d.name == name:
                return d
        return None

    def get_ip(self, name):
        droplet = self.find(name)
        return droplet.ip_address if droplet else ''


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Control your DigitalOcean account droplets')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-n', '--new', nargs=1, metavar='<box_name>', help='Create a new droplet')
    group.add_argument('-d', '--destroy', nargs=1, metavar='<box_name>', help='Destroy an existing droplet')
    group.add_argument('-i', '--getip', nargs=1, metavar='<box_name>', help='Get the ip address of an existing droplet')
    group.add_argument('-l', '--list', action='count', help='List all existing droplets')
    args = parser.parse_args()

    ocean = Ocean()
    if args.getip:
        print(ocean.get_ip(name=args.getip[0]))
    elif args.new:
        ocean.create(name=args.new[0], region='tor1', image='ubuntu-20-04-x64', size_slug='s-1vcpu-1gb')
    elif args.destroy:
        ocean.destroy(name=args.destroy[0])
    elif args.list:
        print(ocean.get_all())
    else:
        print(parser.print_help())
