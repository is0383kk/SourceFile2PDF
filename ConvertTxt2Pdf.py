import os
from fpdf import FPDF

class PDF(FPDF):
    def __init__(self):
        super().__init__()
        self.add_page()
        self.set_auto_page_break(auto=True, margin=15)
        self.set_font("Arial", size=12)

    def add_txt_content(self, txt_content):
        for line in txt_content.split('\n'):
            self.cell(200, 10, txt=line.encode('latin-1', 'replace').decode('latin-1'), ln=True)

def txt_to_pdf(txt_path, pdf_path):
    # Open txt file with UTF-8 encoding
    with open(txt_path, 'r', encoding='utf-8') as txt_file:
        txt_content = txt_file.read()

    # Initialize the PDF
    pdf = PDF()
    pdf.add_txt_content(txt_content)

    # Convert        
    try:
        pdf.output(pdf_path)
        print(f"Success：{txt_path} => {pdf_path}")
    except Exception as e:
        print(f"Failed：{pdf_path}")

def convert_all_txt_to_pdf(folder):
    for filename in os.listdir(folder):
        if filename.endswith(".txt"):
            txt_path = os.path.join(folder, filename)
            file_name = os.path.basename(txt_path)
            pdf_name = os.path.splitext(file_name)[0] + ".pdf"
            pdf_path = os.path.join(folder+"/pdf", pdf_name)
            txt_to_pdf(txt_path, pdf_path)

if __name__ == "__main__":
    # Specify the folder where the txt file you want to convert to PDF is located
    target_folder = os.getcwd()

    os.makedirs(target_folder+"/pdf", exist_ok=True)
    convert_all_txt_to_pdf(target_folder)
