from pytube import  YouTube  
import pytube  
try:
    video_url = 'https://www.youtube.com/watch?v=lTTajzrSkCw'   
    youtube = pytube.YouTube(video_url)  
    video = youtube.streams.first()  
    video.download('C:/Users/abhay/Desktop/')  
    print("Download Successfull !!")
except:
    print("Something Went Wrong !!")