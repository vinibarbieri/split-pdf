import sys
import os
from pypdf import PdfReader, PdfWriter

def extract_pages(pdf_path, start_page, end_page):
    pdf_path = pdf_path.strip().strip("'").strip('"')
    
    if not os.path.exists(pdf_path):
        print(f"Error: File not found: {pdf_path}")
        return

    dir_name = os.path.dirname(pdf_path)
    base_name = os.path.basename(pdf_path).replace(".pdf", "")
    output_filename = f"{base_name}_p{start_page}-{end_page}.pdf"
    output_path = os.path.join(dir_name, output_filename)

    try:
        reader = PdfReader(pdf_path)
        writer = PdfWriter()
        
        total_pages = len(reader.pages)
        if start_page < 1 or end_page > total_pages:
            print(f"Error: PDF has {total_pages} pages. Invalid range.")
            return

        print(f"Processing '{base_name}'...")
        
        # pypdf uses 0-based indexing, user input is 1-based
        for i in range(start_page - 1, end_page):
            writer.add_page(reader.pages[i])

        with open(output_path, "wb") as f:
            writer.write(f)

        print(f"Done! Saved to:\n{output_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) == 4:
        path = sys.argv[1]
        start = int(sys.argv[2])
        end = int(sys.argv[3])
        extract_pages(path, start, end)
    else:
        print("--- PDF Extractor ---")
        path = input("Drag the PDF file here: ")
        start = int(input("Start page: "))
        end = int(input("End page: "))
        extract_pages(path, start, end)