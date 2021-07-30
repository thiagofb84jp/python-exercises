# Parâmetros Nomeados

def tagBloco(texto, classe='sucess', inline=False):
    tag = 'span' if inline else 'div'
    return f'<{tag} class="{classe}">{texto}</{tag}>'


if __name__ == "__main__":
    print(tagBloco('bloco'))
    print(tagBloco('inline e classe', 'info', True))
