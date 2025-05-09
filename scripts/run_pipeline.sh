#!/bin/bash
echo "Extracting frames and audio..."
node scripts/extract_media.js

echo "Transcribing audio..."
node scripts/transcribe.js

echo "Analyzing verbal cues..."
node scripts/verbal_analysis.js

echo "Extracting visual features..."
python scripts/extract_visual.py

echo "Extracting audio features..."
python scripts/extract_audio_features.py

echo "Merging all features..."
python scripts/merge_features.py

echo "✅ All done. Check the output folder."

