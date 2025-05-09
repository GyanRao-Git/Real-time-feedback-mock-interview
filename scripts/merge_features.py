import os
import json
import pandas as pd

def load_json_folder(folder):
    data = []
    for file in os.listdir(folder):
        if not file.endswith('.json'): continue
        with open(os.path.join(folder, file)) as f:
            data.append(json.load(f))
    return pd.DataFrame(data)

verbal_df = load_json_folder('./features/verbal')
audio_df = load_json_folder('./features/audio')
visual_df = load_json_folder('./features/visual')

# Merge on 'video'
df = verbal_df.merge(audio_df, on='video', how='left')
df = df.merge(visual_df, on='video', how='left')

# Save final datasets
df.to_csv('./output/features.csv', index=False)
df.to_json('./output/features.json', orient='records', indent=2)
print("Final CSV and JSON saved.")
