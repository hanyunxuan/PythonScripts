 from PyCPX import CPlexModel
 from numpy import array, arange

 A = 2*arange(1,10).reshape( (3, 3) )
 m = CPlexModel()

 X = m.new( (3, 3), vtype = int)
 u = m.new( 3, vtype = int)
 s = m.new(vtype = int)

 m.constrain(s <= A.T * X <= 10*s)
 m.constrain(1 <= X.sum(axis = 1) <= u)

