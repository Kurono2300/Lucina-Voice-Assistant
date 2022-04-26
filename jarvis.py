import speech_recognition
import pyttsx3 as tts
import sys
import wikipedia
import pywhatkit as kit

from datetime import date
from neuralintents import GenericAssistant
from importlib_metadata import re, os
from googletrans import Translator

# Esto es para ver las voces del sistema
# voices = speaker.getProperty('voices')
# print(voices[0])
# print(voices[1])


recognizer = speech_recognition.Recognizer()

speaker = tts.init()
speaker.setProperty('rate', 150 )
translator = Translator()

todo_list = ['Ir de Compras', 'Limpiar Habitacion']


def crear_nota():
    global recognizer

    speaker.say("Que quieres agrear a tu nota?")
    speaker.runAndWait()
    print("Escuchando")

    done = False

    while not done:
        try:
            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic, timeout=2, phrase_time_limit=3)

                note = recognizer.recognize_google(audio)
                note = note.lower()

                speaker.say("Como deseas llamar el documento?")
                speaker.runAndWait()
                print("Escuchando")

                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic, timeout=2, phrase_time_limit=3)

                filename = recognizer.recognize_google(audio)
                filename = filename.lower()

            with open(filename, 'w') as f:
                f.write(note)
                done = True
                speaker.say(f"Nota {filename} creada satisfactoriamente")    
                speaker.runAndWait()

        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            speaker.say("No he entendido tu solicitud. Podrias repetirlo?")
            speaker.runAndWait()


def agregar_todo():
    global recognizer
    speaker.say("Que quieres agrear a tus que haceres?")
    speaker.runAndWait()
    print("Escuchando")

    done = False
    while not done:
        try:
            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic, timeout=2, phrase_time_limit=3)

                item = recognizer.recognize_google(audio)
                item = item.lower()

                todo_list.append(item)
                done = True

                speaker.say("He agregado el dato a tu lista de que haceres.")
                speaker.runAndWait()

        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            speaker.say("No he entendido tu solicitud. Podrias repetirlo?")
            speaker.runAndWait()


def mostrar_todo():
    global recognizer
    speaker.say("Tu lista de que haceres tiene los siguientes elementos:")
    for item in todo_list:
        speaker.say(item)
    speaker.runAndWait()






def tu_bienvenida():
    speaker.say("Bienvenido Maestro, que necesitas?")
    speaker.runAndWait()

def adios():
    speaker.say("Hasta Pronto.")
    speaker.runAndWait()
    sys.exit(0)

def fecha():
    today = date.today()
    fecha_string = today.strftime("%d/%m/%Y")
    speaker.say(f"La fecha de hoy es {fecha_string}")
    speaker.runAndWait()





def wikipedia_data():
    global recognizer

    speaker.say("Que deseas investigar?")
    speaker.runAndWait()
    print("Escuchando")

    done = False

    while not done:
        try:
            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic, timeout=2, phrase_time_limit=3)

                busqueda = recognizer.recognize_google(audio, language="es-HN")
                busqueda = busqueda.lower()

                try:
                    
                    wikipedia.set_lang("es")
                    resultados = wikipedia.summary(busqueda,sentences=3)   
                    #Esto es usando el traductor                 
                    # print(resultados)
                    # traduccion = translator.translate(resultados,dest='es',src='auto')
                    # print(traduccion.text)
                    # speaker.say(f"Segun Wikipedia. {traduccion.text}")
                    speaker.say(f"Segun Wikipedia. {resultados}")
                    done = True
                    speaker.runAndWait()
                    
                except:
                    speaker.say("No he entendido, podrias repetirlo?")
                    print(busqueda)
                    speaker.runAndWait()
                

        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            speaker.say("No he entendido tu solicitud. Podrias repetirlo?")
            speaker.runAndWait()
    


def play_youtube():
    global recognizer

    speaker.say("Deseas reproducir musica en Ingles o Español?")
    speaker.runAndWait()
    print("Escuchando")

    done = False

    with speech_recognition.Microphone() as mic:
        recognizer.adjust_for_ambient_noise(mic,duration=0.2)
        seleccionidioma = recognizer.listen(mic,timeout=1,phrase_time_limit=2)

        seleccion = recognizer.recognize_google(seleccionidioma, language="es-HN")
        seleccion = seleccion.lower()
        print(seleccion)

    if 'inglés' in seleccion:
            while not done:
                try:
                    with speech_recognition.Microphone() as mic:
                        speaker.say("Que cancion deseas reproducir?")
                        speaker.runAndWait()
                        print("Escuchando")
                        recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                        audio = recognizer.listen(mic, timeout=2, phrase_time_limit=3)

                        busqueda = recognizer.recognize_google(audio, language="en")
                        busqueda = busqueda.lower()

                        try:
                            traduccion = translator.translate(busqueda,dest='es',src='auto')
                            speaker.say(f"Reproduciendo: {traduccion.text}")
                            kit.playonyt(busqueda)                   
                            done = True
                            speaker.runAndWait()
                            
                        except:
                            speaker.say("No he entendido, podrias repetirlo?")
                            print(busqueda)
                            speaker.runAndWait()
                        
                except speech_recognition.UnknownValueError:
                    recognizer = speech_recognition.Recognizer()
                    speaker.say("No he entendido tu solicitud. Podrias repetirlo?")
                    speaker.runAndWait()

    elif 'español' in seleccion:
            while not done:
                try:
                    with speech_recognition.Microphone() as mic:
                        speaker.say("Que cancion deseas reproducir?")
                        speaker.runAndWait()
                        print("Escuchando")
                        recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                        audio = recognizer.listen(mic, timeout=2, phrase_time_limit=3)

                        busqueda = recognizer.recognize_google(audio,language="es-HN")
                        busqueda = busqueda.lower()

                        try:
                            speaker.say(f"Reproduciendo: {busqueda}")
                            kit.playonyt(busqueda)                   
                            done = True
                            speaker.runAndWait()
                            
                        except:
                            speaker.say("No he entendido, podrias repetirlo?")
                            print(busqueda)
                            speaker.runAndWait()
                        
                except speech_recognition.UnknownValueError:
                    recognizer = speech_recognition.Recognizer()
                    speaker.say("No he entendido tu solicitud. Podrias repetirlo?")
                    speaker.runAndWait()









mappings = {
    "bienvenida":tu_bienvenida,
    "crear_nota":crear_nota,
    "agregar_todo":agregar_todo,
    "mostrar_todo":mostrar_todo,
    "adios":adios,
    "fecha":fecha,
    "wikipedia":wikipedia_data,
    "youtube":play_youtube
}    


assistant = GenericAssistant('intents.json', intent_methods=mappings)
assistant.train_model()


while True:
    try:
        with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                print("Escuchando")
                audio = recognizer.listen(mic, timeout=2, phrase_time_limit=3)

                message = recognizer.recognize_google(audio, language="es-HN")
                message = message.lower()

                assistant.request(message)
                # print(message)
                # speaker.say(message)

    except speech_recognition.UnknownValueError:
        recognizer = speech_recognition.Recognizer()
        # speaker.say("No he entendido.")
        speaker.runAndWait()         


