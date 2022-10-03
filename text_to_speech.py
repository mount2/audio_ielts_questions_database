import json 
import os 
import pandas as pd
# Import the required module for text 
# to speech conversion
from gtts import gTTS
  
# This module is imported so that we can 
# play the converted audio
import os
  
# # The text that you want to convert to audio
# mytext = '''Tell me about the kind of accommodation you live in?'''
  
# # Language in which you want to convert
language = 'en'
import re 

questions = pd.read_csv('ielts_questions.csv')

import time
def mp3_file_create(txt , file_path): 
    myobj = gTTS(text=txt, lang=language, slow=False)
    time.sleep(0.5)
    myobj.save(file_path)
    time.sleep(0.5)

questions = questions.dropna()
questions = questions.loc[questions['id']>=357]
file_path_col = []
for index,row in questions.iterrows(): 
    file_path = 'mp3_files/audio_num_'+str(row['id'])+'.mp3'
    txt = str(row['question']) + ' .'    
    txt = re.sub(r'\[','',txt)
    txt = re.sub(r'\]','',txt)
    file_path_col.append(file_path)
    mp3_file_create(txt,file_path)
    print(txt)

#questions['file_path'] = file_path_col
#questions.to_csv('question_with_audio_link.csv',index=False)