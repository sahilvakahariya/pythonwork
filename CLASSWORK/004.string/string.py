st = "Sun rises in East"

print(len(st))
print(st.lower())
print(st.casefold())
print(st.upper())
print(st.capitalize())
print(st.title())
print(st.strip())

print(st.replace("s","Z",2))

print(st.find("Sun"))

print(st.startswith("S"))
print(st.endswith("k"))

print(st.split(" "))

k = "A"
print(k.join("XYZ"))

print("abc1".isalpha())
print("2343".isdigit())
print("abc1$".isalnum())

print("abc".zfill(15))
print("abc".center(11,'#'))


st = "SunrisesinEast"
print(st)
print(st[2:])
print(st[:5])
print(st[2:5])
print(st[-5:-1])
print(st[1:9:2])
print(st[::-1])