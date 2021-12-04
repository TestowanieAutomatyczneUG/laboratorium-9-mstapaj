from src.Environment import Environment


class Checker:
    def __init__(self):
        self.env = Environment()
        self.was_played = False

    def remainder(self):
        if self.env.getTime().hour >= 17:
            self.env.playWavFile('file')
            self.wavWasPlayed()

    def check_wav(self):
        return self.was_played

    def wavWasPlayed(self):
        self.was_played = True

    def resetWav(self):
        self.was_played = False
