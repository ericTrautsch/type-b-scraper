import pdfplumber
import pandas as pd
import os


def process_pdfs(pdf_dir: str) -> pd.DataFrame:
    """
    Iterates over downloaded `.pdf` files in given directory, extracting tables and concatenating results.

    @param pdf_dir: directory to look in for pdfs to process
    """
    all_tables = []
    failed_tables = []
    seen_headers = set()
    # Loop through all pdfs in the folder in sorted order
    for pdf_file in sorted(os.listdir(pdf_dir)):
        if pdf_file.endswith(".pdf"):
            pdf_path = os.path.join(pdf_dir, pdf_file)
            try:
                all_tables.append(extract_table_from_pdf(pdf_path, pdf_file))
                print(f"Processed: {pdf_path}")
            except:
                print(f"Failed to extract {pdf_path}")
                failed_tables.append(pdf_path)
    # Concatenate all tables and serve as csv
    print(f"Failed to extract {len(failed_tables)} files. {failed_tables}")
    final_df = pd.concat(all_tables, ignore_index=True)
    return final_df


def extract_table_from_pdf(pdf_path: str, pdf_file: str) -> pd.DataFrame:
    """
    Extracts tables from pdfs into dataframes, including capturing page number and pdf name

    @param pdf_path: direct file path for the pdf to extract from

    # TODO: Remove pdf file, read from pdf_path instead..
    @param pdf_file: File name of the pdf, to trace back to
    """
    all_tables = []
    with pdfplumber.open(pdf_path) as pdf:
        for page_num, page in enumerate(pdf.pages, start=1):
            tables = page.extract_tables()
            for table in tables:
                df = pd.DataFrame(table)
                df.dropna(how="all", inplace=True)
                df.columns = df.iloc[0]
                df = df[1:]
                df.reset_index()
                # Capture PDF Name and Page Number for reference
                if not df.empty:
                    df["PDF_Name"] = pdf_file
                    df["Page_Number"] = page_num
                    all_tables.append(df)
    return pd.concat(all_tables, ignore_index=True)


def save(df: pd.DataFrame, output_path: str = "output.csv"):
    """
    Saves processed dataframe.

    @param df: dataframe to write from
    @param output_csv: filepath to write to (

    TODO: Update this to save the processed dataframe in another place (database, dynamo, etc)
    """
    print(f"Output saved to {output_path}")
    df.to_csv(output_path, index=False)


def process(pdf_folder: str = "./data/"):
    """
    Processes a folder of pdfs into a single dataframe and saves output
    """
    df = process_pdfs(pdf_folder)
    save(df)


if __name__ == "__main__":
    process()
