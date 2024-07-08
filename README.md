# File2PDFTool  
A Python script to convert files in a specified folder to PDF.  
※ By default, the files in the current directory are targeted.  

| Program Name           | Description                                           |
|------------------------|-------------------------------------------------------|
| ConvertExcel2Pdf.py    | Convert all Excel files in the folder to PDF          |
| ConvertWord2Pdf.py     | Convert all Word files in the folder to PDF           |
| ConvertTxt2Pdf.py      | Convert all text files in the folder to PDF           |
| ConvertJava2Pdf.py     | Convert all Java files in the folder to PDF           |
| ConvertHtml2Pdf.py     | Convert all HTML files in the folder to PDF           |
  
※ Files with "_jp" in their names support Japanese text.

## Requirements  
Environment information confirmed to work:  
- Python 3.11.3
- The following Python packages:
  - `os`
  - `win32com.client`
  - `pandas`: `2.2.2`
  - `fpdf2`: `2.7.9`
※ Please explicitly specify version 2.x and install using the following command:
```bash
python -m pip install fpdf2    
```

# Appendix
[Tutorial in English - fpdf2](https://py-pdf.github.io/fpdf2/Tutorial.html)

# File2PDFTool  
指定したフォルダ内のファイルをPDFに変換するPythonスクリプトです。  
※デフォルトではカレントディレクトリ内のファイル群が対象です  

|プログラム名|説明|
|---|---|
|ConvertExcel2Pdf.py|フォルダ内のExcelファイルをまとめてPDFに変換する|
|ConvertWord2Pdf.py|フォルダ内のWordファイルをまとめてPDFに変換する|
|ConvertTxt2Pdf.py|フォルダ内のテキストファイルをまとめてPDFに変換する|
|ConvertJava2Pdf.py|フォルダ内のJavaファイルをまとめてPDFに変換する|
|ConvertHtml2Pdf.py|フォルダ内のJavaファイルをまとめてPDFに変換する|
  
※「_jp」と付いているファイルは日本語テキストに対応しています。  

## 必要条件  
以下動作確認済みの環境情報  
- Python 3.11.3
- 以下のPythonパッケージ
  - `os`
  - `win32com.client`
  - `pandas`：`2.2.2`
  - `fpdf2`：`2.7.9`
※以下のようにバージョン2系を明示的に指定してインストールしてください。
```bash
python -m pip install fpdf2    
```

# 付録  
[日本語チュートリアル - fpdf2](https://py-pdf.github.io/fpdf2/Tutorial-ja.html)
