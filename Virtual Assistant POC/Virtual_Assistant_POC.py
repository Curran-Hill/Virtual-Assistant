import speech_recognition
import pyttsx3
import threading


class Assistant:
    
    def __init__(self):
        
        self.recognizer = speech_recognition.Recognizer()

        threading.Thread(target=self.run_assistant).start()

    def run_assistant(self):
        while True:
    
            try:
        
                with speech_recognition.Microphone() as mic:
            
                    self.recognizer.dynamic_energy_threshold = True
                    self.recognizer.adjust_for_ambient_noise(mic, duration=2)
                    self.recognizer.pause_threshold = 2
            
                    audio = self.recognizer.listen(mic)
            
                    text = self.recognizer.recognize_google(audio)
                    text=text.lower()
            
                    if "computer" in text:
                        print(f"Go Ahead... \n")
                        
                        audio = self.recognizer.listen(mic)
            
                        text = self.recognizer.recognize_google(audio)
                        text=text.lower()
                
                        print(f"#RECOGNIZED# {text} \n")

            except speech_recognition.UnknownValueError:
                self.recognizer = speech_recognition.Recognizer()
                continue

Assistant()