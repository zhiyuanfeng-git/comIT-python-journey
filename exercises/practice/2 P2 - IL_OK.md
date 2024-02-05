## Introduction to logics

1. Build the truth tables for the following propositional forms.
   * ~q v (p ^ q)
     | p | q | ~q | p ^ q | ~q v (p ^ q) |
     |---|---|----|-------|--------------|
     | T | T |  F |  T    |     T        |
     | T | F |  T |  F    |     T        |
     | F | T |  F |  F    |     F        |
     | F | F |  T |  F    |     T        |
   * ~p -> q
     | p | q | ~p | ~p -> q      |
     |---|---|----|--------------|
     | T | T | F  |    T         |
     | T | F | F  |    T         |
     | F | T | T  |    T         |
     | F | F | T  |    F         | 
   * p ^ q <-> q ^ p
     | p | q | p ^ q | q ^ p | p ^ q <-> q ^ p |
     |---|---|-------|-------|-----------------|
     | T | T |  T    |  T    | T               |
     | T | F |  F    |  F    | F               |
     | F | T |  F    |  F    | F               |
     | F | F |  F    |  F    | F               |
    * a ^ (b v ~a)
     | a | b | ~a  | b v ~a | a ^ (b v ~a) |
     |---|---|-----|--------|--------------|
     | T | T | F   | T      |  T           |
     | T | F | F   | F      |  F           |
     | F | T | T   | T      |  F           |
     | F | F | T   | T      |  F           |
2. Interpret the previous propositional forms.
   * ~q v (p ^ q)
     * ~q represents the negation of q.
     * (p ^ q) represents the conjunction of p and q.
     * ~q v (p ^ q) represents the disjunction of ~q and (p ^ q).
     * if q is true, then ~q is false, and (p ^ q) is determined by the value of p.
       * if p is true, then (p ^ q) is true.
       * if p is false, then (p ^ q) is false. 
     * if q is false, then ~q is true, and (p ^ q) is false regardless of the value of p.
   * for example:
     * Let p be "The ground is white."
     * Let q be "It is snowy."
    The propositional form ~q v (p ^ q) would be interpreted as "It is not snowy or (the ground is white and it is snowy)."
     * The ground is white(p is true) and it is snowy(q is true),it says both p and q are true, then (p ^ q) is true, and the entire statement is true.
     * It is not snowy(q is false),then ~q is true,and the entire statement is true.
     * The ground is not white(p is false), then (p ^ q) is false. It is snowy(q is true), then ~q is false. so the entire statement is false.
     * It is not snowy(q is false), then ~q is true, and the entire statement is true.

3. Build the truth tables for the following propositional forms.
   * p -> (q -> r)
   | p | q | r | q -> r | p -> (q -> r) |
   |---|---|---|--------|---------------|
   | T | T | T |   T    |       T       |
   | T | T | F |   F    |       F       |
   | T | F | T |   T    |       T       |
   | T | F | F |   T    |       T       |
   | F | T | T |   T    |       T       |
   | F | T | F |   F    |       T       |
   | F | F | T |   T    |       T       |
   | F | F | F |   T    |       T       |
   * (p ^ q) -> r
   | p | q | r | p ^ q | (p ^ q) -> r |
   |---|---|---|-------|--------------|
   | T | T | T |   T   |      T       |
   | T | T | F |   T   |      F       |
   | T | F | T |   F   |      T       |
   | T | F | F |   F   |      T       |
   | F | T | T |   F   |      T       |
   | F | T | F |   F   |      T       |
   | F | F | T |   F   |      T       |
   | F | F | F |   F   |      T       |

4. Build the truth tables for the following propositional forms.
   * (p -> q) ^ (q -> r)
   | p | q | r | p -> q | q -> r | (p -> q) ^ (q -> r) |
   |---|---|---|--------|--------|---------------------|
   | T | T | T |    T   |   T    |         T           |
   | T | T | F |    T   |   F    |         F           |
   | T | F | T |    F   |   T    |         F           |
   | T | F | F |    F   |   T    |         F           |
   | F | T | T |    T   |   T    |         T           |
   | F | T | F |    T   |   F    |         F           |
   | F | F | T |    T   |   T    |         T           |
   | F | F | F |    T   |   T    |         T           |

   * ( p -> q ) -> r
   | p | q | r | p -> q | (p -> q) -r |
   |---|---|---|--------|-------------|
   | T | T | T |   T    |      T      |
   | T | T | F |   T    |      F      |
   | T | F | T |   F    |      T      |
   | T | F | F |   F    |      T      |
   | F | T | T |   T    |      T      |
   | F | T | F |   T    |      F      |
   | F | F | T |   T    |      T      |
   | F | F | F |   T    |      T      |