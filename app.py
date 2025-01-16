import streamlit as st # for creating the web app
from docx import Document # for creating a Word document
from pypdf import PdfReader # for reading the PDF file
import io # for reading the file

# Configuring the app
st.set_page_config(page_title="PDF To Word Converter", page_icon="📄", layout="centered") # Configures the appearance of the app
st.title("📄 PDF To Word Converter")

# Pdf file uploader
st.header("Upload a PDF file")
uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])

if uploaded_file:

    # Extracting the text from the PDF file
    try:
        # Read the pdf file
        pdf_reader = PdfReader(uploaded_file)
        pdf_text = ""

        for page in pdf_reader.pages:
            pdf_text += page.extract_text()

        # Create a Word document
        word_doc = Document()
        word_doc.add_paragraph(pdf_text)

        # Save the Word document to an in-memory buffer
        word_buffer = io.BytesIO()
        word_doc.save(word_buffer)
        word_buffer.seek(0)

        st.success("✅ Word document created successfully!")

        # Download Option
        st.download_button(
            label="Download Word Document",
            data=word_buffer,
            file_name="converted_document.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )
    except Exception as e:
        st.error(f"❌ An Error occured: {e}")