# Pages Printer card demo

60-second 1920×1080, 30 fps HyperFrames edit of the supplied livestream:
https://youtube.com/live/E-uvVeSDXyE

YouTube metadata: “More release preparation — Day #67 | ARR: $5948”, October 28, 2026, 5,471 seconds. The linked stream is used as requested, regardless of the relative “yesterday” wording.

## Reproduce

Requires Python 3, yt-dlp, FFmpeg, Node.js 22+ and a local Chrome installation supported by HyperFrames.

From the repository root:

```bash
mkdir -p video/source
yt-dlp --no-playlist --extractor-args 'youtube:player_client=web_embedded' \
  -f 'bestvideo[height<=720]+bestaudio/best[height<=720]' \
  --merge-output-format mp4 -o 'video/source/stream.%(ext)s' \
  'https://youtube.com/live/E-uvVeSDXyE'
python3 video/edit/prepare.py
cd video/edit
npm run check
npx hyperframes@0.8.210 preview --background
npx hyperframes@0.8.210 render --quality delivery --output out/pages-printer-wonop-60s.mp4
```

The download is approximately 450 MB. Source downloads, extracted assets, private campaign files and generated renders are ignored by Git. YouTube may change download requirements; a download failure is not evidence that the footage is unavailable.

The published delivery also applies FFmpeg loudness normalization to −14 LUFS (true-peak target −1.5 dBTP), copying the HyperFrames video stream without re-encoding it. To match that delivery, render to an intermediate filename, then run:

```bash
ffmpeg -i intermediate.mp4 -c:v copy -af "loudnorm=I=-14:TP=-1.5:LRA=11" \
  -c:a aac -b:a 192k -ar 48000 -t 60 -movflags +faststart pages-printer-wonop-60s.mp4
```

## Edit decision list

| Output | Source seconds | Content |
| --- | --- | --- |
| 0–3.8 | Still at 5277 | Result-first hook |
| 3.8–22.6 | 3999–4017.8 | Ask for a Pages Printer coming-soon card |
| 22.6–26.4 | Audio 4068–4071.8; picture 4180–4183.8 | Brand assets instruction with later screen B-roll |
| 26.4–33.6 | 4408.7–4415.9 | Ask for design refinement |
| 33.6–39.2 | 4438–4443.6 | Correct logo on a dark background |
| 39.2–50 | 5274–5284.8 | Final card and creator reaction |
| 50–60 | Card crop from 5277 | Requested beta CTA |

Intro/outro music is retained from source seconds 4870 onward, with reduced gain and fades. Other clips retain their source speech and background sound. No new voiceover. Background audio retains its original rights. The full card-building process takes longer than this highlight; this is an edited recap, not a real-time speed claim. Custom-font implementation was still in progress, so the edit does not claim that feature was completed.

The annotations are a refinement of the HyperFrames `lt-clean-bar` registry pattern. This project retains the installed original under `compositions/lt-clean-bar.html` for reference; it is not mounted in the final film. Actual scenes use scoped, editable sub-compositions.
