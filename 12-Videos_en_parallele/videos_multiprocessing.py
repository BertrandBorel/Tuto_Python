# affichage de deux vidéos en parallèle
import cv2
import multiprocessing as mp
import screeninfo
import time

# Informations sur l'écran
screen_info = screeninfo.get_monitors()[0]
screen_width = screen_info.width
screen_height = screen_info.height

def read_and_display_video(video_path, window_name, shape1, shape2):
    cap = cv2.VideoCapture(video_path)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow(window_name, frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        time.sleep(0.033)  # Pause de 0,033 secondes entre chaque frame
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    video1_path = './test/video_complete_2.mp4'
    video2_path = './test/video_finale_2.mp4'
    # Créer un processus pour la première vidéo
    p1 = mp.Process(target=read_and_display_video, args=(video1_path, 'Vidéo 1', 0, 0))
    p1.start()
    # Créer un processus pour la deuxième vidéo
    p2 = mp.Process(target=read_and_display_video, args=(video2_path, 'Vidéo 2', int(screen_width / 2), 0))
    p2.start()
    # Attendre que les processus se terminent
    p1.join()
    p2.join()
