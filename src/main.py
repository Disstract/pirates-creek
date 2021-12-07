import numpy 
import requests

from urlTamperable import crackhubScene_Filter, crackhub_Filter, gloadFilter

search = str(input("Enter Search: "))

crackhub_Filter.crackhubSearch(search)
crackhubScene_Filter.crackhubSceneSearch(search)
gloadFilter.gloadSearch(search)
