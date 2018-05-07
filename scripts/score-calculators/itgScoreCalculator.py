# calculate ITG scores
# ian klatzco, 2016

#enter scores here
fantastic = 467
excellent = 60
great     = 4
decent    = 0
wayoff    = 0
miss      = 0
hold      = 181
holdTotal = 181
minesHit  = 0
roll      = 1
rollTotal = 1


total = (fantastic+excellent+great+decent+wayoff+miss+holdTotal+rollTotal)*5
score = 5*fantastic+4*excellent+2*great+0*decent+(-6)*wayoff+(-12)*miss+5*hold+0*holdTotal+(-6)*minesHit+5*roll+0*rollTotal
percentScore = float(score)/float(total)
print (percentScore)