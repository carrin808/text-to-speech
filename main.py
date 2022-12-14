import pyttsx3



class TextToSpeech:
    engine: pyttsx3.Engine

    def __init__(self, voice, rate: int, volume: float):
        self.engine = pyttsx3.init()
        if voice:
            self.engine.setProperty('voice', voice)
        self.engine.setProperty('rate', rate)
        self.engine.setProperty('volume', volume)  # Between 0 and 1

    def text_to_speech(self, text: str, save: bool = False, file_name='output.mp3'):
        self.engine.say(text)
        print('I\'m speaking...')

        if save:

            self.engine.save_to_file(text, file_name)

        self.engine.runAndWait()

    def list_available_voices(self):
        voices: list = [self.engine.getProperty('voices')]

        for i, voice in enumerate(voices[0]):
            print(f'({i + 1}) {voice.name} {voice.age}: {voice.languages[0]} ({voice.gender}) [ID: {voice.id}]')


if __name__ == '__main__':
    tts = TextToSpeech('com.apple.speech.synthesis.voice.daniel', 200, 1.0)

    tts.text_to_speech('This will be converted to speech.', save=True, file_name='output.mp3')
