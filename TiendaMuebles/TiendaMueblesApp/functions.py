def handled_uploaded_file(f):
    with open('static/docs'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)