import numpy 
import requests

from urlTamperable import crackhubScene_Filter, crackhub_Filter

search = str(input("Enter Search: "))

crackhub_Filter.crackhubSearch(search)
crackhubScene_Filter.crackhubSceneSearch(search)
