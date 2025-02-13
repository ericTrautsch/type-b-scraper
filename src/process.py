import pdfplumber
import pandas as pd
import os


def extract_tables_from_pdfs(pdf_folder, output_csv):
    all_tables = []
    seen_headers = set()
    count = 0
    # Loop through all pdfs in the folder
    for pdf_file in os.listdir(pdf_folder):
        count = count + 1
        if pdf_file.endswith(".pdf"):
            pdf_path = os.path.join(pdf_folder, pdf_file)
            print(f"Processing: {pdf_path}")

            with pdfplumber.open(pdf_path) as pdf:
                for page_num, page in enumerate(pdf.pages, start=1):
                    tables = page.extract_tables()
                    for table in tables:
                        df = pd.DataFrame(table)
                        # Drop completely emptry rows
                        df.dropna(how="all", inplace=True)
                        # Capture PDF Name and Page Number for reference
                        df["PDF_Name"] = pdf_file
                        df["Page_Number"] = page_num

                        if not df.empty:
                            header_tuple = tuple(df.iloc[0])

                            if header_tuple not in seen_headers:
                                seen_headers.add(header_tuple)
                            else:
                                df = df[1:]
                        all_tables.append(df)
    if all_tables:
        # Concatenate all tables and serve as csv
        final_df = pd.concat(all_tables, ignore_index=True)
        final_df.to_csv(output_csv, index=False)
        print(count)
        print(f"CSV Saved {output_csv}")
    else:
        print("No tables found in pdf")


if __name__ == "__main__":
    pdf_folder = "./data/"
    output_csv = "output.csv"

    extract_tables_from_pdfs(pdf_folder, output_csv)
