import time

print(f"Start!")
begin = time.time()
for i in range(1,1000000+1):
  num = i
  while True:
    if num == 1:
      break
    elif num % 2 == 0:
      num = num / 2
    elif num % 2 == 1:
      num = 3 * num + 1
end = time.time()
print(f"End! This took {end - begin} seconds!")
