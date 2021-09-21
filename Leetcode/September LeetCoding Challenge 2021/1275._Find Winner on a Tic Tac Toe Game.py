class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        if len(moves)<5:
            return "Pending"
        l1=[None]*9
        for i in range(len(moves)):
            rows=moves[i][0]
            cols=moves[i][1]
            if i%2==0:
                l1[3*rows+cols]='X'
            else:
                l1[3*rows+cols]='O'
        if l1[0]==l1[1]==l1[2]=='X' or l1[3]==l1[4]==l1[5]=='X' or l1[6]==l1[7]==l1[8]=='X' or l1[0]==l1[3]==l1[6]=='X' or l1[1]==l1[4]==l1[7]=='X' or l1[2]==l1[5]==l1[8]=='X' or l1[0]==l1[4]==l1[8]=='X' or l1[2]==l1[4]==l1[6]=='X':
            return "A"
        if l1[0]==l1[1]==l1[2]=='O' or l1[3]==l1[4]==l1[5]=='O' or l1[6]==l1[7]==l1[8]=='O' or l1[0]==l1[3]==l1[6]=='O' or l1[1]==l1[4]==l1[7]=='O' or l1[2]==l1[5]==l1[8]=='O' or l1[0]==l1[4]==l1[8]=='O' or l1[2]==l1[4]==l1[6]=='O':
                return 'B'
        if len(moves)==9:
            return "Draw"
        return 'Pending'

            
            
        
        
