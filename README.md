# Intèrpret de Scheme

Aquest projecte és un intèrpret per a un subconjunt del llenguatge Scheme, implementat en Python utilitzant ANTLR per a l'anàlisi lèxica i sintàctica.

## Característiques

- **Anàlisi lèxic i sintàctic**: Utilitza ANTLR per generar el lexer i el parser a partir de la gramàtica `scheme.g4`.
- **Avaluació d'expressions**: Implementa un visitant (`EvalVisitor`) que avalua les expressions del llenguatge Scheme.
- **Suport per a operacions bàsiques**: Suporta operacions aritmètiques, lògiques i de comparació.
- **Gestió de funcions i variables**: Permet la definició i crida de funcions i variables.
- **Control de flux**: Implementa estructures de control com `if` i `cond`.

## Estructura del Projecte

- `scheme.g4`: Arxiu de gramàtica ANTLR que defineix la sintaxi del llenguatge Scheme.
- `eval_visitor.py`: Implementació del visitant que avalua les expressions del llenguatge Scheme.
- `scheme.py`: Script principal que utilitza ANTLR per analitzar l'arxiu d'entrada i avalua les expressions utilitzant `EvalVisitor`.
- `Makefile`: Arxiu de make que automatitza la generació d'arxius ANTLR i la neteja d'arxius generats.

## Requisits

- Python 3
- ANTLR 4

## Instal·lació

1. Instal·lar ANTLR 4 seguint les instruccions a [ANTLR](https://www.antlr.org/).
2. Clonar aquest repositori.

## Ús

### Generar Arxius ANTLR

Per generar els arxius necessaris a partir de la gramàtica `scheme.g4`, executar:

```sh
make generate
```
