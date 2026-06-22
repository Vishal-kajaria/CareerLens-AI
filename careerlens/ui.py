import gradio as gr
from careerlens.pdf_parser import extract_resume_text

def process_resume(file):
    if file is None:
        return "Please upload a resume."
    return extract_resume_text(file.name)

def create_ui():

    with gr.Blocks(title="CareerLens AI") as demo:

        gr.Markdown("# CareerLens AI")
        gr.Markdown("Upload a resume and extract text")

        resume_file = gr.File(
            label="Upload Resume",
            file_types=[".pdf"]
        )

        output_text = gr.Textbox(
            label="Extracted Resume Text",
            lines=20
        )

        submit_btn = gr.Button(
            "Analyze Resume"
        )

        submit_btn.click(
            fn=process_resume,
            inputs=resume_file,
            outputs=output_text
        )

    return demo