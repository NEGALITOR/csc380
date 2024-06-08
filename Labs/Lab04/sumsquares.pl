sumsquares(X, 1) :-
    X = 1.

sumsquares(X, Y) :-
    S is X - 1,
    sumsquares(S, Z),
    Y is X * X + Z.