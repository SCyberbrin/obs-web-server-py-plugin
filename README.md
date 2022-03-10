# obs-web-server-py-plugin
A python script for obs to create localhost HTTP servers.

For example, running a Godot web app that is designed to run on obs with the browser source.


## Technologies
This script is using:

* [Bottle](http://bottlepy.org/docs/dev/)
* [Rocket3](https://github.com/web2py/rocket3) for multithreading, the Bottle framework

## Setup
To run this project, you will need to install the requirments:

```
pip install -r requirements.txt
```

And then load the script [obs_web_server.py](https://github.com/web2py/rocket3) to obs in Tools and Scripts.


## Properties
* **port**: Set port of the web server.
* **HTML folder path**: The **full** path of the folder with the index.html.


## To Do / Idea:
* Make it to run multiple local servers.