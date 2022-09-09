# Récupérer des informations sur une vidéo Youtube

# Source : 
# Documentation pytube : https://pytube3.readthedocs.io/_/downloads/en/latest/pdf/ 



import pytube
from pytube import YouTube


# url de la vidéo Youtube
url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'

# Id de la vidéo
name = pytube.extract.video_id(url)
print(name)

# Titre de la vidéo
title = YouTube(url).title
print(title)

# Savoir s'il y a une limite d'âge
age = YouTube(url).age_restricted
print(age)


### -----------------------------------
# Autre exemple :

# url de la vidéo
yt = YouTube('https://www.youtube.com/watch?v=-w2m-TeLi6I')

# titre de la vidéo
print(yt.title)

# thumbnail url
print(yt.thumbnail_url)

# voir tous les formats disponibles : 
print(yt.streams.all())

# stream 
stream = yt.streams.first()
print(stream)

# # Télécharger dans le dossier courant :
stream.download()

# # Télécharger dans un dossier précis
stream.download('chemin_du_dossier')

# Récupérer seulement l'audio :
audio = yt.streams.filter(only_audio=True).all()
print(audio)

# Récupérer uniquement le format MPEG-4 :
mp4 = yt.streams.filter(file_extension='mp4').all()
print(mp4)

# Récupérer par le tag :
yt.streams.get_by_itag('22')

# Récupérer les langues des sous-titres :
yt = YouTube('https://www.youtube.com/watch?v=-w2m-TeLi6I')
print(yt.captions.all())
