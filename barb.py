import youtube_dl
import json

ydl = youtube_dl.YoutubeDL({
                            'playliststart' : 1,
                            'playlistend' : 10,
                            'matchtitle' : "Super|SMM|Mario",
                            'quiet' : True,
                            })

barb = ydl.extract_info(
    'https://www.youtube.com/user/VideoGameSeppuku/videos', download=False)
carl = ydl.extract_info(
    'https://www.youtube.com/user/CarlSagan42/videos', download=False)

print(barb['entries'][0]['webpage_url'])
#print(json.dumps(result, sort_keys=True, indent=4))
