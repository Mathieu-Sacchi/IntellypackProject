from io import BytesIO

import PyPDF2
from django.http import HttpResponse, FileResponse

from PyPDF2.generic import BooleanObject, NameObject, IndirectObject, NumberObject


def pdf(request, template):
    #template = r'C:\Users\Mathi\Documents\Coding\PDF_Templates\Test_Contract.pdf'  # location of the pdf template

    outfile = r'C:\Users\Mathi\Documents\Coding\PDF_Templates\templates/test.pdf'  # location of the filled in pdf

    input_stream = open(template, "rb")  # opens the template for reading in binary mode and returns it as a file object

    # PyPDF2 class that takes a file object or path to file (test), strict determines whether user should be warned of
    # all problems and also causes some correctable problems to be fatal. Initialises the PdfFileReader object.
    pdf_reader = PyPDF2.PdfFileReader(input_stream, strict=False)

    # Trailer is where all the file's metadata is stored, in a pdf the AcroForm contains the annotation fields
    # NeedAppearances needs to be true to enable the modification and setting of field value
    if "/AcroForm" in pdf_reader.trailer["/Root"]:
        pdf_reader.trailer["/Root"]["/AcroForm"].update(
            {NameObject("/NeedAppearances"): BooleanObject(True)})

    # We create a blank pdf page that will be writen
    pdf_writer = PyPDF2.PdfFileWriter()
    set_need_appearances_writer(pdf_writer)
    if "/AcroForm" in pdf_writer._root_object:
        # Acro form is form field, set needs appearances to fix printing issues
        pdf_writer._root_object["/AcroForm"].update(
            {NameObject("/NeedAppearances"): BooleanObject(True)})

    data_dict = {
        'numero_de_contrat#0': '12345\n',
        'numero_de_contrat#1': '12345\n',
        'Raison_Sociale': 'Dunder Mifflen\n',
        'Adresse': '1 paper drive, Paris\n',
        'SIREN': '1 paper drive, Paris\n',
        'Tel': '06.95.97.02.30\n',
    }

    # Create new page in this pdf we are writingr
    pdf_writer.addPage(pdf_reader.getPage(0))
    page = pdf_writer.getPage(0)
    pdf_writer.updatePageFormFieldValues(page, data_dict)
    for j in range(0, len(page['/Annots'])):
        writer_annot = page['/Annots'][j].getObject()
        for field in data_dict:
            # -----------------------------------------------------BOOYAH!
            if writer_annot.get('/T') == field:
                writer_annot.update({
                    NameObject("/Ff"): NumberObject(1)
                })
            # -----------------------------------------------------
    output_stream = BytesIO()
    pdf_writer.write(output_stream)



    response = HttpResponse(output_stream.getvalue(), content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="completed.pdf"'
    input_stream.close()

    return FileResponse(output_stream, as_attachment=True, filename='test.pdf')


def set_need_appearances_writer(writer):
    try:
        catalog = writer._root_object
        # get the AcroForm tree and add "/NeedAppearances attribute
        if "/AcroForm" not in catalog:
            writer._root_object.update({
                NameObject("/AcroForm"): IndirectObject(len(writer._objects), 0, writer)})

        need_appearances = NameObject("/NeedAppearances")
        writer._root_object["/AcroForm"][need_appearances] = BooleanObject(True)


    except Exception as e:
        print('set_need_appearances_writer() catch : ', repr(e))

    return writer


print(pdf(request=True, template=r'C:\Users\Mathi\Documents\Coding\PDF_Templates\Test_Contract.pdf'))