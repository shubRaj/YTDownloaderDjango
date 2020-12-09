import urllib.request,urllib.parse
import json
from collections import namedtuple
class YouTubeDownloader:
    def __init__(self,url):
        parsed = urllib.parse.urlparse(url)
        video_id=urllib.parse.parse_qs(parsed.query)["v"]
        self._videoInfo = urllib.parse.unquote(str(urllib.request.urlopen("https://www.youtube.com/get_video_info?video_id=%s"%video_id[0]).read()))
        for videoFile in self._videoInfo.split("&"):
            if videoFile.startswith("player_response"):
                streams = json.loads(videoFile.lstrip("player_response="))
                self._thumbnail = streams["videoDetails"]["thumbnail"]["thumbnails"][-1]["url"]
                self._name = streams["videoDetails"]["title"].replace("+"," ")
                streams = streams["streamingData"]["formats"]+streams["streamingData"]["adaptiveFormats"]
                videoStream = namedtuple("stream",("width","height","size","url","type"))
                self._all = [videoStream(stream.get("width"),stream.get("height"),stream.get("contentLength"),urllib.parse.unquote(stream.get("url")),stream.get("mimeType")) for stream in streams]
    def links(self):
        return self._all
    def thumbnail(self):
        return self._thumbnail
    def title(self):
        return self._name
if __name__=="__main__":
    c = YouTubeDownloader("https://www.youtube.com/watch?v=J-bdUWzdXXQ")