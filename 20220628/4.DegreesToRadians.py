#각도를 라디안으로 바꾸기
from math import radians, pi

# 방법1

def DegreesToRadians(deg):
    return radians(deg)

print(DegreesToRadians(12)) #0.20943951023931956
print(DegreesToRadians(73)) #1.2740903539558606

# 방법2

def DegreesToRadians_2(deg):
    return (pi*deg)/180

print(DegreesToRadians_2(12)) #0.20943951023931953
print(DegreesToRadians_2(73)) #1.2740903539558606