from pytube import YouTube

# Obtenir l'URL de la vidéo
url = ""

# Créer une instance de la classe YouTube
yt = YouTube(url, use_oauth=True, allow_oauth_cache=True)

# Sélectionner la meilleure résolution disponible
stream = yt.streams.get_highest_resolution()

# Télécharger la vidéo
stream.download()
