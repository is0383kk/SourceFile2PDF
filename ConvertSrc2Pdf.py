import os
import sys
from fpdf import FPDF

class PDF(FPDF):
    # Header and Footer
    # If you can use Header and Footer, you can use the following code
    
    '''
    def header(self):
        self.set_font('helvetica', '', 10)
        self.cell(0, 10, 'src to PDF Converter', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('helvetica', '', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')
    '''

def src_to_pdf(src_path, pdf_path):
    # Open src file with UTF-8 encoding
    with open(src_path, 'r', encoding='utf-8') as src_file:
        src_content = src_file.read()

    pdf = PDF()
    pdf.set_font('helvetica', size=10)
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)

    for line in src_content.split('\n'):
        line = line.replace('\t', '    ')
        pdf.cell(w=0, h=pdf.font_size * 1.5 ,text=line.encode('utf-8').decode('utf-8'))
        pdf.ln()
    
    # Convert
    try:
        pdf.output(pdf_path)
        print(f"Success：{src_path} => {pdf_path}")
    except Exception as e:
        print(f"Failed：{pdf_path}")

def convert_all_src_to_pdf(folder):
    for filename in os.listdir(folder):
        if filename.endswith(str(sys.argv[1])):
            src_path = os.path.join(folder, filename)
            file_name = os.path.basename(src_path)
            pdf_name = os.path.splitext(file_name)[0] + ".pdf"
            pdf_path = os.path.join(folder+"/pdf", pdf_name)
            src_to_pdf(src_path, pdf_path)

if __name__ == "__main__":
    # Specify the folder where the src file you want to convert to PDF is located
    target_folder = os.getcwd()

    os.makedirs(target_folder+"/pdf", exist_ok=True)
    convert_all_src_to_pdf(target_folder)
