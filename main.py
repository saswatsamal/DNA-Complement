from prettytable import PrettyTable

def complement_base(base):
        
    if base in 'Aa':
        return 'T'
    elif base in 'Tt':
        return 'A'
    elif base in 'Uu':
        return 'A'
    elif base in 'Gg':
        return 'C'
    elif base in 'Cc':
        return 'G'
    elif base in 'Yy':
        return 'R'
    elif base in 'Rr':
        return 'Y'
    elif base in 'Ss':
        return 'S*'
    elif base in 'Ww':
        return 'W*'
    elif base in 'Kk':
        return 'M'
    elif base in 'Mm':
        return 'K'
    elif base in 'Bb':
        return 'V'
    elif base in 'Vv':
        return 'B'
    elif base in 'Dd':
        return 'H'
    elif base in 'Hh':
        return 'D'
    else:
        return 'N'

def reverse_complement(seq):
    
    rev_seq = ''
    
    for base in reversed(seq):
        rev_seq += complement_base(base)

    print("Reverse:",rev_seq)
    return rev_seq

def display_complements(seq):
      
    rev_comp = reverse_complement(seq)
    
    print(seq)
    
    for base in seq:
        print('|', end='')
    
    print()
            
    for base in reversed(rev_comp):
        print(base, end='')
        
    
seq = input("Enter: ")
display_complements(seq)
print("\n")



x = PrettyTable()


x.field_names = ["Base","Name", "Bases Represented", "Complementary Base"]
x.add_row(["A"	,"Adenine",	"A",	"T"])
x.add_row(["T",	"Thymidine", "T",	"A"])
x.add_row(["U"	,"Uridine(RNA only)",	"U"	,"A"])
x.add_row(["G",	"Guanidine",	"G",	"C"])
x.add_row(["C","Cytidine",	"C",	"G"])
x.add_row(["Y", "pYrimidine",	"C T",	"R"])
x.add_row(["R", "puRine",	"A G",	"Y"])
x.add_row(["S", "Strong(3Hbonds)",	"G C"	,"S*"])
x.add_row(["W", "Weak(2Hbonds)",	"A T",	"W*"])
x.add_row(["K", "Keto",	"T/U G"	,"M"])
x.add_row(["M",	"aMino",	"A C",	"K"])
x.add_row(["B",	"not A",	"C G T",	"V"])
x.add_row(["D",	"not C",	"A G T",	"H"])
x.add_row(["H",	"not G",	"A C T",	"D"])
x.add_row(["V",	"not T/U",	"A C G"	,"B"])
x.add_row(["N",	"Unknown",	"A C G T",	"N"])


print("The IUPAC Degeneracies Table")
print(x)
