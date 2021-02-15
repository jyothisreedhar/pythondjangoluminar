# quantifier means how much quntity


from re import *

pattern = "a"  # check for all a
pattern = "a+"  # any number of a excluding zero number of a or single a or consecuitive a

pattern = "a*"  # any number of a including zero number of a
pattern = "a?"  # occurrence of single a including zero number of a
pattern = "a{2}"  # print group of 2 a
pattern = "a{2,4}"  # maximum 4 number of a minimum 2 number of a
