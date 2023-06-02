num = 414//23
number = input('猜一猜414//23的运行结果吧')
times = 1

while True:
  if times > 2:
    break
  if number.isnumeric():
    if int(number) == num:
      break
    if int(number) > num:
      number = input('不对哦，猜大了')
    else:
      number = input('不对哦，猜小了')
  else:
    number = input('需要在下方输入数字')
  times += 1

if times > 2 and int(number) != num:
  print('三次机会用完了')
else:
  print('恭喜你猜中了')
print('结果是' + str(num))
