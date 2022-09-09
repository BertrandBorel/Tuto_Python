# Télécharger une vidéo Youtube 
# (pip install pytube)

# sources :
# - https://pytube.io/en/latest/
# - https://dev.to/seijind/how-to-download-youtube-videos-in-python-44od 
# - https://www.geeksforgeeks.org/pytube-python-library-download-youtube-videos/ 

from pytube import YouTube

# Entrer l'url de la vidéo youtube
url_video = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'

# Téléchargement (dans le dossier courant)
YouTube(url_video).streams.first().download()







