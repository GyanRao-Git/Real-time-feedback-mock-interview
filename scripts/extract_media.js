const fs = require('fs');
const path = require('path');
const ffmpeg = require('fluent-ffmpeg');

const inputDir = './data/video';
const outputFrames = './data/frames';
const outputAudio = './data/audio';

fs.readdirSync(inputDir).forEach(file => {
  if (!file.endsWith('.mp4')) return;
  const base = path.parse(file).name;

  // Extract frames
  ffmpeg(path.join(inputDir, file))
    .output(`${outputFrames}/${base}-%04d.png`)
    .outputOptions(['-vf fps=1'])
    .on('end', () => console.log(`Frames extracted: ${base}`))
    .run();

  // Extract audio
  ffmpeg(path.join(inputDir, file))
    .noVideo()
    .output(`${outputAudio}/${base}.mp3`)
    .on('end', () => console.log(`Audio extracted: ${base}`))
    .run();
});
