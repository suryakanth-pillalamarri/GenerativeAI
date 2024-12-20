import pypdf

class Helper:
    # Step 1: Define function to extract text from PDF using pypdf
    def extract_text_from_pdf(self, pdf_path):
        speech = ""
        with open(pdf_path, "rb") as file:
            reader = pypdf.PdfReader(file)  # Using pypdf (PyPDF2) to read PDF
            for page in reader.pages:
                speech += page.extract_text()  # Extract text from each page
        return speech

    # Helper function to calculate average length of sentences/paragraphs in a text
    def calculate_avg_chunk_size(self, text):
        sentences = text.split("\n")  # Assuming paragraphs are separated by newline
        if len(sentences) == 0:
            return 0
        avg_len = sum(len(sentence) for sentence in sentences) / len(sentences)
        return avg_len
