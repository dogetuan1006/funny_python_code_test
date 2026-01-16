Score = 0
# Question 1
print ('Question 1: What is "Xin Chao" in English?')
print ('1) Thank you')
print ('2) Hello')
print ('3) See you again')
print ('4) IDK')
a = int(input('Answer: '))
if a == 1:
  print ('That is incorrect')
elif a == 2:
  print ('That is correct')
  Score = Score + 10
elif a == 3:
  print ('That is incorrect')
elif a == 4:
  print ('What?')
else: print ('Error 404 =(')
# Question 2
print ('Question 2: What is 36?')
print ('1) 67 Kid')
print ('2) Well, it is just Thirty Six')
print ('3) Thanh Hoa')
print ('4) Rau Ma')
b = int(input('Answer: '))
if b == 1:
  print ('Wrong Answer Son =(')
elif b == 2:
  print ('Nope')
elif b == 3:
  print ('That is correct')
  Score = Score + 40
elif b == 4:
  print ('Wrong!!!')
else: print ('Error 404 =(')
# Question 3
print ('Question 3: Fill in blank:')
print ('  "Sao Xi Nhan Ben Phai, ..."  ')
print ('1) Ma Chi Lai Di Ben Trai')
print ('2) Cho Toi Xem Giay To Va Dua Xe Vao Le')
print ('3) 67')
print ('4) IDK')
c = int(input('Answer: '))
if c == 1:
  print ('That is correct')
  Score = Score + 50
elif c == 2:
  print ('Nope')
elif c == 3:
  print ('Stop 67!! Kid')
elif c == 4:
  print ('Really?')
else: print ('Error 404 =(')
# Your Result
print ('Your Score: ', Score)
if Score == 0 or Score < 50:
  print('You Failed The Vietnamese Test')
elif Score >= 50:
  print ('Congratulations! You passed the Vietnamese Test')
