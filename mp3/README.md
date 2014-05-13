CS398VL Project Skeleton
================

A project skeleton for CS398 VL (Visualizing Literature). This was initially created Spring 2014.

A Quick Note about the License
-----------------------------
This repository is licensed under the MIT license, meaning you are free to do whatever you like with it. When you fork this repository, you can even change the license to be closed source, GPL, whatever. By default, though, the LICENSE.md file included indicates that your fork is also completely open source, and anyone else may modify it at will.


Publishing
----------
You have several options for hosting your project. 

### Engineering@Illinois Servers
You can run the syncing script by typing `./sync.sh`, It will prompt you for some info. You may leave the hostname and destination folder as-is, but make sure your username is your Netid!

If you choose to, you can have the script save these values in a file called `.config`. To change the values later you can either edit that file or delete it and run the script again.

You may then access the site at http://web.engr.illinois.edu/~NETID/.

### Github Pages
This one is easy! You just need to create a `gh-pages` branch and Github will use that for hosting your site. Since you don't really need the `gh-pages branch` locally, you can use the following command to push master to gh-pages. This assumes origin is your fork, not the main repository.

    git push origin master:gh-pages
    
Note that this will make all of the files available on the website, not just HTML and the like. This is in contrast to the Illinois server above.

You can then access the site (after a short delay) at http://USERNAME.github.io/REPOSITORY_NAME

### Amazon Web Services
Coming soon!
