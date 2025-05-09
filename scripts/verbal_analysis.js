const fs = require('fs');
const path = require('path');
const Sentiment = require('sentiment');
const sentiment = new Sentiment();

const transcriptDir = './data/transcripts';
const outputDir = './features/verbal';

const fillers = ['um', 'uh', 'like', 'you know'];
const pronouns = ['i', 'we', 'you', 'he', 'she', 'they'];

fs.readdirSync(transcriptDir).forEach(file => {
  if (!file.endsWith('.txt')) return;
  const base = path.parse(file).name;
  const text = fs.readFileSync(path.join(transcriptDir, file), 'utf8').toLowerCase();
  const words = text.split(/\s+/);
  const wordCount = words.length;

  const fillerCount = words.filter(w => fillers.includes(w)).length;
  const pronounCount = words.filter(w => pronouns.includes(w)).length;
  const sentimentScore = sentiment.analyze(text).score;

  const result = {
    video: base,
    wordCount,
    fillerCount,
    pronounCount,
    sentimentScore
  };

  fs.writeFileSync(`${outputDir}/${base}.json`, JSON.stringify(result, null, 2));
  console.log(`Verbal features saved for: ${base}`);
});
