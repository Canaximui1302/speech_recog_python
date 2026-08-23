import speech_recognition as sr

# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()

file = sr.AudioFile('test.wav')
r.pause_threshold = 1

# Reading Microphone as source
# listening the speech and store in audio_text variable

""" For testing with file
with file as source:
    print("Talk")
    audio_text = r.record(source)
    print("Time over, thanks")
    # recoginze_() method will throw a request
    # error if the API is unreachable,
    # hence using exception handling
    
    try:
        # using google speech recognition
        print("Text: "+r.recognize_google(audio_text))
    except:
         print("Sorry, I did not get that")
"""

# For testing with live recording
with sr.Microphone() as source:
    print("Talk")
    audio_text = r.listen(source, phrase_time_limit=6)
    print("Time over, thanks")
    # recoginze_() method will throw a request
    # error if the API is unreachable,
    # hence using exception handling
    
    try:
        # using google speech recognition
        print("Input recognized from recording: "+r.recognize_google(audio_text))
    except:
        print("Sorry, I did not get that")