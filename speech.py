import speech_recognition as sr
import pyttsx3
  
# Initializing the recognizer
recog = sr.Recognizer()
  
# Function to convert text to
# speech
def SpeakText(command):
      
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()
    
# Funtion to listen for speech and returns Value as string
# Returns -1 and error code if failed,
# Retuens 1 and Bookname if runs correctly

def bookName():
    try:
              
        # use the microphone as source for input.
        with sr.Microphone() as source2:
                  
            # Adjust the energy threshold based on the surrounding noise level
            recog.adjust_for_ambient_noise(source2, duration=0.2)
                  
            audio2 = recog.listen(source2)
                  
            # Using Gpogle Recogniser to recognize audio, needs active internet.
            MyText = recog.recognize_google(audio2)
            MyText = MyText.lower()
      
            code = 1
            return code, MyText;
                  
    except sr.RequestError as e:
        # print("Could not request results; {0}".format(e))
        errorText = "Could not request results"
        code = -1
        return code, MyText;
              
    except sr.UnknownValueError:
        errorText = "Unknown error occured"
        code = -1
        return code, MyText;
