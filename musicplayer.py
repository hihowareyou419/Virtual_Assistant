import pygame
import json

class MusicPlayer:
    global v
    def __init__(self, config_File, v):
        pygame.mixer.init()
        self.config = None
        with open(config_File, "r") as f:
            self.config = json.load(f)
        if self.config is None:
            print("Error loading audio, music offline")
        self.currentTrack = None
        self.volume = v
    def displayTracks(self, trackType = "music"):
        for i, t in enumerate(self.config[trackType]):
            print(f"{i}: {t['trackname']}")
    def loadTrack(self, i, trackType = "music"):
        self.currentTrack = pygame.mixer.Sound(self.config[trackType][i]["filename"])
        self.currentTrack.set_volume(self.volume)
    def changeVolume(self, v):
        self.volume = v
    def pause(self):
        pygame.mixer.pause()
    def resume(self):
        pygame.mixer.unpause()
    def play(self):
        self.currentTrack.play()