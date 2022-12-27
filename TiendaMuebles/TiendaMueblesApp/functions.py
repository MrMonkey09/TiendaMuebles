from xhtml2pdf import pisa
from django.template.loader import get_template
from io import BytesIO
from django.http import HttpResponse

def handled_uploaded_file(f):
    with open('static/images/productos/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def template2pdf(template_origen, contexto={}):
    template = get_template(template_origen)
    html = template.render(contexto)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(),content_type='application/pdf')
    return None