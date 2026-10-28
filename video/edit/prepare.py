"""Extract the documented editorial cut from the downloaded source stream."""
from pathlib import Path
import subprocess
ROOT=Path(__file__).resolve().parent
ASSETS=ROOT/'assets'
ASSETS.mkdir(exist_ok=True)
# (source seconds, duration seconds): original audio is retained.
CUTS=[('request',3999.0,18.8),('brand',4068.0,3.8),('refine',4408.7,7.2),('logo',4438.0,5.6),('result',5274.0,10.8)]
for name,start,duration in CUTS:
 subprocess.run(['ffmpeg','-y','-loglevel','error','-ss',str(start),'-i',str(ROOT.parent/'source/stream.mp4'),'-t',str(duration),'-vf','scale=1600:900:force_original_aspect_ratio=decrease,pad=1600:900:(ow-iw)/2:(oh-ih)/2,fps=30','-c:v','libx264','-preset','fast','-crf','20','-c:a','aac','-ar','48000',str(ASSETS/f'{name}.mp4')],check=True)
for name,t in [('final',5277),('hook',5277)]:
 subprocess.run(['ffmpeg','-y','-loglevel','error','-ss',str(t),'-i',str(ROOT.parent/'source/stream.mp4'),'-frames:v','1',str(ASSETS/f'{name}.jpg')],check=True)

subprocess.run(['ffmpeg','-y','-loglevel','error','-ss','4870','-i',str(ROOT.parent/'source/stream.mp4'),'-t','14','-vn','-af','afade=t=in:d=0.2,afade=t=out:st=13:d=1','-c:a','aac',str(ASSETS/'bed.m4a')],check=True)
subprocess.run(['ffmpeg','-y','-loglevel','error','-i',str(ASSETS/'final.jpg'),'-vf','crop=500:285:220:240','-frames:v','1',str(ASSETS/'card.jpg')],check=True)
# Brand instruction audio predates the visible new card; use later real screen footage as B-roll.
subprocess.run(['ffmpeg','-y','-loglevel','error','-ss','4180','-i',str(ROOT.parent/'source/stream.mp4'),'-ss','4068','-i',str(ROOT.parent/'source/stream.mp4'),'-t','3.8','-map','0:v:0','-map','1:a:0','-vf','scale=1600:900:force_original_aspect_ratio=decrease,pad=1600:900:(ow-iw)/2:(oh-ih)/2,fps=30','-c:v','libx264','-preset','fast','-crf','20','-c:a','aac','-ar','48000',str(ASSETS/'brand.mp4')],check=True)
