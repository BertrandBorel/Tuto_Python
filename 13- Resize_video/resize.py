# Redimensionner une vidéo
import cv2

# Ouvrir la vidéo originale
vid = cv2.VideoCapture('path of video')
# Récupérer les dimensions de la vidéo originale
width = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
# Créer un objet VideoWriter pour écrire la vidéo redimensionnée
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('enter path + video_name.mp4', fourcc, 25, (1000, 600))

# Boucler sur toutes les images de la vidéo originale
while True:
    ret, frame = vid.read()
    # Si la vidéo est terminée, sortir de la boucle
    if not ret:
        break
    # Redimensionner l'image
    resized = cv2.resize(frame, (1000, 600))
    # Écrire l'image redimensionnée dans la nouvelle vidéo
    out.write(resized)
# Libérer les ressources
vid.release()
out.release()
cv2.destroyAllWindows()
