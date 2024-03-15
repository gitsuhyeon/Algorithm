import math
def solution(brown, yellow):
    answer = []
    """x=0
    y=0
    2x + 2y  =brown+4
    brown +yellow = xy
    x= (b+yw)/y
    2(b+w)/y + 2y = b+4
    y^2 - (b+4)/2y + (b+w)=0
    y = sqrt(-b-w+(b+4)^2/16)+ (b+4)/2"""
    y = math.sqrt((brown+4)**2/16-brown-yellow) +(brown+4)/4
    x = brown/2 +2 -y
    if y > x:
        x, y = y, x
    answer = [x,y]
    return answer