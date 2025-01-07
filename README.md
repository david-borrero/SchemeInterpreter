# Intèrpret de Scheme

Aquest projecte és un intèrpret per a un subconjunt del llenguatge Scheme, implementat en Python utilitzant ANTLR per a l'anàlisi lèxica i sintàctica. Es tracta d'una implementació minimalista que simplifica el llenguatge a crides a funció i tipus bàsics, delegant la lògica de cada operació al visitador, que actua com a motor d'execució. La seva modularitat permet una extensió senzilla de les funcionalitats.

---

## Decisions de Disseny

### 1. Modularitat i Extensibilitat

- **Estructura del codi**: La classe `EvalVisitor` hereta de `schemeVisitor`, permetent una implementació modular on cada mètode gestiona un tipus específic de node del parse tree.
- **Operadors inicialitzats dinàmicament**: Les operacions aritmètiques i lògiques es defineixen en un diccionari (`initialize_operators`), facilitant l'extensió amb nous operadors sense alterar la lògica principal.

### 2. Gestió de Contextos i Variables

- **Pila de contextos (`call_stack`)**: Proporciona aïllament entre diferents àmbits de variables, útil per gestionar funcions i blocs com `let`.
- **Variables globals i locals**: Es diferencien les variables globals (`global_variables`) de les locals (`variables`), assegurant una clara separació entre escops.

### 3. Suport a Característiques del Llenguatge Scheme

- **Gestió de funcions definides per l’usuari**:
  - Es poden definir funcions mitjançant `define`.
  - Els paràmetres i el cos de les funcions es guarden en un diccionari (`funcions`).
- **Operacions amb llistes**: Implementació explícita de `car`, `cdr`, `cons` i `null?`, reflectint la importància de les llistes en Scheme.
- **Operadors lògics i condicionals**: Suport complet per a construccions com `if`, `cond` i operadors com `and`, `or`, `not`.

### 4. Interacció amb l’Usuari

- **Lectura de dades (`read`)**:
  - Les dades es llegeixen línia per línia des de l’entrada estàndard.
  - Es processen segons el format esperat (valors booleans, enters, llistes, etc.).
- **Sortida (`display`, `newline`)**:
  - Suport per mostrar valors i gestionar sortides personalitzades.

### 5. Robustesa

- **Gestió d’errors**:
  - Excepcions clares per a noms desconeguts, variables no definides o discrepàncies en el nombre d’arguments de les funcions.
- **Validació d’arguments**:
  - Els operadors i funcions validen el nombre i tipus d’arguments per evitar errors en temps d’execució.

### 6. Optimització del Flux d’Execució

- **Ús de `reduce`**:
  - Per avaluar operacions que impliquen múltiples valors (sumes, comparacions encadenades, etc.), reduint la complexitat del codi.
- **Preparació de dades d’entrada**:
  - Es detecten operacions `read` al principi per preparar les dades abans de visitar els nodes del parse tree.

---

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
(define x (read))
(define y (read))

(define (main)
    (let ((res1 (suma x y))
          (res2 (producte x y)))
        (display res1)
        (newline)
        (display res2)
        (newline)))
