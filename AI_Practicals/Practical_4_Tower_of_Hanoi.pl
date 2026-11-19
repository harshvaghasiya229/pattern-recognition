% Tower of Hanoi in Prolog

% Base case: move one disc
hanoi(1, Source, Destination, _) :-
    write('Move disc from '),
    write(Source),
    write(' to '),
    write(Destination),
    nl.

% Recursive rule: move n discs
hanoi(N, Source, Destination, Auxiliary) :-
    N > 1,
    N1 is N - 1,
    hanoi(N1, Source, Auxiliary, Destination),
    hanoi(1, Source, Destination, Auxiliary),
    hanoi(N1, Auxiliary, Destination, Source).

% Run the program for 3 discs:
% ?- hanoi(3, a, c, b).
