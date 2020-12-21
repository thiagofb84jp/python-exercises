# Parâmetros Opcionais

def tagBloco(texto, classe='sucess'):
    return f'<div class="{classe}">{texto}</div>'


if __name__ == "__main__":
    # Testes (assertions)
    assert tagBloco('Incluído com sucesso!') == \
        '<div class="sucess">Incluído com sucesso!</div>'
    assert tagBloco('Impossível excluir!', 'error') == \
        '<div class="error">Impossível excluir!</div>'
    print(tagBloco('bloco'))