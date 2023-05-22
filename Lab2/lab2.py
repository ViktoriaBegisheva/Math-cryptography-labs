import random

S_box = (
    0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
    0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
    0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
    0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
    0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
    0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
    0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
    0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
    0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
    0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
    0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
    0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
    0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
    0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
    0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
    0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16
)

S_box_inv = (
    0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB,
    0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB,
    0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E,
    0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25,
    0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92,
    0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84,
    0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06,
    0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B,
    0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73,
    0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E,
    0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B,
    0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4,
    0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F,
    0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF,
    0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61,
    0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D,
)

rcon = (
    0x00, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40,
    0x80, 0x1B, 0x36, 0x6C, 0xD8, 0xAB, 0x4D, 0x9A,
    0x2F, 0x5E, 0xBC, 0x63, 0xC6, 0x97, 0x35, 0x6A,
    0xD4, 0xB3, 0x7D, 0xFA, 0xEF, 0xC5, 0x91, 0x39,
)

xtime = (
    0x00, 0x02, 0x04, 0x06, 0x08, 0x0A, 0x0C, 0x0E, 0x10, 0x12, 0x14, 0x16, 0x18, 0x1A, 0x1C, 0x1E,
    0x20, 0x22, 0x24, 0x26, 0x28, 0x2A, 0x2C, 0x2E, 0x30, 0x32, 0x34, 0x36, 0x38, 0x3A, 0x3C, 0x3E,
    0x40, 0x42, 0x44, 0x46, 0x48, 0x4A, 0x4C, 0x4E, 0x50, 0x52, 0x54, 0x56, 0x58, 0x5A, 0x5C, 0x5E,
    0x60, 0x62, 0x64, 0x66, 0x68, 0x6A, 0x6C, 0x6E, 0x70, 0x72, 0x74, 0x76, 0x78, 0x7A, 0x7C, 0x7E,
    0x80, 0x82, 0x84, 0x86, 0x88, 0x8A, 0x8C, 0x8E, 0x90, 0x92, 0x94, 0x96, 0x98, 0x9A, 0x9C, 0x9E,
    0xA0, 0xA2, 0xA4, 0xA6, 0xA8, 0xAA, 0xAC, 0xAE, 0xB0, 0xB2, 0xB4, 0xB6, 0xB8, 0xBA, 0xBC, 0xBE,
    0xC0, 0xC2, 0xC4, 0xC6, 0xC8, 0xCA, 0xCC, 0xCE, 0xD0, 0xD2, 0xD4, 0xD6, 0xD8, 0xDA, 0xDC, 0xDE,
    0xE0, 0xE2, 0xE4, 0xE6, 0xE8, 0xEA, 0xEC, 0xEE, 0xF0, 0xF2, 0xF4, 0xF6, 0xF8, 0xFA, 0xFC, 0xFE,
    0x1B, 0x19, 0x1F, 0x1D, 0x13, 0x11, 0x17, 0x15, 0x0B, 0x09, 0x0F, 0x0D, 0x03, 0x01, 0x07, 0x05,
    0x3B, 0x39, 0x3F, 0x3D, 0x33, 0x31, 0x37, 0x35, 0x2B, 0x29, 0x2F, 0x2D, 0x23, 0x21, 0x27, 0x25,
    0x5B, 0x59, 0x5F, 0x5D, 0x53, 0x51, 0x57, 0x55, 0x4B, 0x49, 0x4F, 0x4D, 0x43, 0x41, 0x47, 0x45,
    0x7B, 0x79, 0x7F, 0x7D, 0x73, 0x71, 0x77, 0x75, 0x6B, 0x69, 0x6F, 0x6D, 0x63, 0x61, 0x67, 0x65,
    0x9B, 0x99, 0x9F, 0x9D, 0x93, 0x91, 0x97, 0x95, 0x8B, 0x89, 0x8F, 0x8D, 0x83, 0x81, 0x87, 0x85,
    0xBB, 0xB9, 0xBF, 0xBD, 0xB3, 0xB1, 0xB7, 0xB5, 0xAB, 0xA9, 0xAF, 0xAD, 0xA3, 0xA1, 0xA7, 0xA5,
    0xDB, 0xD9, 0xDF, 0xDD, 0xD3, 0xD1, 0xD7, 0xD5, 0xCB, 0xC9, 0xCF, 0xCD, 0xC3, 0xC1, 0xC7, 0xC5,
    0xFB, 0xF9, 0xFF, 0xFD, 0xF3, 0xF1, 0xF7, 0xF5, 0xEB, 0xE9, 0xEF, 0xED, 0xE3, 0xE1, 0xE7, 0xE5
)


