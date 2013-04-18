##Autosnap - Automatic Rotating Rackspace OpenCloud Snapshots

Good Evening, Cloud!

Due to high demand and numerous requests, I am be providing a way via cron and a small python script I have written to work around the current lack of automated snapshots within the Rackspace OpenCloud enviornment.

To start off, a few disclaimers:

1. This code is provided as-is and is not supported in any way. That said...
    * If a bug is found I will be more than willing to look into it and attempt a fix, but I cannot guarantee turnaround time or that an issue will be updated.
    * If you would like to fix it yourself, by all means do so! This code is open-source for anyone to use and modify as they see fit. A github link will be provided later for anyone wishing to do pull requests/forks/clones/etc.
    * Feature requests will also be looked at but will receive much lower priority.
    
2. This is -NOT- meant to be a permanent fix or a replacement for automated snapshots. Automatic snapshots are coming down the pipeline for OpenCloud servers so this is just a band-aid until that time.

3. This one is a biggie! Remember that snapshots do not a backup make! Snapshots are a great way to make a 'golden-image' of a server or provide a quick way to restore a server in the event of an issue. You should always (and I mean Always!) use as many backup options available to you as reasonable. Rackspace OpenCloud offers file level Cloud Backups as a service, which I highly encourage everyone to use. Also, remember that  while we do our best to protect everyone's data, we may not be able to plan for all circumstances (such as meteors crashing into our data center) so be sure that you have local or otherwise off-site backups of your essential data. A snapshot will allow you to easily pick up where you left off, but it's not a replacement for ensuring your critical data is safe and secure.


Okay... now that the caveats are out of the way, on to the fun.

### GITHUB LINK

https://github.com/redphaser/autosnap

### DESCRIPTION

autosnap is a small python script that I wrote to fill in the gaps between now and when an automatic snapshot feature will be provided by Rackspace OpenCloud as a supported feature.

It has been designed to be used primarily under Linux environments in conjunction with cron. 

### INSTALLATION INSTRUCTIONS

### BEST PRACTICES
