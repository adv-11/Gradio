import gradio as gr

def add_numbers(x,y):
    return x+y 

interface = gr.Interface(fn=add_numbers , 
                         inputs=[gr.Number(10) , gr.Number()],
                         outputs= gr.Number()
                         )

interface.launch()

