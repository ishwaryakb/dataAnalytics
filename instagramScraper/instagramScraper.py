import instaloader

ig=instaloader.Instaloader()

#enter the username 
req_user=input("User name")

#download profile picture of the given username
ig.download_profile(req_user,profile_pic_only=True)

#downloads all posts including metadata for the given username
ig.download_profile(req_user,profile_pic=True)

