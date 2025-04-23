import pdfplumber
from docx import Document

def extract_text_from_pdf(file_path):
    """Extrait le texte depuis un fichier PDF."""
    with pdfplumber.open(file_path) as pdf:
        text = "\n".join(
            page.extract_text() for page in pdf.pages if page.extract_text()
        )
    return text.strip()

def extract_text_from_docx(file_path):
    """Extrait le texte depuis un fichier DOCX."""
    doc = Document(file_path)
    return "\n".join(paragraph.text for paragraph in doc.paragraphs).strip()

def extract_cv_text(file_path):
    """Détecte le format de fichier et retourne le texte brut du CV."""
    if file_path.endswith(".pdf"):
        return extract_text_from_pdf(file_path)
    elif file_path.endswith(".docx"):
        return extract_text_from_docx(file_path)
    else:
        raise ValueError("Format de fichier non supporté. Utilisez .pdf ou .docx")
