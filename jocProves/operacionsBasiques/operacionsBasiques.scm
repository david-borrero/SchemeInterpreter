(define a 10)
(define b 20)
(define c 20)

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