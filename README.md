# PDF to Word Converter

This Streamlit app allows you to easily convert PDF files to Microsoft Word documents.

**Key Features:**

* **User-friendly interface:** Streamlit provides a simple and intuitive web-based interface for uploading PDFs and downloading the converted Word files.
* **Fast and efficient:** The conversion process is designed to be quick and efficient.
* **Reliable:** The app leverages robust libraries to ensure accurate and reliable conversions.

## Installation

1. **Clone the repository:**

    ```bash
    git clone <repository_url>
    ```

2. **Install required packages:**

    ```bash
    pip install streamlit pypdf python-docx
    ```

## Usage

1. **Run the app:**

    ```bash
    streamlit run app.py 
    ```

2. **Upload a PDF file:**
   Use the file uploader in the Streamlit app to select the PDF file you want to convert.

3. **Convert and download:**
    Click the "Convert" button. Once the conversion is complete, you can download the resulting Word document.

## Dependencies

* streamlit: For building the web application.
* PyPDF2: For reading and manipulating PDF files.
* docx: For creating and manipulating Word documents.
  
## Contributing

Contributions are welcome! Please feel free to submit a pull request with any improvements or bug fixes.

**Note:**

This is a basic example, and you may need to customize it further based on your specific requirements. For more complex conversions or advanced features, you might consider using other libraries like pdfminer or pdfplumber.
