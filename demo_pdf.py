from weasyprint import HTML
import os, pathlib


def main():
    root_file = pathlib.Path(__file__).parent.resolve()
    google_pdf_path = os.path.join(root_file, "statics", "google.pdf")
    local_pdf_path = os.path.join(root_file, "statics", "local.pdf")
    html_file_path = os.path.join(root_file, "statics", "html_code.html")
    test_pdf_path = os.path.join(root_file, "statics", "test.pdf")

    # Création de PDF à partir d'un URL
    HTML(url='https://google.fr/').write_pdf(google_pdf_path)
    # Création d'un PDf à partir d'un fichier HTML local
    HTML(filename=html_file_path).write_pdf(local_pdf_path)
    # Création d'un PDf à partir d'un string
    html_code = """
    <h1>Ceci est un titre H1</h1>
    <p>Ceci est le paragraphe.</p>
    """
    HTML(string=html_code).write_pdf(test_pdf_path)


    from weasyprint import HTML, CSS
    from weasyprint.text.fonts import FontConfiguration

    font_config = FontConfiguration()
    html = HTML(string='<h1>The title</h1>')
    css = CSS(string='''
        @font-face {
            font-family: Lato;
            src: url(https://fonts.googleapis.com/css2?family=Lato&display=swap);
        }
        h1 { font-family: Lato }''', font_config=font_config)
    html.write_pdf(
        '/tmp/example.pdf', stylesheets=[css],
        font_config=font_config)


if __name__ == '__main__':
    main()