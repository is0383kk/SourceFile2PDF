import os
from PyPDF2 import PdfMerger

def merge_pdfs(folder_path, output_path):
    merger = PdfMerger()

    for item in os.listdir(folder_path):
        if item.endswith('.pdf'):
            file_path = os.path.join(folder_path, item)
            merger.append(file_path)

    # Save the merged PDF file
    merger.write(output_path)
    merger.close()
    print(f"PDFs merged=>{output_path}")

if __name__ == "__main__":
    # Specify the folder where the txt file you want to merge PDFs is located
    target_folder = os.getcwd()
    output_path = os.getcwd() + "\merged.pdf"
    
    merge_pdfs(target_folder, output_path)
