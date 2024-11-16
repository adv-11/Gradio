import gradio as gr

def add_numbers(x,y):
    return x+y 

def reverse_text(input_text):
    return input_text[::-1]

def slider (value):
    return 'Current Value is {value}'

options = ['A', 'B' , 'C']

def dropDown(value):
    return "Value you selected is ",value ,"."


from PIL import Image 

def convert (image_path):
    image = Image.open(image_path)
    gray_image = image.convert("L")
    return gray_image

#json

#label 

interface = gr.Interface(fn=convert , 
                         inputs=[gr.Image(type='filepath')],
                         outputs= gr.Image()
                        )

interface.launch()
