#Python 
#Script goes through a list of URLs from "domains-test" file and pings them to see if the domains are up

import os

home_hostname = "sometestdomain.com"
path="./domains-test"

def open_files_and_return_content(path):
#Open list of files from file:
    filename=path
    with open(filename) as f:
      content = f.readlines()
#You may also want to remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content]
    print(content)
    return content


def ping_each_hostname(content):
    num_content=len(content)
#Run ping through each item of content list
    for i in range(num_content):
        response = os.system("ping -c 1 " + content["i"])
    #and then check the response...
        if response != 0:
          print(response, 'is up!')
        else:
          print(response, 'is down!')


