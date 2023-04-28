import random
def toBase(num,base):  #Maximum base - 36
  base_num = ""
  while num>0:
    dig = int(num%base)
    if dig<10:
      base_num += str(dig)
    else:
      base_num += chr(ord('A')+dig-10)  #Using uppercase letters
    num //= base
  base_num = base_num[::-1]  #To reverse the string
  return base_num
maxBase = 36
sList = ["₀", "₁", "₂", "₃", "₄", "₅", "₆", "₇", "₈", "₉", "₁₀", "₁₁", "₁₂", "₁₃", "₁₄", "₁₅", "₁₆", "₁₇", "₁₈", "₁₉", "₂₀", "₂₁", "₂₂", "₂₃", "₂₄", "₂₅", "₂₆", "₂₇", "₂₈", "₂₉", "₃₀", "₃₁", "₃₂", "₃₃", "₃₄", "₃₅", "₃₆"]
wList = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty", "twenty-one", "twenty-two", "twenty-three", "twenty-four", "twenty-five", "twenty-six", "twenty-seven", "twenty-eight", "twenty-nine", "thirty", "thirty-one", "thirty-two", "thirty-three", "thirty-four", "thirty-five", "thirty-six"]
uList = [max((bb+1)*10, bb**2+bb+1) for bb in range(maxBase+1)]
for ui in range(len(uList)):
  if uList[ui] > 1000:
    uList[ui] = 100
with open("base-counts.txt", "w", encoding = 'utf-8') as f:
  f.write(f"Here are some examples of counting in different base systems. For clarity, the numbers in these examples have a subscripted base number (in base ten format) attached to each of them to clarify what base system the number is written in. Notice that base 1 is not represented here because, unlike the other base systems, starting the unique digits with zero and including no more of them than the number of the base would mean 0 would be the only available digit, and since 0 times 1 to any power is zero the only number we could represent this way is zero.\n\n")
  '''
  icount = 1
  ss = sList[icount]
  upto = uList[icount]
  f.write(f"Counting to {upto}⏨ in base {wList[icount]}: 1{sList[icount]}")
  for n in range(2, upto+1):
    bnum = "1"*n
    f.write(f", {bnum}{sList[icount]}")
  f.write(f".\n\n")
  '''
  for icount in range (2, maxBase+1):
    baseStr = toBase(icount, 10)
    ss = sList[icount]
    upto = uList[icount]
    f.write(f'Base "{baseStr}⏨": Counting to {upto}₁₀ in base {wList[icount]}: 1{sList[icount]}')
    for n in range(2, upto+1):
      bnum = toBase(n, icount)
      f.write(f", {bnum}{sList[icount]}")
    f.write(f".\n\n")
f.close()
#😄😄Alt+x