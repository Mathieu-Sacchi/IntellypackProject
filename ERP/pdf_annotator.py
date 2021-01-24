import PyPDF2
from PyPDF2.generic import BooleanObject, NameObject, IndirectObject, NumberObject
from django.http import HttpResponse, FileResponse
from io import  BytesIO


def write_pdf(template_path, data_dict):
    input_stream = open(template_path, "rb")  # opens the template for reading in bin mode and returns it as a file object
    pdf_reader = PyPDF2.PdfFileReader(input_stream, strict=False)

    # NeedAppearances needs to be true to allow thte
    if "/AcroForm" in pdf_reader.trailer["/Root"]:
        pdf_reader.trailer["/Root"]["/AcroForm"].update(
            {NameObject("/NeedAppearances"): BooleanObject(True)})

    pdf_writer = PyPDF2.PdfFileWriter()
    if "/AcroForm" in pdf_writer._root_object:
        pdf_writer._root_object["/AcroForm"].update(
            {NameObject("/NeedAppearances"): BooleanObject(True)})

    number_of_pages = pdf_reader.getNumPages()
    # print(number_of_pages)

    for page_number in range(number_of_pages):

        pdf_writer.addPage(pdf_reader.getPage(page_number))
        page = pdf_writer.getPage(page_number)

        # Method will update the form field values for a given page from a fields dictionary.
        # Copy field texts and values from fields to page.
        # fields (here) – a Python dictionary of field names (/T) and text values (/V)
        # pdf_writer.updatePageFormFieldValues(page, data_dict)

    output_stream = BytesIO()
    pdf_writer.write(output_stream)

    response = HttpResponse(output_stream.getvalue(), content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="completed.pdf"'
    input_stream.close()

    return FileResponse(output_stream, as_attachment=True, filename='test.pdf')

    #open(r'C:\Users\Mathi\Documents\Coding\PDF_Templates\templates\test.pdf', 'w').write(output_stream)

    #return FileResponse(output_stream, as_attachment=True, filename='hello.pdf')


template = r'C:\Users\Mathi\Documents\Coding\PDF_Templates\Test_Contract.pdf'
data = {
    '/Tnumero_de_contrat#0': '/V12345\n',
    '/Tnumero_de_contrat#1': '/V12345\n',
    '/TRaison_Sociale': '/VDunder Mifflen\n',
    '/TAdresse': '/V1 paper drive, Paris\n',
    '/TSIREN': '/V123456789\n',
    '/TTel': '/V06.95.97.02.30\n',
    }
write_pdf(template, data)

