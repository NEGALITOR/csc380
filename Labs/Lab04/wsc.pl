/* Facts */
is_in_class(toby,csc380).
is_in_class(bob,csc480).
is_in_class(toby,csc480).
is_in_class(taha, csc323). /* My Fact */
is_in_class(taha, csc245). /* My Fact */


is_in_room(csc480,wsc100).
is_in_room(csc380,wsc238).
is_in_room(csc323, wsc210). /* My Fact */
is_in_room(csc245, wsc230). /* My Fact */


has_temperature(wsc100,65).
has_temperature(wsc238,92).
has_temperature(wsc210, 72). /* My Fact */

/* OLD */
is_hot(Person) :-
    is_in_class(Person, Class),
    is_in_room(Class, Room),
    has_temperature(Room, Temp),
    Temp > 80.

/* NEW */
is_hot(Person) :-
    is_in_class(Person, _),
    is_in_room(_, _),
    has_temperature(_, Temp),
    Temp > 80.
