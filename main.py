from careerlens.pdf_parser import extract_resume_text

resume_path = "data\\uploads\\Modern Professional CV Resume.pdf"
resume_text = extract_resume_text(resume_path)
print(resume_text)