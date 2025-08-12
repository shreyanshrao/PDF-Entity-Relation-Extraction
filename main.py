import openai
import csv
import fitz  # PyMuPDF

# 1. Set your API key
openai.api_key = ""  # <-- Replace with your key

# 2. Function to read PDF
def read_pdf(file_path):
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

# 3. Function to extract entities and relations using GPT
def extract_entities_and_relations(text):
    prompt = f"""
    You are an information extraction system.
    From the following text, extract:
    - Entities: Organisation, Name, PAN
    - Relations: PAN_Of

    Format output as CSV rows:
    Entity(PAN),Relation,Entity(Person/Organisation)

    Text:
    {text}
    """
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an expert in entity and relation extraction."},
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )
    return response["choices"][0]["message"]["content"]

# 4. Save to CSV
def save_to_csv(extracted_data, output_file):
    rows = [row.strip().split(",") for row in extracted_data.strip().split("\n")]
    with open(output_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Entity(PAN)", "Relation", "Entity(Person/Organisation)"])
        writer.writerows(rows)

# 5. Main script
if __name__ == "__main__":
    pdf_path = "pdf.pdf"  # Change to your PDF path
    output_csv = "extracted_results.csv"

    pdf_text = read_pdf(pdf_path)
    extracted_data = extract_entities_and_relations(pdf_text)
    save_to_csv(extracted_data, output_csv)

    print(f"Extraction complete. Results saved to {output_csv}")
