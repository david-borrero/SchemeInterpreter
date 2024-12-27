(define (filter predicat llista)
  (cond
    ((null? llista) '())  ;
    ((predicat (car llista))
     (cons (car llista) (filter predicat (cdr llista))))
    (#t (filter predicat (cdr llista)))))  

(define (map func llista)
  (cond
    ((null? llista) '())
    (else (cons (func (car llista)) (map func (cdr llista))))))

(define (parell? x) (= (mod x 2) 0))
(define (triplica x) (* x 3))

(define (main)
    (display (map triplica (filter parell? '(1 2 3 4 5 6 7 8 9 10)))))