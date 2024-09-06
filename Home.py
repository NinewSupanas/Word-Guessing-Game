import random

#คำศัพท์ที่ให้ทาย
words =["python", "Programming", "Computer", "Java"]

#สุ่มคำ
word =random.choice(words)
word_display=['_']*len(word)
attempts= 3 #ทายผิดสามครั้ง

#ฟังก์ชันแสดงสถานะคำที่ทาย
def display_Status():
    print("คำ:"+''.join(word_display))

print("ยินดีต้อนรับ!") 
display_Status()

while attempts > 0 and '_'in word_display: 
    guess = input("ใส่ตัวอักษรที่ต้องการทาย: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("กรุณาใส่เพียงตัวอักษรภาษาอังกฤษ 1 ตัว")
        continue

    if guess in word:
        for index, letter in enumerate(word):
            if letter == guess:
                word_display[index] = guess
            print(f"ถูกต้อง ตัวอักษร '{guess}' อยู่ในคำ")
    else:
        attempts -= 1
        print(f"ไม่ถูกต้อง ตัวอักษร '{guess}' ไม่อยู่ในคำ คุณมีโอกาสอีก {attempts} ครั้ง")

    display_Status()

if '_' not in word_display:
    print("คุณทายถูก:" +word)
else:
    print("คุณทายผิด เฉลยคือ  {word}")