def SubBytes(state, inv=False):
    if not inv:
        for i in range(4):
            for j in range(4):
                state[i][j] = S_box[state[i][j]]
    else:
        for i in range(4):
            for j in range(4):
                state[i][j] = S_box_inv[state[i][j]]


def ShiftRows(state, inv=False):
    if not inv:
        for i in range(len(state)):
             state[i] = state[i][i:] + state[i][:i]
    else:
        for i in range(1,len(state)):
             state[i] = state[i][-i:] + state[i][:-i]


def mpy(x, y):                  # mpy two 8 bit values
    p = 0b100011011             # mpy modulo x^8+x^4+x^3+x+1
    m = 0                       # m will be product
    for i in range(8):
        m = m << 1
        if m & 0b100000000:
            m = m ^ p
        if y & 0b010000000:
            m = m ^ x
        y = y << 1
    return m

def MixColumns(state,inv=False):
    s=[[0,0,0,0] for i in range(4)]
    if inv:
        for i in range(4):
            for j in range(4):
                s[i][j] = mpy(state[i][j],0x0e)^mpy(state[(i+1)%4][j],0x0b)^mpy(state[(i+2)%4][j],0x0d)^mpy(state[(i+3)%4][j],0x09)
        for i in range(4):
            for j in range(4):
                state[i][j] = s[i][j]
        return state
    for i in range(4):
        for j in range(4):
            #print(i,j,"=",i,j,"*2 ^",(i+1)%4,j,"*3 ^",(i+2)%4,j," ^",(i+3)%4,j," ^",)
            s[i][j] = mpy(state[i][j],2)^mpy(state[(i+1)%4][j],3)^state[(i+2)%4][j]^state[(i+3)%4][j]
    for i in range(4):
        for j in range(4):
            state[i][j] = s[i][j]
    return state



def AddRoundKey(state, key):
    for i in range(4):
        for j in range(4):
            state[i][j] = state[i][j] ^ key[i][j]


