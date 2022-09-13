# youtube.com/watch?v=Q0lHb-FCATk
# pip3.8 install pdfplumber gtts art

from datetime import datetime
from art import tprint
from gtts import gTTS
import pdfplumber
from pathlib import Path

def pdf_to_mp3(file_path = 'test.pdf', language = 'en'):    
    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':
        
        print(f'[+] Original file: {Path(file_path).name}')
        print(f'[+] Processing...')
        
        with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:
            pages = [page.extract_text() for page in pdf.pages]
        
        text = ''.join(pages)
        text = text.replace('\n', '')
        
        my_audio = gTTS(text=text, lang=language, slow=False)
        file_name = Path(file_path).stem
        my_audio.save(f'{file_name}.mp3')
        
        return f'[+] {file_name}.mp3 saved successfully!\n---Have a good day---'
    
    else:
        return 'File not exists, check the file in path'    

def main():
    start = datetime.now()
    #--------- the code  
    tprint('PDF>>TO>>MP3', font='bulbhead')
    file_path = input("\nEnter a file's path: ")
    language = input("Choose language, for example 'en' or 'ru': ")
    print(pdf_to_mp3(file_path=file_path, language=language))
    #--------- quit code
    end = datetime.now()
    print(f'[+] lead time {str(end-start)}')


if __name__ == '__main__':
    main()