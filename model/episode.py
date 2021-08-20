from dataclasses import dataclass
from datetime import datetime
from time import mktime


@dataclass
class Episode:
  title: str
  summary: str
  date: datetime
  tags: list
  duration: int
  season_number: str
  episode_number: str
    
  def __init__(self, item: dict):
    self.title = item['title']
    self.summary = item['summary']
    self.date = datetime.fromtimestamp(mktime(item['published_parsed']))
    self.duration = round(int(item['itunes_duration']) / 60, 0)
    self.season_number = item['itunes_season']
    self.episode_number = item['itunes_episode']
