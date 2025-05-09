const {
  exec
} = require('child_process');
const fs = require('fs');
const path = require('path');

const audioDir = './data/audio';
const outputDir = './data/transcripts';

fs.readdirSync(audioDir).forEach(file => {
  if (!file.endsWith('.mp3')) return;
  const base = path.parse(file).name;
  const cmd = `whisper "${audioDir}/${file}" --language en --model base --output_dir ${outputDir}`;

  exec(cmd, (err) => {
    if (err) console.error(`Whisper error: ${base}`, err);
    else console.log(`Transcription done: ${base}`);
  });
});
