np(everyone).
np(someone).
np(alex).
v(loves).

s([H|T]) :-
	np(H), vp(T).

vp([H|[T]]) :-
	v(H), np(T).
