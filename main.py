from gtts import gTTS
from playsound import playsound

class TextToSpeechBot:
    def speak(self, text):
        tts = gTTS(text=text, lang='en')
        tts.save('output.mp3')
        playsound('output.mp3')

    def run(self):
        while True:
            text = input("Enter text to speak (or 'exit' to quit): ")

            if text.lower() == "exit":
                break

            self.speak(text)

if __name__ == '__main__':
    bot = TextToSpeechBot()
    bot.run()
