# 9.21. Geração de uma página web a partir de um dicionário
# Modificando o programa para exibir os elementos <ul> e <li>

filmes = {
    "drama": ["Cidadão Kane", "O Poderoso Chefão"],
    "comedia": ["Tempos Modernos", "American Pie", "Dr. Dolittle"],
    "policial": ["Chuva Negra", "Desejo de Matar", "Difícil de Matar"],
    "guerra": ["Rambo", "Platoon", "Tora! Tora! Tora!"]
}

with open("filmes.html", "w", encoding="utf-8") as pagina:
    pagina.write("""
        <!DOCTYPE html>
        <html lang="pt-BR">
        <head>
            <meta charset="utf-8">
            <title>Filmes</title>
        </head>
        <body>
    """)

    for c, v in filmes.items():
        pagina.write(f"<h1>{c.capitalize()}</h1>\n")
        pagina.write("<ul>")
        for e in v:
            pagina.write(f"<li>{e}</li>\n")
        pagina.write("</ul>")
        pagina.write("""
        </body>
        </html>
    """)
