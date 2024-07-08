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
