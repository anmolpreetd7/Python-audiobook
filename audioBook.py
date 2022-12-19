##Importing required Python modules for PDF and text to speech
import PyPDF2,pyttsx3

## Opening the pdf file
file_path= open('AnmolpreetDhindsaResume.pdf', 'rb')
file = PyPDF2.PdfFileReader(file_path)

speaker = pyttsx3.init()

##Extracting all pages in the pdf file to text
for page_num in range(file.numPages):
    text = file.getPage(page_num).extractText()
    clean_text= text.strip().replace('\n','')
    print(clean_text)


##Saving mp3 file in the same location as the pdf file
speaker.save_to_file(clean_text, 'audioresume.mp3')
speaker.runAndWait()

speaker.stop()


