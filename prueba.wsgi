import sys
#Expand Python classes path with your app’s path
sys.path.insert(0, "E:/BilateralPneumoniaClassification")
from test import app
#Put logging code (and imports) here …
#Initialize WSGI app object
application = app