from django.core.files.base import File
from pyquery import PyQuery
from pdfquery import PDFQuery
from ..common.common import write_file
import tempfile
from ..CustomPyPDF.CustomPdfReader import PdfFileWriter, CustomPdfReader
from ..CustomPyPDF.CustomPageObject import CustomPageObject
from pypdf._page import PageObject
from pypdf import PdfReader, PdfWriter, generic, _utils
from fpdf import FPDF
import sys
from ..CustomPyPDF.CustomFPDF import CustomFPDF
import sys
import json
from ..nlp.service.vinai_transalte import VinaiTranslate

SIZE = {
    "A4": {
        "x": 210,
        "y": 297,
    }
}

def children(pdfQuery: PyQuery, pdf: CustomFPDF):
    if pdfQuery is None:
        return
    lst = pdfQuery.getchildren()
    if lst is None or len(lst) == 0:
        if "text" not in pdfQuery.tag.lower():
            return
        text = pdfQuery.text
        if text is None or len(text) == 0:
            return
        x0 = float(pdfQuery.attrib["x0"])
        y0 = float(pdfQuery.attrib["y0"])
        y1 = float(pdfQuery.attrib["y1"])
        pdf.set_font_size(abs(y0 - y1))
        x = x0
        y = 792 - y0
        # text = VinaiTranslate.translate_en2vi(text)
        pdf.text(x, y, text)
    for child in pdfQuery.getchildren():
        children(child, pdf)

class PdfFile:
    __file: File
    __fileName: str

    def __init__(self, file: File, fileName: str) -> None:
        self.__file = file
        self.__fileName = fileName

    def scan_pdf(self):
        PdfFile.__scan_pdf_fpdf(self)
        # PdfFile.__scan_pdf_PDFQuery(self)
        pass

    def __scan_pdf_fpdf(self):
        pdf = CustomFPDF()
        pdf.config()

        # compression is not yet supported in py3k version
        pdfReader = CustomPdfReader(self.__file)
        pagecount = len(pdfReader.pages)

        for p in range(10):
            pageObj = pdfReader.pages[p]
            text = pageObj.extract_text()
            PdfFile.__addPage(pdf)
            print("Page %s" % p)
            text = VinaiTranslate.translate_en2vi(text)
            PdfFile.__addTextToPdf(pdf, text)
        pdf.output('test-2.pdf', 'F')
        pass

    def __scan_pdf_PDFQuery(self):
        pdfQuery = PDFQuery(self.__file)
        # pdf.load()
        # lst = []
        pdf = CustomFPDF('P', 'pt', 'A4')
        pdf.config()

        pagecount = pdfQuery.doc.catalog['Pages'].resolve()['Count']
        # master = pd.DataFrame()
        for p in range(10):
            pdfQuery.load(p)
            PdfFile.__addPage(pdf)
            print("Page %s" % p)
            text = PdfFile.__pdfscrape(pdfQuery, pdf) 
        pdf.output('__scan_pdf_PDFQuery.pdf', 'F')

    def __pdfscrape(pdfQuery: PDFQuery, pdf: CustomFPDF):
        pq = pdfQuery.pq('LTPage')
        for child in pq.children():
            children(child, pdf)
    def __addPage(pdf: CustomFPDF):
        pdf.add_page()
        pdf.set_font('times', '', 11)  
        pdf.ln(10)
    
    def __addTextToPdf(pdf: CustomFPDF, text: str):
        pdf.write(5, text)
