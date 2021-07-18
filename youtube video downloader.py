# import package

from pytube import YouTube

url = input("Enter the url of the video")
my_video = YouTube(url)

print("**************Video Title**************")
#get video title

print(my_video.title)

print("***************Thumbnail Image************")
#get thumbnail image

print(my_video.thumbnail_url)


print("***************Download video*************")
#get all the stream resolution for the

# for stream in my_video.streams :
#       print(stream)


my_video = my_video.streams.get_highest_resolution()

#Download Video

my_video.download() #you can find your video in your download section of your pc or in your project file location






