##Autosnap - Automatic Rotating Rackspace OpenCloud Snapshots

Good Evening, Cloud!

Due to high demand and numerous requests, I am be providing a way via cron and a small python script I have written to work around the current lack of automated snapshots within the Rackspace OpenCloud enviornment.

To start off, a few disclaimers:

### DISCLAIMERS

This code is provided as-is and is not supported in any way. That said...
* If a bug is found I will be more than willing to look into it and attempt a fix, but I cannot guarantee turnaround time or that an issue will be updated.
* If you would like to fix it yourself, by all means do so! This code is open-source for anyone to use and modify as they see fit.
* Feature requests will also be looked at but will receive lower priority.
    
This is -NOT- meant to be a permanent fix or a replacement for automated snapshots. Automatic snapshots are coming down the pipeline for OpenCloud servers so this is just a band-aid until then.

This next one is a biggie!

Remember that snapshots do not a backup make! Snapshots are a great way to make a 'golden-image' of a server or provide a quick way to restore a server in the event of an issue. You should always (and I mean Always!) use as many backup options available to you as reasonable. Rackspace OpenCloud offers file level Cloud Backups as a service, which I highly encourage everyone to use. Also, remember that  while we do our best to protect everyone's data, we may not be able to plan for all circumstances (such as meteors crashing into our data center) so be sure that you have local or otherwise off-site backups of your essential data. A snapshot will allow you to easily pick up where you left off, but it's not a replacement for ensuring your critical data is safe and secure.


Okay, now that the caveats are out of the way, on to the fun.

### GITHUB LINK

https://github.com/redphaser/autosnap

### DESCRIPTION

autosnap is a small python script that I wrote to fill in the gaps between now and when an automatic snapshot feature will be provided by Rackspace OpenCloud as a supported feature.

It has been designed to be used primarily under Linux environments in conjunction with cron. 

### INSTALLATION

This script relies on the pyrax SDK for Rackspace OpenCloud. You can easily install it using python pip.
    
If you do not have pip installed, you can generally download it with your distribution's package manager. For example...

For RedHat (e.g. RedHat/CentOS/Fedora) based distros...

    sudo yum install python-pip

Or for Debian (e.g. Debian/Ubuntu) based distros...

    sudo apt-get install python-pip

Once you have pip, you can install pyrax by simply running...

    sudo pip install pyrax

The next step to is actually pull down the script.

Download the python script (git is the preferred method) to your selected directory. You can copy/paste the content of the script directly into a file if you wish (e.g. autosnap.py), just be sure it's executable or that you call it with python. If you do not have git, it can be installed via your distribution's package manager.

    git clone git://github.com/redphaser/autosnap.git

More documentation on git can be found at their website...

![Git Documentation](http://git-scm.com/documentation)

Once you have your environment set up with pyrax/autosnap.py you can now set up cron to run the script. You do -not- need root privleges so this can be run as any user.

### USAGE

Here is what you will need to run autosnap (all of this can be found in your Cloud Control panel at mycloud.rackspace.com)...

* Account username
* API Key
* Server UUID 
* Server Region (DFW, ORD, Lon)
* Desired Minimum Retention (explained in a moment)

Let's see an example...

    /your/folder/autosnap/autosnap.py rackuser abcdefghijklmnopqrstuvwxyz123456 abcdefgh-ijkl-mnop-qrst-uvwxyz123456 5 DFW

The help text for autosnap explains each argument...

    usage: autosnap.py [-h] username apikey server retention region
    
    auto-rotate image snapshots
    
    positional arguments:
      username    Username for account
      apikey      API key for account
      server      UUID of server to autosnap
      retention   Minimum number of autosnaps to retain
      region      Region of Server (DFW, ORD, LON)
    
    optional arguments:
      -h, --help  show this help message and exit

Most of the arguments are self-explanatory. 

To expand on Minimum Retention, this is a value passed that will determine the -Minimum- number of snapshots to save. During normal operation, the number of snapshots you have once they start to rotate will be retention + 1. The reasoning behind this is that if you have retention set to 1 snapshot you don't want a situation where you may be left with no valid snapshots available. 

Now to set this up with cron.

To have a basic setup of 7 rotating daily snapshots (this will leave you with 8 snapshots generally) that start at midnight (according to your system's time), your cron statement will look like this...

    ** 0 * * * /your/folder/autosnap/autosnap.py rackuser abcdefghijklmnopqrstuvwxyz123456 abcdefgh-ijkl-mnop-qrst-uvwxyz123456 7 DFW

Some great articles on how to use cron can be found at...

![Basic Linux task scheduling with cron](http://www.rackspace.com/knowledge_center/article/basic-linux-task-scheduling-with-cron)
![Fine-grained task scheduling with cron](http://ww.wip.rackspacecloud.com/knowledge_center/article/fine-grained-task-scheduling-with-crond)

### BEST PRACTICES

Depending on how you use this script, it can be amazing or a bit of a pain.

* The first thing to keep in mind is the amount of data being stored on your server. While there are currently no limits as to the size of a snapshot on Rackspace OpenCloud, the amount of data stored can weigh heavily on the amount of time it takes a snapshot to complete. Because of this, I don't recommend running these snaps any more than once per day. I've tested it on an hourly basis with a very small server and it does work so there's no hard rule against it, but I was only snapshotting about 1GB of data.

* My recommendation for how to run these snapshots is to have two sets of cron statements. One that will snapshot your server daily with a retention of 7 and then one that will keep a weekly snapshot with a retention of 2. This way, you will have at least 2 weekly snapshots and maintain snapshots for every day of the past week. I would even suggest going with a monthly run using a retention of 1 just in case something goes oddly awry and you need to revert a change made recently.


Eddie Bullard
Rackspace Cloud Servers Support

We like our weather cloudy.
