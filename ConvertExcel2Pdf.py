import os
import win32com.client as win32
import pandas as pd

def excel_to_pdf(excel_path, pdf_path):
    excel_app = win32.Dispatch('Excel.Application')
    excel_app.Visible = False
    
    # Open Excel
    workbook = excel_app.Workbooks.Open(excel_path)
    
    # Convert
    try:
        workbook.ExportAsFixedFormat(0, pdf_path)
        print(f"Success：{excel_path} => {pdf_path}")
    except Exception as e:
        print(f"Failed：{excel_path}")

def convert_all_excel_to_pdf(folder):
    for filename in os.listdir(folder):
        if filename.endswith(".xlsx") or filename.endswith(".xls"):
            excel_path = os.path.join(folder, filename)
            file_name = os.path.basename(excel_path)
            pdf_name = os.path.splitext(file_name)[0] + ".pdf"
            pdf_path = os.path.join(folder+"/pdf", pdf_name)
            excel_to_pdf(excel_path, pdf_path)

if __name__ == "__main__":
    # Specify the folder where the Excel file you want to convert to PDF is located
    target_folder = os.getcwd()
    
    os.makedirs(target_folder+"/pdf", exist_ok=True)
    convert_all_excel_to_pdf(target_folder)
