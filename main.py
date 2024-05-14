import os
import easyocr
from pdf2image import convert_from_path

pdf_directory = '/home/alifoo/Workspace/py-ocr/mext/'

def create_pdf(pdf_directory):
    for root, dirs, files in os.walk(pdf_directory):
        for pdf_file in files:
            if pdf_file.endswith('.pdf'):
                # Create a folder for each PDF file
                pdf_name = os.path.splitext(pdf_file)[0]
                output_folder = os.path.join(root, pdf_name)
                os.makedirs(output_folder, exist_ok=True)

                # Convert PDF to images
                pages = convert_from_path(os.path.join(root, pdf_file))

                # Save images in the folder
                for i, page in enumerate(pages):
                    page.save(os.path.join(output_folder, f'page_{i}.jpg'), 'JPEG')

if __name__ == "__main__":
    reader = easyocr.Reader(["en"])
    result = reader.readtext("/home/alifoo/Workspace/py-ocr/example.jpg")

    for (bbox, text, prob) in result:
        print(text)