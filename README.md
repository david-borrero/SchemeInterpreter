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

## Jocs de proves

### Funcions basiques

#### Introducció

Aquest codi implementa dues funcions simples per operar amb nombres enters: una per sumar i una altra per multiplicar. També inclou instruccions per mostrar els resultats d'aquestes operacions.

#### Contingut del codi

##### Definicions de les funcions

1. **Funció `suma`**

   ```scheme
   (define (suma x y)
     (+ x y))
   ```

   Aquesta funció pren dos paràmetres (`x` i `y`) i retorna la seva suma utilitzant l'operador `+`.

2. **Funció `producte`**

   ```scheme
   (define (producte x y)
     (* x y))
   ```

   Aquesta funció pren dos paràmetres (`x` i `y`) i retorna el seu producte utilitzant l'operador `*`.

##### Mostra dels resultats

El codi utilitza les funcions `display` i `newline` per imprimir els resultats de les operacions i `read` per introduïr els valors:

```scheme
(display "Introdueix el primer número: ")
(define x (read))
(display "Introdueix el segon número: ")
(define y (read))

(display "La suma és: ")
(display (suma x y))
(newline)

(display "El producte és: ")
(display (producte x y))
(newline)
```

###### Resultat esperat:

- Primer es mostra la suma de `5` i `7` (que és `12`).
- Després es mostra el producte de `4` i `6` (que és `24`).
- Cada resultat apareix en una nova línia.

## Ús

```sh
python3 scheme.py <arxiu> < entrada > sortida
```

### Generar Arxius ANTLR

Per generar els arxius necessaris a partir de la gramàtica `scheme.g4`, executar:

```sh
make generate
```
