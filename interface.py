import gradio as gr
from transformers import pipeline

def analytics_emo(x):
    data = classifier(x)[0]
    return data

if __name__ == "__main__":
    classifier = pipeline("text-classification", model="bhadresh-savani/bert-base-uncased-emotion", top_k=1)

    with gr.Blocks() as demo:
        gr.Markdown("<center><h1>Content Sentiment Analysis</h1> A simple Sentiment Analysis Tool</center>")
        with gr.Tab("Sentiment Analysis"):
            with gr.Row():
                with gr.Column(scale=1, min_width=600):
                    analytics_input = gr.Textbox(label="Text Content", lines=4, max_lines=100, placeholder="Analyzing Sentiment...")
                    analytics_button = gr.Button("Analyze")
                text_output = gr.Textbox(label="Result", lines=10, max_lines=100, placeholder="Sentiment...")
        analytics_button.click(analytics_emo, api_name="analytics", inputs=analytics_input, outputs=text_output)
    demo.launch(debug=True, server_name="0.0.0.0", share = True)
