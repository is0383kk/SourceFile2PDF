import os
from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('IPAexGothic', '', 12)
        self.cell(0, 10, 'Java to PDF Converter', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('IPAexGothic', '', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

def java_to_pdf(java_path, pdf_path):
    # Open Java file with UTF-8 encoding
    with open(java_path, 'r', encoding='utf-8') as java_file:
        java_content = java_file.read()

    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_font('IPAexGothic', '', os.getcwd()+'/ipaexg.ttf', uni=True)
    pdf.set_font('IPAexGothic', size=12)

    max_width = pdf.w - 2 * pdf.l_margin
    line_height = pdf.font_size * 1.5

    for line in java_content.split('\n'):
        pdf.multi_cell(max_width, line_height, line.encode('utf-8').decode('utf-8'))
    
    # Convert
    try:
        pdf.output(pdf_path)
        print(f"Success：{java_path} => {pdf_path}")
    except Exception as e:
        print(f"Failed：{pdf_path}")

def convert_all_java_to_pdf(folder):
    for filename in os.listdir(folder):
        if filename.endswith(".java"):
            java_path = os.path.join(folder, filename)
            file_name = os.path.basename(java_path)
            pdf_name = os.path.splitext(file_name)[0] + ".pdf"
            pdf_path = os.path.join(folder+"/pdf", pdf_name)
            java_to_pdf(java_path, pdf_path)

if __name__ == "__main__":
    # Specify the folder where the Java file you want to convert to PDF is located
    target_folder = os.getcwd()

    os.makedirs(target_folder+"/pdf", exist_ok=True)
    convert_all_java_to_pdf(target_folder)
