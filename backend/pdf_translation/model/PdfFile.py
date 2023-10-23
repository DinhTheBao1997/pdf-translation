from django.core.files.base import File
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
    

class PdfFile:
    __file: File
    __fileName: str

    def __init__(self, file: File, fileName: str) -> None:
        self.__file = file
        self.__fileName = fileName

    def scan_pdf(self):
        # PdfFile.__scan_pdf_PDFQuery(self)
        # PdfFile.__scan_pdf_pypdf(self)
        PdfFile.__scan_pdf_fpdf(self)
        pass

    def __scan_pdf_pypdf(self):
        lst = []
        pdf_write = PdfWriter()
        pdfReader = CustomPdfReader(self.__file)
        pagecount = len(pdfReader.pages)
        for p in range(pagecount):
            pageObj = pdfReader.pages[p]
            text = pageObj.extract_text()
            pdf_write.add_page(pageObj)
            # lst.append(pageObj.extract_text())
        # write_file("./%s.txt" % self.__fileName, "\n".join(lst))
        with open('test.pdf', 'wb') as fh:
            pdf_write.write(fh)

    def __scan_pdf_fpdf(self):
        pdf = CustomFPDF()
        # compression is not yet supported in py3k version
        pdf.compress = False
        pdfReader = CustomPdfReader(self.__file)
        pagecount = len(pdfReader.pages)
        # for p in range(pagecount):
        #     pageObj = pdfReader.pages[p]
        #     text = pageObj.extract_text()
        #     pdf.add_page()
        #     pdf.set_font('Arial', '', 11)  
        #     pdf.ln(10)
        #     pdf.write(5, "text")
        # with open('py3k.pdf', 'wb') as f:
        #     f.write(pdf.buffer)

        pdf.add_font('times', '', 'times.ttf', uni=True) 
        for p in range(pagecount):
            pageObj = pdfReader.pages[p]
            text = pageObj.extract_text()
            pdf.add_page()
            pdf.set_font('times', '', 11)  
            pdf.ln(10)
            pdf.write(5, text)
            print(pdf.text(5, 10))
        pdf.output('py3k.pdf', 'F')
        pass

    def write_new_file():
        pass

    def __scan_pdf_PDFQuery(self):
        pdf = PDFQuery(self.__file)
        # pdf.load()
        lst = []

        pagecount = pdf.doc.catalog['Pages'].resolve()['Count']
        # master = pd.DataFrame()
        for p in range(pagecount):
            pdf.load(p)
            page = PdfFile.__pdfscrape(pdf, lst) 
        print(tempfile.gettempdir())
        write_file("./%s.txt" % self.__fileName, "\n".join(lst))

    def __pdfscrape(pdf: PDFQuery, lst: list[str]):
        # Extract each relevant information individually
        pq = pdf.pq('LTTextLineHorizontal')
        text = pq.text(squash_space=False)
        text = text.replace("  ", "\n")
        lst.append(text)
