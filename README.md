PDF Entity & Relation Extraction
This project extracts entities and relations from PDF documents using a Large Language Model (LLM).
It focuses on:

Entities: Organisation, Name, PAN

Relations: PAN_Of (e.g., AAUFM6247N PAN_Of Mr. Agarwal)

The extracted results are saved into a CSV file.

1️⃣ Models Used
Primary: Mistral 7B
We use the open-source Mistral-7B-v0.1 model for entity & relation extraction.

⚠ Important:
mistralai/Mistral-7B-v0.1 is a gated Hugging Face model.
To use it:

Sign in to Hugging Face

Visit the Mistral-7B model page

Click "Request Access"

Wait for approval


# Clone repository
git clone https://github.com/your-repo/pdf-entity-extraction.git
cd pdf-entity-extraction

# Create a virtual environment
python -m venv venv
source venv/bin/activate   # (Linux/Mac)
venv\Scripts\activate      # (Windows)

# Install dependencies
pip install -r requirements.txt
requirements.txt

nginx
Copy
Edit
transformers
torch
PyMuPDF
huggingface_hub
openai
3️⃣ Running the Script
bash
Copy
Edit
python main.py --pdf input.pdf --output results.csv
Arguments:

--pdf → Path to input PDF

--output → Path to output CSV file

4️⃣ Example Output
Entity(PAN)	Relation	Entity(Person/Organisation)
AAUFM6247N	PAN_Of	Mr. Agarwal
BBBBB1234X	PAN_Of	XYZ Pvt Ltd
