# 9.18. Uso de aspas triplas

with open("pagina.html", "w", encoding="utf-8") as pagina:
    pagina.write("""
        <!DOCTYPE html>
        <html lang="pt-BR">
        <head>
            <meta charset="utf-8">
            <title>Título da Página</title>
        </head>
        <body>
            Olá!
    """)
    for lines in range(100):
        pagina.write(f"<p>{lines}</p>")

    pagina.write("""
        </body>
        </html>
    """)
