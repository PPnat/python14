#การแสดงค่าในlist
fruits = ["apple", "banana", "cherry", "watermelon", "blueberry"]
print(fruits[1])
#การเปลี่ยนค่าในlist
fruits[1] = "blackcurrant"
print(fruits[1])
#เปลี่ยนค่าในlistหลายตำแกน่ง
fruits[1:3] = ["kiwi", "mango", "pineapple"]
print(fruits)
fruits.append("orange")
print(fruits)
fruits.insert(3,"grape")
print(fruits)
tropical = ["mango", "pineapple", "papaya"]
fruits.extend(tropical)
print(fruits)
#ลบค่าในlist
fruits.remove("watermelon")
print(fruits)
fruits.pop(1)
#del fruits
fruits.sort(reverse=True)
print(fruits)

#นายพีรณัฐ พลศิริ  M.6/14 17