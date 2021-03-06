#라디안을 각도로 바꾸기
#ラジアンを角度に変える
from math import degrees, pi

# 방법1　方法１

def RadiansToDegrees(rad):
    return degrees(rad)

print(RadiansToDegrees(0.22)) #12.60507149287811
print(RadiansToDegrees(1.28)) #73.33859777674537

# 방법2　方法２

def RadiansToDegrees_2(rad):
    return (rad*180.0)/pi

print(RadiansToDegrees_2(pi/2)) #90.0
