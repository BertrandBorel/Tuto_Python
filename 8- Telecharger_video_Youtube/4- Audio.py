# Télécharger la piste audio d'une vidéo Youtube

import pytube 

# Url de la vidéo :
url = 'https://www.youtube.com/watch?v=-w2m-TeLi6I'

# Téléchargement de l'audio : 
pytube.YouTube(url).streams.filter(only_audio=True).first().download()