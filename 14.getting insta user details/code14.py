# coded by Prince!
# a script to get instagram user details like
# profile name,number of followers,following,posts

##---made only for learning purpose---##

import requests,urllib.request
username = input("Enter instagram username: ")
req = urllib.request.urlopen("http://instagram.com/"+username)
content = req.read().decode("utf-8")
content = content.split("\n")

profile_name = content[7][:content[7].find('(')]
profile_data = content[192][content[192].find('"')+1 : content[192].find("Posts")+5]
print("\nProfile Name: {}\n{}has {}\n".format(profile_name,profile_name,profile_data))

##---next post we'll get profile picture---#