
import pafy 
  
url = "https://www.youtube.com/watch?v=eACohWVwTOc"
video = pafy.new(url)
  
bestaudio = video.getbestaudio()
bestaudio.download()