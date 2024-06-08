animal(dog)  :- is_true('has fur'), is_true('says woof').
animal(cat)  :- is_true('has fur'), is_true('says meow').
animal(duck) :- is_true('has feathers'), is_true('says quack').
animal(mouse) :- is_true('is small'), is_true('says squeak').

animal(giraffe) :- is_true("is long"), is_true('has long neck')
animal(bear) :- is_true("has fur"), is_true('says roar')
animal(bird) :- is_true("is small"), is_true('says tweet')


is_true(Q) :-
        format("~w?\n", [Q]),
        read(yes).
