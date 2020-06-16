from __future__ import print_function
import os
import grpc
import math

from datetime import datetime
from time import sleep
from concurrent import futures

import translator_pb2
import translator_pb2_grpc

import PySimpleGUI as sg
import pyaudio
import wave
from tkinter import messagebox

def func():
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000
    CHUNK = int(RATE / 10)
    RECORD_SECONDS = 3
    audio = pyaudio.PyAudio()
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                rate=RATE, input=True,
                frames_per_buffer=CHUNK)
    messagebox.showinfo("Message Popup","Recording...")  
    print ("recording...")
    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    print ("finished recording")
    messagebox.showinfo("Message Popup","Finished Recording") 

    # stop Recording
    stream.stop_stream()
    stream.close()
    audio.terminate()
    
    file = open("aud.raw", "wb")
    file.write(b''.join(frames))
    file.close()
    

sg.theme('LightGreen')

layout = [[sg.Text('Please choose services you want to use', font='Courier')],
          [sg.Checkbox('Translator',default='0',key='translator' ,size =(40,1)),sg.Checkbox('Translator Multiline parallel only',default='0',key='translator multiline parallel only')],
          [sg.Checkbox('Translator Multiline parallel stream',default='0',key='translator multiline parallel stream',size =(40,1)),sg.Checkbox('Speech to text Translator',default='0',key = 'Speech to Text Translator')],
          [sg.Text('_'  * 80)],  

          [sg.Text('Please enter required input here:',font='Courier')],

          [sg.Text('Text to be translated', size=(20, 1)), sg.InputText('good morning',key='text')],
          [sg.Text('Destined Langauge', size=(20, 1)), sg.InputText('ja',key='dest')],
          [sg.Text('..'  * 70)], 

          [sg.Text('For multiline translator parallel only:', font='Courier')],
          [sg.Radio('Location','RAD1',size=(12, 1),default='0',key='path po') , sg.Radio('Text Box','RAD1',size=(12, 1),default='0',key='text po')],
          [sg.Text('Full path of the file', size=(20, 1)), sg.Input(key= 'path file po'), sg.FileBrowse()],
          [sg.Text('Text to be Translated', size=(20, 1)),sg.Multiline(key='multiline data po')],
          [sg.Text('Destined Language', size=(20, 1)), sg.InputText('hi',key='destpo')],
          [sg.Text('Max workers limit', size=(20, 1)), sg.InputText('60',key='max_workers_po')],
          [sg.Text('..'  * 70)], 
          
          [sg.Text('For multiline translator parallel stream:', font='Courier')],
          [sg.Radio('Location','RAD2',size=(12, 1),default='0',key='path ps') , sg.Radio('Text Box','RAD2',size=(12, 1),default='0',key='text ps')],
          [sg.Text('Full path of the file', size=(20, 1)), sg.Input(key= 'path file ps'), sg.FileBrowse()],
          [sg.Text('Text to be translated', size=(20, 1)),sg.Multiline(key='multiline data ps')],
          [sg.Text('Destined Language', size=(20, 1)), sg.InputText('hi',key='destps')],
          [sg.Text('Max workers limit', size=(20, 1)), sg.InputText('60',key='max_workers_ps')],
          [sg.Text('..'  * 70)], 
          
          [sg.Text('For speech to text conversion:', font='Courier')],
          [sg.Text('Record Speech', size=(20, 1)),sg.Button('Record Audio')],
          [sg.Text('_'  * 80)], 
          
          [sg.Submit(), sg.Cancel()]
         ]
Layout=[[sg.Column(layout,size=(600,700),scrollable=True)]]

window = sg.Window('Inputs', Layout)
w, h = sg.Window.get_screen_size()
window.size=(w,h)

event, values = window.read()
if event == 'Record Audio':
    func()

window.close()
    
    
def run():
    with open('mydomain.crt', 'rb') as f:
        trusted_certs = f.read()
    credentials = grpc.ssl_channel_credentials(root_certificates=trusted_certs)
    print("\n calling translator server---- \n")
    channel = grpc.secure_channel("localhost:3001",credentials)
    stub = translator_pb2_grpc.TranslatorStub(channel)
    s1=values['text']
    s2=values['dest']
    text = translator_pb2.Text(value=s1,dest=s2)
    response = stub.GoogTrans(text)
    with open("result"+".txt",'a+') as f:
        f.write("\nTranslator Server Output----\n")
        f.write("String given by Client to translate: "+ s1 + "\nDestined Langauge: "+ s2)
        f.write("\nTranslated String: "+response.value+"\n")
    f.close()
    
def run_translator(content):
    stub = translator_pb2_grpc.TranslatorStub(content[0])
    s2=values['destpo']
    Text = translator_pb2.Text(value=content[1],dest=s2)
    response = stub.GoogTrans(Text)
    return response.value
    
