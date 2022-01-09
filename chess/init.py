from pieces import *

BR1 = Rook("BR1", "B") 
BK1 = Knight("BK1", "B")
BB1 = Bishop("BB1", "B") 
BQU = Queen("BQU", "B")
BKI = King("BKI", "B")
BB2 = Bishop("BB2", "B")
BK2 = Knight("BK2", "B")
BR2 = Rook("BR2", "B")
BP1 = Pawn("BP1", "B")
BP2 = Pawn("BP2", "B")
BP3 = Pawn("BP3", "B")
BP4 = Pawn("BP4", "B")
BP5 = Pawn("BP5", "B")
BP6 = Pawn("BP6", "B")
BP7 = Pawn("BP7", "B")
BP8 = Pawn("BP8", "B")
WP1 = Pawn("WP1", "W") 
WP2 = Pawn("WP2", "W") 
WP3 = Pawn("WP3", "W") 
WP4 = Pawn("WP4", "W") 
WP5 = Pawn("WP5", "W") 
WP6 = Pawn("WP6", "W") 
WP7 = Pawn("WP7", "W") 
WP8 = Pawn("WP8", "W")
WR1 = Rook("WR1", "W")
WK1 = Knight("WK1", "W")
WB1 = Bishop("WB1", "W")
WQU = Queen("WQU", "W")
WKI = King("WKI", "W")
WB2 = Bishop("WB2", "W")
WK2 = Knight("WK2", "W")
WR2 = Rook("WR2", "W")

board = [
    ['8', str(BR1), str(BK1), str(BB1), str(BQU), str(BKI), str(BB2), str(BK2), str(BR2)],
    ['7', str(BP1), str(BP2), str(BP3), str(BP4), str(BP5), str(BP6), str(BP7), str(BP8)],
    ['6', "---", "---", "---", "---", "---", "---", "---", "---"],
    ['5', "---", "---", "---", "---", "---", "---", "---", "---"],
    ['4', "---", "---", "---", "---", "---", "---", "---", "---"],
    ['3', "---", "---", "---", "---", "---", "---", "---", "---"],
    ['2', str(WP1), str(WP2), str(WP3), str(WP4), str(WP5), str(WP6), str(WP7), str(WP8)],
    ['1', str(WR1), str(WK1), str(WB1), str(WQU), str(WKI), str(WB2), str(WK2), str(WR2)],
    ["-", "-A-", "-B-", "-C-", "-D-", "-E-", "-F-", "-G-", "-H-"]
]
boardtranslation = {
    '8': 0,
    '7': 1,
    '6': 2,
    '5': 3,
    '4': 4,
    '3': 5,
    '2': 6,
    '1': 7,
    'A': 1,
    'B': 2,
    'C': 3,
    'D': 4,
    'E': 5,
    'F': 6,
    'G': 7,
    'H': 8,
}