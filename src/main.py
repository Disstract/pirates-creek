import numpy 
import requests

from urlTamperable.DirectSites import crackhub_Filter, crackhubScene_Filter, gloadFilter, gogGamesFilter, ovagamesFilter
from urlTamperable.Repacks import chovkaRepackFilter, fitgirlRepackFilter

search = str(input("Enter Search: "))

crackhubResults = crackhub_Filter.crackhubSearch(search)
print(" ")
print(crackhubResults)

crackhubSceneResults = crackhubScene_Filter.crackhubSceneSearch(search)
print(" ")
print(crackhubSceneResults)

gloadResults = gloadFilter.gloadSearch(search)
print(" ")
print(gloadResults)

gogGamesResults = gogGamesFilter.gogGamesSearch(search)
print(" ")
print(gogGamesResults)

ovaGamesResults = ovagamesFilter.ovaGamesSearch(search)
print(" ")
print(ovaGamesResults)

chovkaRepackResults = chovkaRepackFilter.chovkaSearch(search)
print(" ")
print(chovkaRepackResults)

fitgirlRepackResults = fitgirlRepackFilter.fitgirlSearch(search)
print(" ")
print(fitgirlRepackResults)  



