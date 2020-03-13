import speech_recognition as sr  


#Sample rate is how often values are recorded 
sample_rate = 4800
#it is advisable to use powers of 2 such as 1024 or 2048 
chunk_size = 2048
                                                                   
r = sr.Recognizer()  

running = True
while running:
    with sr.Microphone(sample_rate = sample_rate, chunk_size = chunk_size) as source:    
        # to adjust the threshold with bg noise level 
        r.adjust_for_ambient_noise(source)                                                                   
        print("Speak:")                                                                                   
        audio = r.listen(source)   
        textCaptured = r.recognize_google(audio)
        try:
            print("You said " + textCaptured)
            if(textCaptured == 'stop'):
                running =  False
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
