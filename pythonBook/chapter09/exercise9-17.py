# 9.7. Criação de uma página inicial em Python

with open("pagina.html", "w", encoding="utf-8") as pagina:
    pagina.write("<!DOCTYPE html>\n")
    pagina.write("<html>\n")
    pagina.write("<head>\n")
    pagina.write("<meta charset=\"utf-8\">\n")
    pagina.write("<title>Título da Página</title>\n")
    pagina.write("</head>\n")
    pagina.write("<body>\n")
    pagina.write("Olá!")

    for line in range(100):
        pagina.write(f"<p>{line}</p>\n")

    pagina.write("<p>Fim do programa.</p>\n")
    pagina.write("</body>\n")
    pagina.write("</html>\n")
