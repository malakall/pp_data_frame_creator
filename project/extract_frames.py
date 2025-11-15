import cv2
import os


VIDEO_PATH = "videos/my_video.mp4" # путь к видсоу
OUTPUT_DIR = "frames"           # куда сохраняем
EVERY_NTH_FRAME = 8             # сохряняем каждый n-ый кадр


def extract_frames(video_path, output_dir, every_nth=1):
    os.makedirs(output_dir, exist_ok=True)

    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print(f"Не удалось открыть видео: {video_path}")
        return

    frame_idx = 0      
    saved_idx = 0  

    while True:
        ret, frame = cap.read()
        if not ret:
            break  

        
        if frame_idx % every_nth == 0:
            filename = f"frame_{saved_idx:06d}.jpg"  # название фоточек!! сделать норм как по доке для yolo
            filepath = os.path.join(output_dir, filename)
            cv2.imwrite(filepath, frame)
            print(f"Сохранён кадр: {filepath}")
            saved_idx += 1

        frame_idx += 1

    cap.release()
    print("Готово! Всего сохранено кадров:", saved_idx)


if __name__ == "__main__":
    extract_frames(VIDEO_PATH, OUTPUT_DIR, EVERY_NTH_FRAME)