def KeyExpansion(key, Nk, Nb, Nr):
    
    w = [[0 for j in range(Nb * (Nr + 1))] for i in range(4)]

    for j in range(Nk):
        for i in range(4):
            w[i][j]=key[j + 4 * i]
        
    for col in range(Nk, Nb*(Nr + 1)): # col - column number
        tmp = [w[row][col-1] for row in range( 4)]
        if col % Nk == 0:
            #rotate
            tmp = [w[row][col-1] for row in range(1, 4)]
            tmp.append(w[0][col-1]) 
            
            # change its elements using Sbox-table like in SubBytes
            for j in range(len(tmp)):        
                sbox_row = tmp[j] // 0x10
                sbox_col = tmp[j] % 0x10
                sbox_elem =  S_box[16*sbox_row + sbox_col]
                tmp[j] = sbox_elem
            
            tmp[0] ^= rcon[col//Nk]
                
        elif Nk > 6 and col % Nk == 4:
            for j in range(len(tmp)):        
                sbox_row = tmp[j] // 0x10
                sbox_col = tmp[j] % 0x10
                sbox_elem =  S_box[16*sbox_row + sbox_col]
                tmp[j] = sbox_elem
              
        for i in range(4):
            w[i][col] = w[i][col - Nk] ^ tmp[i]
    
    #print([[w[i][4 * j:4 * (j + 1)] for i in range(4)] for j in range(len(w[0]) // 4)])
    return [[w[i][4 * j:4 * (j + 1)] for i in range(4)] for j in range(len(w[0]) // 4)]
    
    
class AES:
    def __init__(self, key):
        self.Nk = len(key) // 4
        self.Nb = 4
        self.Nr = 12 if len(key) == 24 else 10 if len(key) == 16 else 14
        self.roundkey = KeyExpansion(key, self.Nk, self.Nb, self.Nr)
        

    def encrypt(self, pt):

        state = [[] for j in range(4)]
        for c in range(self.Nb):
            for r in range(4):
                state[r].append(pt[c + 4 * r])
                
        AddRoundKey(state, self.roundkey[0])
        
        for r in range(1, self.Nr):
            SubBytes(state)
            ShiftRows(state)
            MixColumns(state)
            AddRoundKey(state, self.roundkey[r])
            
        SubBytes(state)
        ShiftRows(state)
        AddRoundKey(state, self.roundkey[-1])

        return state

    def decrypt(self, ct):
        state = [[] for j in range(4)]
        for c in range(self.Nb):
            for r in range(4):
                state[r].append(ct[c + 4 * r])

        AddRoundKey(state, self.roundkey[-1])

        for r in range(self.Nr - 1, 0, -1):
            ShiftRows(state, True)
            SubBytes(state, True)
            AddRoundKey(state, self.roundkey[r])
            MixColumns(state, True)
            
        ShiftRows(state, True)
        SubBytes(state, True)
        AddRoundKey(state, self.roundkey[0])
        return state

def checkAES(n,key,pt,ct=""):
    print(n)
    i=0
    while len(key)*8<n:
        key+=key[i%len(key)]
        i+=1
    
    key=bytes(key,'utf-8')
    print(key)
    pt=bytes(pt,'utf-8')
    print(pt)
    aes_enc = AES(key).encrypt(pt)
    
    l=len(key)
    n=128 if l==16 else 192 if l==24 else 256
    
    print("AES",n,"encryption:")
    s=[]
    for line in aes_enc:
        s0=' '.join(hex(x) for x in line)+" "
        print(s0)
        for i in line: s.append(i)
    #s="\\"+s.replace(" 0", "\\")[1:]
    print(s)
    
    print()
    
    if ct=="": ct=s
    #ct=b'\x6f\xd8\x9d\xed\x29\xa6\x83\xe2\x96\x7d\x18\xe0\x82\x76\xf4\x93'
    aes_dec = AES(key).decrypt(ct)

    s=[]
    print("AES",n,"decryption:")
    for line in aes_dec:
        print(' '.join(hex(x) for x in line))
        for i in line: s.append(i)
    print(s)
    print([chr(i) for i in s])
    print(pt)
    print([i for i in pt])
    print()
    print()



def checkAES128():
    n=128
    key = 'labtasknumberone'
    pt = 'Task number one '
    
    checkAES(n,key,pt)

def checkAES192():
    n=192
    key = 'labtasknumberone'
    pt = 'Task number two '
    
    checkAES(n,key,pt)


def checkAES256():
    n=256
    key = 'labtasknumberone'
    pt = 'Task number thee'
    
    checkAES(n,key,pt)

def to_bin(l):
    s=""
    for i in l:
        for j in i:
            s+=bin(j)
    return s

def pt_changes(aes):
    
    size = 24 if aes == 192 else 16 if aes == 128 else 32
    key = [random.getrandbits(8) for i in range(size)]
    pt_bin = [random.getrandbits(8) for i in range(16)]
    
    su=0
    ct = AES(key).encrypt(pt_bin)
    ct=to_bin(ct)
    for _ in range(1000):
        pt_bin[random.randint(1,len(pt_bin)-1)] = random.getrandbits(8)
        
        ct_changed = AES(key).encrypt(pt_bin)
        ct_changed=to_bin(ct_changed)
        for i in range(4):
            if ct[i]!=ct_changed[i]:
                su += ct[i]!=ct_changed[i]
        ct=ct_changed
    return su / 1000


def key_changes(aes):
    
    size = 24 if aes == 192 else 16 if aes == 128 else 32
    key_bin = [random.getrandbits(8) for i in range(size)]
    pt = [random.getrandbits(8) for i in range(16)]
    
    su=0
    ct = to_bin(AES(key_bin).encrypt(pt))
    
    for _ in range(1000):
        key_bin[random.randint(1,len(key_bin)-1)] = random.getrandbits(8)
        ct_changed = to_bin(AES(key_bin).encrypt(pt))
        for i in range(4):
            if ct[i]!=ct_changed[i]:
                su += ct[i]!=ct_changed[i]
        ct=ct_changed
    return su / 1000


def changes():
    print("AES 128 plain text changes: ", pt_changes(128))
    print("AES 192 plain text changes: ", pt_changes(192))
    print("AES 256 plain text changes: ", pt_changes(256))
    print()
    print("AES 128 key changes: ", key_changes(128))
    print("AES 192 key changes: ", key_changes(192))
    print("AES 256 key changes: ", key_changes(256))


checkAES128()
checkAES192()
checkAES256()
changes()











