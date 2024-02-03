import pypdf as pdf
from gtts import gTTS
import pyttsx3 as p

book = pdf.PdfReader("./Testing.pdf")
total_pages = len(book.pages)

final_text = ''
for i in range(total_pages):
    current_page = (book.pages[i]).extract_text()
    final_text += current_page


def term_audio():
    engine = p.init()
    engine.setProperty('rate', 125)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[11].id)
    engine.say(final_text)
    engine.runAndWait()


def audio_file():
    text_file = open("Testing.txt", "w")
    text_file.write(final_text)
    text_file.close()

    print("Please wait. This might take a while.")
    file = open("Testing.txt", "r").read().replace("\n", "")
    language = "en"
    speech = gTTS(text=str(file), lang=language, slow=False)
    speech.save("Testing.mp3")
    print("Audio saved!")
