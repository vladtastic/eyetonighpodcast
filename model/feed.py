from dataclasses import dataclass
from model.episode import Episode
import feedparser


@dataclass
class Feed:
    url: str = ''
    episodes = list
    
    def __init__(self, url: str):
      self.url = url
      self.episodes = [Episode(item) for item in feedparser.parse(self.url)['entries']]
