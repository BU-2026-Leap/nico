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
        <h2>{title}</h2>
        {img_tag}
        <div>{content}</div>
    """