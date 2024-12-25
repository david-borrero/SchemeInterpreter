(define (factorial n)
  (if (= n 0)
      1
      (* n (factorial (- n 1)))))

(define (mcd a b)
  (if (= b 0)
      a
      (mcd b (mod a b))))

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