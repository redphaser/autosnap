#!/usr/bin/env python

"""
This script provides a way to run rotating snapshots of a Rackspace
Cloud Server on the OpenCloud infrastructure.

Usage:
autosnap.py <username> <APIKey> <ServerUUID> <Minimum Retention> <Region>
"""

import pyrax
import argparse


def delete_old(snap_list, cloud):
    """Return an updated snapshot list after removing the oldest autosnap."""
    old = snap_list[0]
    for i in range(len(snap_list)-1):
        if old.created > snap_list[i+1].created:
            old = snap_list[i+1]
    cloud.images.delete(old)
    snap_list.remove(old)
    return snap_list


def main():
    """Parse arguments, take snap, and trigger deletion of oldest autosnap."""
    parser = argparse.ArgumentParser(description='auto-rotate image snapshots')
    parser.add_argument('user', metavar='username', type=str,
                        help='Username for account')
    parser.add_argument('key', metavar='apikey', type=str,
                        help='API key for account')
    parser.add_argument('server', metavar='server', type=str,
                        help='UUID of server to autosnap')
    parser.add_argument('retention', metavar='retention', type=int,
                        help='Minimum number of autosnaps to retain')
    parser.add_argument('region', metavar='region', type=str,
                        help='Region of Server (DFW, ORD, LON)',
                        choices=['DFW', 'ORD', 'LON'])

    args = parser.parse_args()

    pyrax.set_credentials(args.user, args.key)

    #Set up a cloud object based on region specified by user
    cloud = pyrax.connect_to_cloudservers(region=args.region)

    server = cloud.servers.get(args.server)
    images = cloud.images.list()

    snap_list = []

    snap_name = server.name + "-autosnap-" + args.server

    #Search for previous autosnaps of server and append to a list
    for i in images:
        search_name = server.name + "-autosnap-" + server.id
        if i.name == search_name:
            snap_list.append(i)

    #Delete oldest snapshot(s) if retention < num images
    while args.retention < len(snap_list):
        snap_list = delete_old(snap_list, cloud)

    #Create snapshot if retention >= number of previous autosnaps
    if args.retention >= len(snap_list):
        server.create_image(snap_name)


if __name__ == '__main__':
    main()