def write_func_po(responses):
    with open("result"+".txt",'a+') as f:
        for response in responses:
            f.write(response)
            if response!='\n':
                f.write('\n')
        f.close()
        
def run_parallel_only():
    with open("result"+".txt",'a+') as f:
        f.write("\nTranslator Server parallel computations Output----\n\n")
        f.close()
    with open('mydomain.crt', 'rb') as f:
        trusted_certs = f.read()
    credentials = grpc.ssl_channel_credentials(root_certificates=trusted_certs)
    print("\n calling translator server---- \n")
    channel = grpc.secure_channel("localhost:3001",credentials)
    startTime = datetime.now()
    executor = futures.ThreadPoolExecutor(max_workers=int(values['max_workers_po']))
    if values['path po']:
        with open(values['path file po'],'r') as f:
            limit=50000
            content=f.read()
            contents=[content[i:i+limit] for i in range(0, len(content), limit)]
            for cont in contents:
                data=cont.splitlines()
                executor = futures.ThreadPoolExecutor(max_workers=min(int(values['max_workers_po']),10**(int(math.log(len(data),10)))))
                responses=list(executor.map(run_translator,[[channel,line] for line in data]))
                write_func_po(responses)
    if values['text po']:
        data=values['multiline data po'].splitlines()
        #print(data)
        executor = futures.ThreadPoolExecutor(max_workers=min(int(values['max_workers_po']),10**(int(math.log(len(data),10)))))
        responses=list(executor.map(run_translator,[[channel,line] for line in data]))
        write_func_po(responses)   
    print("parallel only case :"+str(datetime.now() - startTime))
    

def run_stream_trans_req(dest_lang,contents):
    #print(contents)
    for content in contents:
        for line in content:
            yield translator_pb2.Text(value=line,dest=dest_lang)
    
def run_stream_trans(contents):
    stub = translator_pb2_grpc.TranslatorStub(contents[0])
    s2=values['destps']
    responses = stub.StreamTrans(run_stream_trans_req(s2,contents[1:]))
    return responses
    
def write_func_ps(responses):
    with open("result"+".txt",'a+') as f:
        for response in responses:
            for rep in response:
                f.write(rep.value)
                if rep.value!='\n':
                    f.write('\n')
        f.close()
        
def run_parallel_with_stream():
    with open("result"+".txt",'a+') as f:
        f.write("\nTranslator Server parallel stream computations Output----\n\n")
        f.close()
    with open('mydomain.crt', 'rb') as f:
        trusted_certs = f.read()
    credentials = grpc.ssl_channel_credentials(root_certificates=trusted_certs)
    print("\n calling translator server---- \n")
    channel = grpc.secure_channel("localhost:3001",credentials)
    startTime = datetime.now()
    if values['path ps']:
        with open(values['path file ps'],'r') as f:
            limit=50000
            content=f.read()
            contents=[content[i:i+limit] for i in range(0, len(content), limit)]
            #print(len(contents))
            for cont in contents:
                data=cont.splitlines()
                executor = futures.ThreadPoolExecutor(max_workers=min(int(values['max_workers_ps']),10**(int(math.log(len(data),10)))))
                responses=list(executor.map(run_stream_trans,[[channel,data[i:i+2]] for i in range(0,len(data),2) ]))
                write_func_ps(responses)
    if values['text ps']:
        #s2=values['destps']
        data=values['multiline data ps'].splitlines()
        executor = futures.ThreadPoolExecutor(max_workers=min(1000,10**(int(math.log(len(data),10)))))
        responses=list(executor.map(run_stream_trans,[[channel,data[i:i+2]] for i in range(0,len(data),2) ]))
        write_func_ps(responses)
    print("parallel streams case :"+str(datetime.now() - startTime))

def run3():
    with open("result"+".txt",'r') as f:
        sg.popup_scrolled(f.read(),size=(200, None))
    f.close()

def speech():
    with open("result"+".txt",'a+') as f:
        f.write("\nSpeech Server Output----\n")
        f.close()
    with open('mydomain.crt', 'rb') as f:
        trusted_certs = f.read()
    credentials = grpc.ssl_channel_credentials(root_certificates=trusted_certs)
    print("\n calling speech server---- \n")
    channel = grpc.secure_channel("localhost:3001",credentials)
    stub = translator_pb2_grpc.SpeechTranslatorStub(channel)
    # s1='aud.raw'
    with  open('aud.raw','rb') as f:
        s1=f.read()
        f.close()
    rtext = translator_pb2.audio(binary=s1)
    response = stub.translate(rtext)
    # print(response.value)
    with open("result"+".txt",'a+') as f:
        f.write(response.value)
    f.close()


if __name__ == '__main__':
    open("result"+".txt",'w').close()
    if values['translator']:run()
    if values['translator multiline parallel only']:run_parallel_only()
    if values['translator multiline parallel stream']:run_parallel_with_stream()
    if values['Speech to Text Translator']:speech()
    run3()
