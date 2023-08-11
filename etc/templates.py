from utils import html


html_template = lambda data: html.strip(f"""
    <html>
        <head>
            <title>{data['title']}</title>
        </head>
        <body>
            <p>{data['description']}</p>
        </body>
    </html>
""")