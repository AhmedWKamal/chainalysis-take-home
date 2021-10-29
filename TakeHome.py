#TakeHome.py
#Ahmed Kamal

import os
import backend
import frontend
import time

# Create our objects
backend = backend.Backend()
#Build our flask app
os.system("export FLASK_APP=frontend")
os.system("flask run")