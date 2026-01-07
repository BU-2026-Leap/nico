def html_response(body, status=200):
    return {
        "statusCode": status,
        "headers": {
            "Content-Type": "text/html"
        },
        "body": f"""
        <!DOCTYPE html>
        <html>
        <head>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB" crossorigin="anonymous">
            <link href="aws/styles.css" rel="stylesheet">
            <style>
                body {{ font-family: Arial; max-width: 600px; margin: 50px auto; }}
                img {{ max-width: 100%; height: auto; }}
            </style>
        </head>
        <body>
            {body}
        </body>
        </html>
        """
    }



def page_template(title, content, image_url=None):
    """Reusable page template"""
    img_tag = f'<img src="{image_url}" alt="{title}">' if image_url else ''
    return f"""
        <div class="row justify-content-center">
            <div class="col-auto">
                <h2>{title}</h2>
            </div>
        </div>
        <div class="container">
            <div class="row justify-content-center">
                <div class="frame mb-3 mt-3">
                    <div class="img-container col-auto border border-white">
                      {img_tag}
                    </div>
                </div>
            </div>
        </div>
        <div class="flavortext">{content}</div>
    """

