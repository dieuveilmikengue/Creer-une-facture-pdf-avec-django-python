from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
from django.conf import settings
import os

def index(request):
    context = {
        "title": "Django example",
    }
    return render(request, "index.html", context)


def generate_pdf(request):
    # Données à passer au template
    data = {
        'title': 'Mon Document PDF',
        'content': 'Ceci est un exemple de contenu pour le PDF.'
    }

    # # Rendre le template HTML
    html_string = render_to_string('generate_pdf.html', data)

    # # Créer un objet PDF
    html = HTML(string=html_string)
    pdf_file = html.write_pdf()


    # # Chemin absolu vers le fichier CSS en local
    # # css_path = settings.BASE_DIR, 'static', 'main.css'

    # # Créer un objet PDF avec le CSS en local
    # html = HTML(string=html_string)
    # pdf_file = html.write_pdf(stylesheets=[CSS(css_path)])

    # # Créer la réponse HTTP avec le PDF attaché
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="document.pdf"'

    return response