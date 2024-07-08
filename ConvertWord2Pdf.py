import os
import win32com.client as win32

def word_to_pdf(word_path, pdf_path):
    word_app = win32.Dispatch('Word.Application')
    word_app.Visible = False

    # Open Word
    doc = word_app.Documents.Open(word_path)

    # Convert
    try:
        doc.SaveAs(pdf_path, FileFormat=17)
        print(f"Success：{word_path} => {pdf_path}")
        doc.Close()
    except Exception as e:
        print(f"Failed：{word_path}")

def convert_all_word_to_pdf(folder):
    for filename in os.listdir(folder):
        if filename.endswith(".docx") or filename.endswith(".doc"):
            word_path = os.path.join(folder, filename)
            file_name = os.path.basename(word_path)
            pdf_name = os.path.splitext(file_name)[0] + ".pdf"
            pdf_path = os.path.join(folder+"\pdf", pdf_name)
            word_to_pdf(word_path, pdf_path)

if __name__ == "__main__":
    # Specify the folder where the Word file you want to convert to PDF is located
    target_folder = os.getcwd()
    
    os.makedirs(target_folder+"/pdf", exist_ok=True)
    convert_all_word_to_pdf(target_folder)
