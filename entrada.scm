(define (map func llista)
  (cond
    ((null? llista) '())
    (else (cons (func (car llista)) (map func (cdr llista))))))

(define (dobla x) (* x 2))

(display (map dobla '(1 2 3 4)))