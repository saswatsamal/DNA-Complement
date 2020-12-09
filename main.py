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
    else:
        return 'N'


def reverse_complement(seq):
    
    
    
    rev_seq = ''
    
    
    for base in reversed(seq):
        rev_seq += complement_base(base)
        
    print("Reverse: ",rev_seq)
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

    
