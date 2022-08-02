from pytube import YouTube
link = input("ENTER THE LINK FROM THE YOUTUBE:")
yt = YouTube(link)
# various information of the link
"""VIDEO TITLE"""
print("VIDEO TITLE:", yt.title)
"""VIDEO LENGTH"""
print("video length", yt.length, "seconds")
"""no of views """
print("VIEWS:", yt.views)
"""Description of the views"""
print("DESCRIPTION:", yt.description)
"""Rating of the video"""
print("RATING:", yt.rating)
"AVAILABLE STREAMS"
print(yt.streams)
#"""TO FILTER OUT THE audio"""
# print(yt.streams.filter(only_audio=True))
#"""TO FILTER OUT THE VIDEO"""
# print(yt.streams.filter(only_video=True))
videos = yt.streams.all()
vid = list(enumerate(videos))
for i in vid:
    print(i)
print()
strm = int(input("enter the stream:"))
print("DOWNLOADING........")
videos[strm].download()
print(" DOWNLOAD success 100%")
