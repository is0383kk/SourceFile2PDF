# SourceFile2PDFTool  
A Python script to convert files in a specified folder to PDF.  
※ By default, the files in the current directory are targeted.   
※ Files with "_jp" in their names support Japanese text.  

| Program Name           | Description                                           |
|------------------------|-------------------------------------------------------|
| ConvertSrc2Pdf(_jp).py      | Convert all Source Code in the folder to PDF          |
| ConvertExcel2Pdf.py    | Convert all Excel files in the folder to PDF          |
| ConvertWord2Pdf.py     | Convert all Word files in the folder to PDF           |

## Usage：ConvertSrc2Pdf.py  
１．Place the converted source code as follows:  

SourceFile2PDFTool  
　|- ConvertSrc2Pdf.py  
　|- ConvertSrc2Pdf_jp.py  
　|- ipaexg.ttf  
　|- Sample001.java  
　|- Sample002.java  

２．Convert Java files to PDF using ```ConvertSrc2Pdf.py```  

```powershell
$ python ConvertSrc2Pdf.py .java
```
or  
```powershell
$ python ConvertSrc2Pdf_jp.py .java
```

３．PDF is generated

SourceFile2PDFTool  
　|- ConvertSrc2Pdf.py  
　|- ConvertSrc2Pdf_jp.py  
　|- ipaexg.ttf  
　|- Sample001.java  
　|- Sample002.java  
　|- Sample001.pdf  
　|- Sample002.pdf  

If you get any of the following errors, use ```ConvertSrc2Pdf_jp.py```  
```fpdf.errors.FPDFUnicodeEncodingException```

## Requirements  
Environment information confirmed to work:  
- Python 3.11.3
- The following Python packages:
  - `os`
  - `sys`  
  - `win32com.client`
  - `fpdf2`: `2.7.9`
※ Please explicitly specify version 2.x and install using the following command:
```bash
python -m pip install fpdf2    
```

# Appendix
[Tutorial in English - fpdf2](https://py-pdf.github.io/fpdf2/Tutorial.html)

---

# SourceFile2PDFTool  
指定したフォルダ内のファイルをPDFに変換するPythonスクリプトです。  
※デフォルトではカレントディレクトリ内のファイル群が対象です。  
※「_jp」と付いているファイルは日本語テキストに対応しています。  

|プログラム名|説明|
|---|---|
|ConvertSrc2Pdf(_jp).py      | フォルダ内のソースコードをまとめてPDFに変換する|
|ConvertExcel2Pdf.py|フォルダ内のExcelファイルをまとめてPDFに変換する|
|ConvertWord2Pdf.py|フォルダ内のWordファイルをまとめてPDFに変換する|
  
## 使い方：ConvertSrc2Pdf_jp.py  
１．以下フォルダ構造になるようにPDF変換したいファイルを配置する（Javaファイルの例）:  

SourceFile2PDFTool  
　|- ConvertSrc2Pdf.py  
　|- ConvertSrc2Pdf_jp.py  
　|- ipaexg.ttf  
　|- Sample001.java  
　|- Sample002.java  

２．```ConvertSrc2Pdf_jp.py```を実行する  

```powershell
$ python ConvertSrc2Pdf_jp.py .java
```

３．以下フォルダ構造でPDFが生成される  

SourceFile2PDFTool  
　|- ConvertSrc2Pdf.py
　|- ConvertSrc2Pdf_jp.py  
　|- ipaexg.ttf  
　|- Sample001.java  
　|- Sample002.java  
　|- Sample001.pdf  
　|- Sample002.pdf  

もし以下エラーが出る場合は、```ConvertSrc2Pdf_jp.py```を使用してください  
```fpdf.errors.FPDFUnicodeEncodingException```

## 必要条件  
以下動作確認済みの環境情報  
- Python 3.11.3
- 以下のPythonパッケージ
  - `os`
  - `sys`
  - `win32com.client`
  - `fpdf2`：`2.7.9`
※以下のようにバージョン2系を明示的に指定してインストールしてください。
```bash
python -m pip install fpdf2    
```

# 付録  
[日本語チュートリアル - fpdf2](https://py-pdf.github.io/fpdf2/Tutorial-ja.html)
