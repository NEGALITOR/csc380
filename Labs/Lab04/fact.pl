/* Base Case */
fact(X, 1) :-
    X < 2.

/* Rule */
fact(N, X) :-
    F is N - 1,
    factorial(F, Y),
    X is N * Y.