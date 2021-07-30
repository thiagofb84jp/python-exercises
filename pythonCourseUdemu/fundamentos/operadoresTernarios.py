# Operadores Ternários
"""
(False, True)[validação da expressão]
"""

estahChovendo = True
print('Hoje estou com as roupas ' + ('secas.', 'molhadas.')[estahChovendo])
print('Hoje estou com as roupas '
      + ('molhadas.' if estahChovendo else 'secas.'))
