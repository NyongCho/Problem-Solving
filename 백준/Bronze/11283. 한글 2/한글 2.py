import sys
input = sys.stdin.readline

text = input().strip()
print(ord(text)-ord('가')+1)