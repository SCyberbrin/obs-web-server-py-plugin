# obs-web-server-py-plugin
A python script for obs to create multiple HTTP servers for localhost.
This script is usesing [Bottle](https://github.com/bottlepy/bottle) as server btw.

# !!!IMPORTANT!!!
Also, to know is that the script could make your obs slow at start up and at closing.
And also crashing your obs.
So please used it with caution.

# Properties
* **port**: Set port of the web server.
* **HTML folder path**: The **full** path of the folder with the index.html.


# TODOS:
* Make sure that it can make multiple HTTP servers (rn: it can only create one HTTP server)