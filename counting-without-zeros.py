import random
def toBase(num,base):  #Maximum base - 36
  base_num = ""
  while num>0:
    dig = int(num%(base))
    if dig == 0 and num >= base:
      dig = base
    if dig<10:
      base_num += str(dig)
    else:
      base_num += chr(ord('A')+dig-10)  #Using uppercase letters
    num -= dig
    num //= base
  base_num = base_num[::-1]  #To reverse the string
  return base_num
maxBase = 35
# Superscript ⁰¹²³⁴⁵⁶⁷⁸⁹
# ₐₐbBcCdDₑₑfFgGₕₕᵢᵢⱼⱼₖₖₗₗₘₘₙₙₒₒₚₚqQᵣᵣₛₛₜₜᵤᵤᵥᵥwWₓₓyYzZ
sList = ["₀", "₁", "₂", "₃", "₄", "₅", "₆", "₇", "₈", "₉", "₁₀", "₁₁", "₁₂", "₁₃", "₁₄", "₁₅", "₁₆", "₁₇", "₁₈", "₁₉", "₂₀", "₂₁", "₂₂", "₂₃", "₂₄", "₂₅", "₂₆", "₂₇", "₂₈", "₂₉", "₃₀", "₃₁", "₃₂", "₃₃", "₃₄", "₃₅", "₃₆"]
sList = ["₀", "₁", "₂", "₃", "₄", "₅", "₆", "₇", "₈", "₉", "₁₀", "₁₁", "₁₂", "₁₃", "₁₄", "₁₅", "₁₆", "₁₇", "₁₈", "₁₉", "₂₀", "₂₁", "₂₂", "₂₃", "₂₄", "₂₅", "₂₆", "₂₇", "₂₈", "₂₉", "₃₀", "₃₁", "₃₂", "₃₃", "₃₄", "₃₅", "₃₆"]
wList = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty", "twenty-one", "twenty-two", "twenty-three", "twenty-four", "twenty-five", "twenty-six", "twenty-seven", "twenty-eight", "twenty-nine", "thirty", "thirty-one", "thirty-two", "thirty-three", "thirty-four", "thirty-five", "thirty-six"]
uList = [10, 20, 30, 36, 42, 47, 54, 61, 70, 9**2, 10**2, 11**2, 12**2, 13**2, 14**2, 15**2, 16**2, 17**2, 18**2, 19**2, 20**2, 21**2, 22**2, 23**2, 24**2, 25**2, 26**2, 27**2, 28**2, 29**2, 30**2, 31**2, 32**2, 33**2, 34**2, 35**2, 36**2]
uList = [max((bb+1)*10, bb**2+bb+1) for bb in range(maxBase+1)]
for ui in range(len(uList)):
  if uList[ui] > 1000:
    uList[ui] = 100
with open("bases-without-zeros.txt", "w", encoding = 'utf-8') as f:
  f.write(f"Here are some examples of counting in different base systems without the use of a zero digit. For clarity, the numbers in these examples have a subscripted base number attached to each of them, with the base numbers written in base ten format, to clarify what base system the number is written in. For example, to my knowledge Unicode does not yet have either a subscripted or superscripted letter Q in either uppercase or lowercase, nor do I know of a unicode combining character to make any character into a subscripted character.\n\n")
  for icount in range (1, maxBase+1):
    baseStr = toBase(icount, icount)
    ss = sList[icount]
    upto = uList[icount]
    f.write(f'Base "{baseStr}": Counting to {upto}⏨ in base {wList[icount]}: 1{sList[icount]}')
    for n in range(2, upto+1):
      bnum = toBase(n, icount)
      f.write(f", {bnum}{sList[icount]}")
    f.write(f".\n\n")
  f.write(f'It is worth noting that shifting the normalized group of digits for a base system from starting with "0" to starting with "1" does not exclude the possibility of using a zero character, but rather makes it unnecessary in a variety of circumstances, and also that the base number of each base system can be written as a single digit in that base rather than having every base number be represented as 10 within that base system. Unfortunately, I don not know of a way that I can subscript all such base number representations here, which is why I represented them subscripted in base ten instead.\n\n')
f.close()
#😄😄Alt+x