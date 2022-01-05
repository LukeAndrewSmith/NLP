/* p(a,word,weight,b) */
p(a,'this',1,b).
p(a,'this',2,c).
p(b,'assignment',5,e).
p(b,'assignment',1,d).
p(c,'course',2,b).
p(c,'course',3,e).
p(c,'course',2,d).
p(c,'course',1,c).
p(d,'is',4,a).
p(d,'is',2,e).
p(d,'is',4,f).
p(d,'is',1,d).
p(e,'not',10,e).
p(e,'not',2,f).
p(f,'educational',3,d).

search(X,Y) :-
	path(A,X,Y).

path(A,[H],C) :-
	p(A,H,C,B).

path(A,[H|T],Sum) :-
	p(A,H,C1,B),
	path(B,T,C2),
	Sum is C1 + C2.


