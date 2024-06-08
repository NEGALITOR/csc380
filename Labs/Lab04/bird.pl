hassize(bluebird,small).
hascovering(bird,feathers).
hascolor(bluebird,blue).
hasproperty(bird,flies).
isa(bluebird,bird).
isa(bird,vertebrate).

isbird(Animal) :-
    /* Has any size or any color */
    (isa(Animal, bird),
    hascolor(Animal, _),
    hassize(Animal, _));

    /* ; - Means OR */

    /* Must have feathers and fly. */
    (isa(Animal, vertebrate),
    hascovering(Animal, feathers),
    hasproperty(Animal, flies)).


