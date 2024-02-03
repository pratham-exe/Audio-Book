import main

choice = int(input("""1. Play audio on terminal
2. Download audio as mp3 file
Please enter your choice: """))

if choice == 1:
    main.term_audio()
else:
    main.audio_file()
