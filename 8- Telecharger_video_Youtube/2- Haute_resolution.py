# Télécharger une vidéo youtube (haute définition)
# pip install pytube

# source :
# - https://pytube.io/en/latest/
# - https://dev.to/seijind/how-to-download-youtube-videos-in-python-44od 
# - https://www.geeksforgeeks.org/pytube-python-library-download-youtube-videos/ 

import pytube

# url de la vidéo youtube
url_video = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'

youtube = pytube.YouTube(url_video)

# -------------------------------------
# Régler la haute définition : 
video = youtube.streams.get_highest_resolution()

# -------------------------------------
# Télécharger la vidéo :
video.download() # indiquer le chemin souhaité (sinon : dossier courant)

# -------------------------------------
# Afficher le titre de la vidéo
print(video.title) 
