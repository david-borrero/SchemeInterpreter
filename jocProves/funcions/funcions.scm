(define (suma x y)
    (+ x y))

(define (producte x y)
    (* x y))

(define x (read))
(define y (read))

(define (main)
    (let ((res1 (suma x y))
          (res2 (producte x y)))
        (display res1)
        (newline)
        (display res2)
        (newline)))