from io import BytesIO
import PyPDF2
from PyPDF2.generic import BooleanObject, NameObject, IndirectObject, NumberObject

# open the pdf
input_stream = open("YourPDF.pdf", "rb")
pdf_reader = PyPDF2.PdfFileReader(input_stream, strict=False)
if "/AcroForm" in pdf_reader.trailer["/Root"]:
    pdf_reader.trailer["/Root"]["/AcroForm"].update(
        {NameObject("/NeedAppearances"): BooleanObject(True)})

pdf_writer = PyPDF2.PdfFileWriter()
set_need_appearances_writer(pdf_writer)
if "/AcroForm" in pdf_writer._root_object:
    # Acro form is form field, set needs appearances to fix printing issues
    pdf_writer._root_object["/AcroForm"].update(
        {NameObject("/NeedAppearances"): BooleanObject(True)})

data_dict = dict() # this is a dict of your DB form values

pdf_writer.addPage(pdf_reader.getPage(0))
page = pdf_writer.getPage(0)
# update form fields
pdf_writer.updatePageFormFieldValues(page, data_dict)
for j in range(0, len(page['/Annots'])):
    writer_annot = page['/Annots'][j].getObject()
    for field in data_dict:
        if writer_annot.get('/T') == field:
            writer_annot.update({
                NameObject("/Ff"): NumberObject(1)    # make ReadOnly
            })
output_stream = BytesIO()
pdf_writer.write(output_stream)

# output_stream is your flattened PDF


def set_need_appearances_writer(writer):
    # basically used to ensured there are not 
    # overlapping form fields, which makes printing hard
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