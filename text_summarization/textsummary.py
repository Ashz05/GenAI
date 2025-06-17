import torch
import gradio as gr

# Use a pipeline as a high-level helper
from transformers import pipeline


model_path=("../Model/models--sshleifer--distilbart-cnn-12-6/snapshots"
            "/a4f8f3ea906ed274767e9906dbaede7531d660ff")
text_summary= pipeline("summarization", model="sshleifer/distilbart-cnn-12-6",
                torch_dtype=torch.bfloat16)

#Example text
# A gaming computer, also known as a gaming PC, is a specialized personal computer designed for playing PC games at high standards.
#  They typically differ from mainstream personal computers by using high-performance graphics cards,
#  a high core-count CPU with higher raw performance and higher-performance RAM. 
# Gaming PCs are also used for other demanding tasks such as video editing. 
# While often in desktop form, gaming PCs may also be laptops or handhelds.

#Note : Maxium length is set to 142 , thus ensure you have summary text length below the 142 range
# That is range between (>0 and <142)


def summary(input):
    output=text_summary(input)
    return output[0]['summary_text']

gr.close_all()


#demo=gr.Interface(fn=summary, inputs="text",outputs="text")
demo=gr.Interface(fn=summary,
                  inputs=[gr.Textbox(label="Input text to summarize",lines=6)],
                  outputs=[gr.Textbox(label="Summarized text",lines=4)],
                  title="TextSummaryAI : Text Summarizer",
                  description="This project is used to summarize the text by providing the input")


demo.launch()

'''After done summarizing the text we can save the text as csv,
By clicking the flag option given through the gradio link(provided in output terminal)
thus it is stored in gradio file ensuring the text are stored'''

