def handled_uploaded_file(f):
    with open('static/images/productos/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)