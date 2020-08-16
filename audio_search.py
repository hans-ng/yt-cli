#TODO: make this class iterable

from youtubesearchpython.videos__search import SearchVideos

class audio_search(SearchVideos):
    def __iter__(self):
        return self.__iter__()