import cv2
import mediapipe as mp
import os
import json

input_dir = './data/frames'
output_dir = './features/visual'

mp_face = mp.solutions.face_mesh
face_mesh = mp_face.FaceMesh(static_image_mode=True)

for file in os.listdir(input_dir):
    if not file.endswith('.png'):
        continue
    path = os.path.join(input_dir, file)
    img = cv2.imread(path)
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb)

    data = {"video": file, "face_detected": False}
    if results.multi_face_landmarks:
        data["face_detected"] = True
        # just an example: first landmark's x,y,z
        lm = results.multi_face_landmarks[0].landmark[1]
        data.update({"landmark_1": [lm.x, lm.y, lm.z]})

    out_path = os.path.join(output_dir, file.replace('.png', '.json'))
    with open(out_path, 'w') as f:
        json.dump(data, f, indent=2)