```

###### Resultat esperat:

- Primer es mostra la suma de `5` i `7` (que és `12`).
- Després es mostra el producte de `5` i `7` (que és `35`).
- Cada resultat apareix en una nova línia.

### Funcions d'Alt Ordre

#### Introducció

Aquest codi implementa funcions d'ordre superior per treballar amb llistes, incloent les clàssiques operacions `map` i `filter`, a més de definir funcions per operar amb nombres i una funció `main` per mostrar un exemple.

#### Contingut del codi

##### Definicions de les funcions

1. **Funció `filter`**

   ```scheme
   (define (filter predicat llista)
     (cond
       ((null? llista) '())
       ((predicat (car llista))
        (cons (car llista) (filter predicat (cdr llista))))
       (#t (filter predicat (cdr llista)))))
   ```

   Aquesta funció pren un predicat i una llista, i retorna una nova llista amb els elements que compleixen el predicat.

2. **Funció `map`**

   ```scheme
   (define (map func llista)
     (cond
       ((null? llista) '())
       (else (cons (func (car llista)) (map func (cdr llista))))))
   ```

   Aquesta funció aplica una funció a cada element d'una llista i retorna una nova llista amb els resultats.

3. **Funció `parell?`**

   ```scheme
   (define (parell? x) (= (mod x 2) 0))
   ```

   Aquesta funció determina si un nombre és parell.

4. **Funció `triplica`**

   ```scheme
   (define (triplica x) (* x 3))
   ```

   Multiplica un nombre per 3.

5. **Funció `main`**

   ```scheme
   (define (main)
       (display (map triplica (filter parell? '(1 2 3 4 5 6 7 8 9 10))))
       (newline))
   ```

   Aquesta funció mostra els resultats de filtrar els nombres parells d'una llista i triplicar-los.

##### Mostra dels resultats

Quan s'executa la funció `main`, el resultat esperat és:

```
(6 12 18 24 30)
```

Aquest resultat correspon als nombres parells de la llista inicial `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`, després de ser triplicats i filtrats.

### Funcions Recursives

#### Introducció

Aquest codi implementa dues funcions recursives per a càlculs matemàtics: una per calcular el factorial d'un nombre i una altra per trobar el màxim comú divisor (MCD) entre dos nombres. També inclou una funció `main` per mostrar exemples d'execució interactivament.

#### Contingut del codi

##### Definicions de les funcions

1. **Funció `factorial`**

   ```scheme
   (define (factorial n)
     (if (= n 0)
         1
         (* n (factorial (- n 1)))))
   ```

   Aquesta funció calcula el factorial d'un nombre enter `n`. Si `n` és 0, retorna 1. En cas contrari, retorna `n` multiplicat pel factorial de `n - 1`.

2. **Funció `mcd`**

   ```scheme
   (define (mcd a b)
     (if (= b 0)
         a
         (mcd b (mod a b))))
   ```

   Aquesta funció calcula el màxim comú divisor de dos nombres enters `a` i `b` utilitzant l'algorisme d'Euclides.

3. **Funció `main`**

   ```scheme
   (define (main)
     (let ((a (read))
           (b (read)))
       (display "El maxim comu divisor es: ")
       (display (mcd a b))
       (newline))
     (let ((n (read)))
       (display "El factorial es: ")
       (display (factorial n))
       (newline)))
   ```

   Aquesta funció interactua amb l'usuari per:

   - Llegir dos nombres i calcular-ne el MCD utilitzant la funció `mcd`.
   - Llegir un tercer nombre i calcular-ne el factorial amb la funció `factorial`.

##### Mostra dels resultats

Quan s'executa la funció `main`, l'usuari pot introduir valors i obtenir resultats. Per exemple:

1. Si l'usuari introdueix `48` i `18`:

   ```
   El maxim comu divisor es: 6
   ```

2. Si l'usuari introdueix `5` per al factorial:
   ```
   El factorial es: 120
   ```

Aquestes sortides il·lustren els càlculs del MCD i el factorial basats en els valors introduïts per l'usuari.

### Operacions amb Llistes

#### Introducció

Aquest codi implementa operacions bàsiques amb llistes en Scheme. Utilitza diverses funcions integrades per treballar amb llistes, com ara `car`, `cdr`, `cons` i `null?`. La funció `main` mostra exemples d'aquestes operacions interactivament.

#### Contingut del codi

##### Definicions de la funció

1. **Funció `main`**

   ```scheme
   (define (main)
       (let ((llista (read)))
           (display (car llista))
           (newline)
           (display (cdr llista))
           (newline)
           (display (cons 0 llista))   ; esperat: '(0 1 2 3 4 5)
           (newline)
           (display (null? '()))
           (newline)
           (display (null? llista))
           (newline)))
   ```

   Aquesta funció:

   - Llegeix una llista introduïda per l'usuari.
   - Mostra el primer element de la llista utilitzant `car`.
   - Mostra la resta de la llista (sense el primer element) utilitzant `cdr`.
   - Afegeix un element `0` al principi de la llista amb `cons`.
   - Comprova si una llista està buida amb `null?`.

##### Mostra dels resultats

Quan s'executa la funció `main`, l'usuari pot introduir una llista i obtenir resultats. Per exemple:

1. Si l'usuari introdueix `'(1 2 3 4 5)`:

   ```
   1
   (2 3 4 5)
   (0 1 2 3 4 5)
   #t
   #f
   ```

   - `1` és el primer element de la llista.
   - `(2 3 4 5)` és la resta de la llista.
   - `(0 1 2 3 4 5)` és la nova llista amb `0` al davant.
   - `#t` indica que la llista buida (`'()`) és veritablement buida.
   - `#f` indica que la llista introduïda no és buida.

### Operacions Matemàtiques i Comparacions

#### Introducció

Aquest codi implementa operacions matemàtiques bàsiques i comparacions lògiques entre variables. Es defineixen tres variables (`a`, `b`, i `c`) i es mostren resultats d'operacions aritmètiques i comparatives utilitzant funcions integrades de Scheme.

#### Contingut del codi

```scheme
(define (main)
   (display (+ a b))
   (newline)

   (display (- b a))
   (newline)

   (display (* a b))
   (newline)

   (display (/ b a))
   (newline)

   (display (> b a))
   (newline)

   (display (< b a))
   (newline)

   (display (= b c))
   (newline)

   (display (<= b a))
   (newline)
   (display (<= b c))
   (newline)

   (display (>= a b))
   (newline)
   (display (>= b c))
   (newline)

   (display (<> a b))
   (newline)
   (display (<> b c))
   (newline)

   (display (< a b c))
   (newline)

   (display (<= a b c))
   (newline))
```

##### Definicions i operacions

1. **Definicions de les variables**

   ```scheme
   (define a 10)
   (define b 20)
   (define c 20)
   ```

   Es defineixen tres variables: `a`, `b` i `c` amb els valors `10`, `20`, i `20` respectivament.

2. **Operacions matemàtiques**

   ```scheme
   (display (+ a b))
   (newline)

   (display (- b a))
   (newline)

   (display (* a b))
   (newline)

   (display (/ b a))
   (newline)
   ```

   Aquestes operacions calculen:

   - La suma de `a` i `b`.
   - La resta de `b` menys `a`.
   - El producte de `a` i `b`.
   - La divisió de `b` entre `a`.

3. **Comparacions**

   ```scheme
   (display (> b a))
   (newline)

   (display (< b a))
   (newline)

   (display (= b c))
   (newline)

   (display (<= b a))
   (newline)
   (display (<= b c))
   (newline)

   (display (>= a b))
   (newline)
   (display (>= b c))
   (newline)
   ```

   Aquestes comparacions mostren:

   - Si `b` és major que `a`.
   - Si `b` és menor que `a`.
   - Si `b` és igual a `c`.
   - Si `b` és menor o igual a `a`.
   - Si `b` és menor o igual a `c`.
   - Si `a` és major o igual a `b`.
   - Si `b` és major o igual a `c`.

4. **Comparacions lògiques complexes**

   ```scheme
   (display (< a b c))
   (newline)

   (display (<= a b c))
   (newline)
   ```

   Aquestes expressions comproven si:

   - `a`, `b` i `c` estan en ordre creixent.
   - `a`, `b` i `c` estan en ordre creixent o igual.

##### Mostra dels resultats

Quan s'executa aquest codi, els resultats esperats són:

1. Operacions matemàtiques:

   ```
   30
   10
   200
   2
   ```

2. Comparacions simples:

   ```
   #t
   #f
   #t
   #f
   #t
   #f
   #t
   ```

3. Comparacions complexes:
   ```
   #t
   #t
   ```

Aquestes sortides mostren els resultats de les operacions aritmètiques i les verificacions lògiques aplicades a les variables `a`, `b` i `c`.

## Ús

Abans de fer-ne ús, s'han hagut de generar els arxius. Es pot usar de dos maneres:

```sh
python3 scheme.py <arxiu> < entrada > sortida
```

```sh
make run file=<arxiu>
```

### Generar Arxius

Per generar els arxius necessaris a partir de la gramàtica `scheme.g4`, executar:

```sh
make
```

O alternativament:

```sh
make generate
```

També pots netejar el teu directori dels arxius generats amb

```sh
make clean
```
