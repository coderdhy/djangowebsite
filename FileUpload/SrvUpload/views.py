from django.http import HttpResponse
# from django.shortcuts import render_to_response
import os

FileDir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'FileDir')


def upload(request):
    if request.method == 'POST':
        for field_name in request.FILES:
            uploaded_file = request.FILES[field_name]
            # int size = uploaded_file['chunk']
            # int total = uploaded_file['chunks']
            destination_path = os.path.join(FileDir, uploaded_file.name)
            destination = open(destination_path, 'wb+')
            for chunk in uploaded_file.chunks():
                destination.write(chunk)
            destination.close()
        return HttpResponse("ok", mimetype="text/plain")
    else:
        # show the upload UI
        return HttpResponse('uploads/manual.html')