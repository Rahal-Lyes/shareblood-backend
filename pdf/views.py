# backend/pdf_tools/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from pdf2image import convert_from_path
import tempfile
import os
from django.http import FileResponse

class PDFToJPGView(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request, *args, **kwargs):
        pdf_file = request.FILES.get('file')
        if not pdf_file:
            return Response({'error': 'No file provided'}, status=400)

        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_pdf:
            for chunk in pdf_file.chunks():
                temp_pdf.write(chunk)
            temp_pdf.flush()

            images = convert_from_path(temp_pdf.name)
            image_path = tempfile.mktemp(suffix=".jpg")
            images[0].save(image_path, 'JPEG')

            response = FileResponse(open(image_path, 'rb'), content_type='image/jpeg')
            response['Content-Disposition'] = 'attachment; filename="converted.jpg"'

            # Optionnel : Nettoyage
            os.unlink(temp_pdf.name)
            # tu peux aussi supprimer image_path après réponse si tu veux

            return response
