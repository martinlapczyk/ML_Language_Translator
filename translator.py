import gradio as gr
from transformers import pipeline
def translate_german(from_text):
    translation_pipeline=pipeline(model="Helsinki-NLP/opus-mt-en-de")
    results=translation_pipeline(from_text)
    return results[0]['translation_text']
def translate_dutch(from_text):
    translation_pipeline=pipeline(model="Helsinki-NLP/opus-mt-en-nl")
    results=translation_pipeline(from_text)
    return results[0]['translation_text']
def translate_russian(from_text):
    translation_pipeline=pipeline(model="Helsinki-NLP/opus-mt-en-ru")
    results=translation_pipeline(from_text)
    return results[0]['translation_text']
def translate_french(from_text):
    translation_pipeline=pipeline(model="Helsinki-NLP/opus-mt-en-fr")
    results=translation_pipeline(from_text)
    return results[0]['translation_text']
choice=input("Select a language")
match choice:
    case 'german':
        interface=gr.Interface(fn=translate_german,inputs=gr.inputs.Textbox(lines=2, placeholder="Enter text to translate"), outputs='text')
        interface.launch()
    case 'dutch':
        interface=gr.Interface(fn=translate_dutch,inputs=gr.inputs.Textbox(lines=2, placeholder="Enter text to translate"), outputs='text')
        interface.launch()
    case 'russian':
        interface=gr.Interface(fn=translate_russian,inputs=gr.inputs.Textbox(lines=2, placeholder="Enter text to translate"), outputs='text')
        interface.launch()
    case 'french':
        interface=gr.Interface(fn=translate_french,inputs=gr.inputs.Textbox(lines=2, placeholder="Enter text to translate"), outputs='text')
        interface.launch()   
    case _:
        print("That is not an option")
