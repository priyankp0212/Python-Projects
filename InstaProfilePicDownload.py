import instaloader
i= instaloader.Instaloader()
username = input("Enter Username: ")
i.download_profile(username, profile_pic_only= True)
