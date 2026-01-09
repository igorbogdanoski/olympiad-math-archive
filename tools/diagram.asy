size(200);

pair A = (0, 3);
pair B = (4, 3);
pair C = (0, 0);
pair D = (4, 0);
pair P1 = (1, 3);
pair P2 = (2.5, 1.5);
pair P3 = (1.5, 0);

draw(A--B);
draw(C--D);
draw(P1--P2--P3, blue);
dot(P1);
dot(P2);
dot(P3);