import argparse
import os
from pypdf import PdfReader, PdfWriter

def extract_pages(pdf_path, start_page, end_page):
    pdf_path = pdf_path.strip().strip("'").strip('"')
    
    if not os.path.exists(pdf_path):
        print(f"Error: File not found: {pdf_path}")
        return

    if not pdf_path.lower().endswith(".pdf"):
        print("Error: File is not a PDF.")
        return

    if start_page > end_page:
        print(f"Error: Start page ({start_page}) is greater than end page ({end_page}).")
        return

    base_name, _ = os.path.splitext(os.path.basename(pdf_path))
    dir_name = os.path.dirname(pdf_path)
    output_filename = f"{base_name}_p{start_page}-{end_page}.pdf"
    output_path = os.path.join(dir_name, output_filename)

    if os.path.exists(output_path):
        answer = input(f"'{output_filename}' already exists. Overwrite? [y/N]: ").strip().lower()
        if answer != "y":
            print("Aborted.")
            return

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

def read_int(prompt):
    while True:
        value = input(prompt)
        try:
            return int(value)
        except ValueError:
            print(f"Error: '{value}' is not a valid number. Try again.")

def build_parser():
    parser = argparse.ArgumentParser(
        description="Extract a range of pages from a PDF file."
    )
    parser.add_argument("file", nargs="?", help="path to the PDF file")
    parser.add_argument("start", nargs="?", type=int, help="start page (1-based)")
    parser.add_argument("end", nargs="?", type=int, help="end page (1-based)")
    return parser

if __name__ == "__main__":
    parser = build_parser()
    args = parser.parse_args()

    if args.file and args.start is not None and args.end is not None:
        extract_pages(args.file, args.start, args.end)
    else:
        print("--- PDF Extractor ---")
        path = args.file or input("Drag the PDF file here: ")
        start = args.start if args.start is not None else read_int("Start page: ")
        end = args.end if args.end is not None else read_int("End page: ")
        extract_pages(path, start, end)