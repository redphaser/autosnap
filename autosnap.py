#!/usr/bin/env python

import pyrax
import re
import argparse


def delete_old(snap_list):
    old = snap_list[0]
    for i in range(len(snap_list)-1):
        if old.created > snap_list[i+1].created:
            old = snap_list[i+1]
    cs.images.delete(old)
    snap_list.remove(old)
    return snap_list

parser = argparse.ArgumentParser(description='auto-rotate image snapshots')
parser.add_argument('user', metavar='username', type=str,
                    help='Username for account')
parser.add_argument('key', metavar='apikey', type=str,
                    help='API key for account')
parser.add_argument('server', metavar='server', type=str,
                    help='UUID of server to snapshot')
parser.add_argument('retention', metavar='retention', type=int,
                    help='Number of days to retain snapthots')
parser.add_argument('region', metavar='region', type=str,
                    help='Region of Server (DFW, ORD, LON)',
                    choices=['DFW', 'ORD', 'LON'])

args = parser.parse_args()

pyrax.set_credentials(args.user, args.key)

cs = pyrax.connect_to_cloudservers(region=args.region)
server = cs.servers.get(args.server)
images = cs.images.list()

server = cs.servers.get(args.server)

snap_list = []
snap_name = server.name + "-autosnap-" + args.server

#Search for previous autosnaps of server and append to a list
for i in images:
    search_name = "-autosnap-" + args.server
    if re.search(search_name, i.name + "$"):
        snap_list.append(i)

#Create snapshot if number of current snaps LTE retention
if args.retention >= len(snap_list):
    server.create_image(snap_name)

#Delete oldest snapshot(s) if retention < num images
while args.retention < len(snap_list):
    snap_list = delete_old(snap_list)
