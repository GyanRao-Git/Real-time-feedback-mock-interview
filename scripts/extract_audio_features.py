import librosa
import os
import json
import numpy as np

input_dir = './data/audio'
output_dir = './features/audio'

for file in os.listdir(input_dir):
    if not file.endswith('.mp3'):
        continue

    path = os.path.join(input_dir, file)
    y, sr = librosa.load(path, sr=16000)

    f0 = librosa.yin(y, fmin=50, fmax=500, sr=sr)
    pitch_avg = float(np.mean(f0))

    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    mfcc_means = mfccs.mean(axis=1).tolist()

    intervals = librosa.effects.split(y, top_db=30)
    total_speech = sum((end - start) for start, end in intervals)
    silence_rate = (len(y) - total_speech) / len(y)

    result = {
        "video": file.replace('.mp3', ''),
        "pitch_avg": pitch_avg,
        "mfcc_means": mfcc_means,
        "silence_rate": silence_rate
    }

    out_path = os.path.join(output_dir, file.replace('.mp3', '.json'))
    with open(out_path, 'w') as f:
        json.dump(result, f, indent=2)
