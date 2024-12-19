(define (aplica-dos-cops f x)
  (f (f x)))

(define (dobla x) (* x 2))
(display (aplica-dos-cops dobla 5))