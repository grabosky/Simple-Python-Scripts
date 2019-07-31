#Simple script that saves HTML of a website to XML file with current date and time as a filename (ie. 2019-01-01-12-05-25_website.xml)
#Then opens website in default webbrowser to take screenshot of it

import urllib
import webbrowser
from time import strftime
from subprocess import call

#Save html to a xml file
date_accesed = strftime("%Y-%m-%d-%H-%M-%S")
u = urllib.urlopen('http://www.address.com')
data = u.read()
f = open(date_accesed + '_website.xml', 'wb')
f.write(data)
f.close()

#Open website in default webbrowser
webbrowser.open('http://www.address.com')

#Take a screenshot and save it
call(["scrot"])

#To Do: need to slow down taking the screenshot as the website needs to fully load first




