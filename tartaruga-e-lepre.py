import random

def stampa_corsia(pos_t, pos_h):
    corsia = ['_'] * 70
    
    if pos_t == pos_h:
        corsia[pos_t - 1] = 'OUCH!!!'
    else:
        corsia[pos_t - 1] = 'T'
        corsia[pos_h - 1] = 'H'
        
    print(''.join(corsia))

def mossa_tartaruga(pos):
    mossa = random.randint(1, 10)
    if 1 <= mossa <= 5:
        pos += 3  # Passo veloce
    elif 6 <= mossa <= 7:
        pos -= 6  # Scivolata
    else:
        pos += 1  # Passo lento

    if pos < 1:
        pos = 1
    return pos

def mossa_lepre(pos):
    mossa = random.randint(1, 10)
    if 1 <= mossa <= 2:
        pos += 0  # Riposo
    elif 3 <= mossa <= 4:
        pos += 9  # Grande balzo
    elif mossa == 5:
        pos -= 12  # Grande scivolata
    elif 6 <= mossa <= 8:
        pos += 1  # Piccolo balzo
    else:
        pos -= 2  # Piccola scivolata

    if pos < 1:
        pos = 1
    return pos

def gara():
    print('BANG !!!!! AND THEY\'RE OFF !!!!!')
    pos_tartaruga = 1
    pos_lepre = 1
    
    while pos_tartaruga < 70 and pos_lepre < 70:
        pos_tartaruga = mossa_tartaruga(pos_tartaruga)
        pos_lepre = mossa_lepre(pos_lepre)
        stampa_corsia(pos_tartaruga, pos_lepre)
        
        if pos_tartaruga >= 70 and pos_lepre >= 70:
            print("IT'S A TIE.")
            return
        elif pos_tartaruga >= 70:
            print("TORTOISE WINS! || VAY!!!")
            return
        elif pos_lepre >= 70:
            print("HARE WINS || YUCH!!!")
            return

gara()


    
     
        
    
    
    
    
    





