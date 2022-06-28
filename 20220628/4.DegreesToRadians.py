#각도를 라디안으로 바꾸기
#角度をラジアンに変える
from math import radians, pi

# 방법1　方法１

def DegreesToRadians(deg):
    return radians(deg)

print(DegreesToRadians(12)) #0.20943951023931956
print(DegreesToRadians(73)) #1.2740903539558606

# 방법2　方法２

def DegreesToRadians_2(deg):
    return (pi*deg)/180

print(DegreesToRadians_2(12)) #0.20943951023931953
print(DegreesToRadians_2(73)) #1.2740903539558606
