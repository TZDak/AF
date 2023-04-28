import math
def toBase(num,base,grouping):  #Maximum base - 36
  grouping = int(grouping)
  base_num = ""
  while num>0:
    dig = int(num%base)
    if dig<10:
      base_num += str(dig)
    else:
      base_num += chr(ord('A')+dig-10)  #Using uppercase letters
    num //= base
  base_num = base_num[::-1]  #To reverse the string
  while len(base_num) % grouping:
    base_num = '0' + base_num
  return base_num
print("Working...")
maxBase = 36
sList = ["₀", "₁", "₂", "₃", "₄", "₅", "₆", "₇", "₈", "₉", "₁₀", "₁₁", "₁₂", "₁₃", "₁₄", "₁₅", "₁₆", "₁₇", "₁₈", "₁₉", "₂₀", "₂₁", "₂₂", "₂₃", "₂₄", "₂₅", "₂₆", "₂₇", "₂₈", "₂₉", "₃₀", "₃₁", "₃₂", "₃₃", "₃₄", "₃₅", "₃₆"]
wList = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty", "twenty-one", "twenty-two", "twenty-three", "twenty-four", "twenty-five", "twenty-six", "twenty-seven", "twenty-eight", "twenty-nine", "thirty", "thirty-one", "thirty-two", "thirty-three", "thirty-four", "thirty-five", "thirty-six"]
uList = [10, 20, 30, 36, 42, 47, 54, 61, 70, 9**2, 10**2, 11**2, 12**2, 13**2, 14**2, 15**2, 16**2, 17**2, 18**2, 19**2, 20**2, 21**2, 22**2, 23**2, 24**2, 25**2, 26**2, 27**2, 28**2, 29**2, 30**2, 31**2, 32**2, 33**2, 34**2, 35**2, 36**2]
uList = [max((bb+1)*10, bb**2+bb+1) for bb in range(maxBase+1)]
fwp = []
fwp.append("Using a digit group base conversion table only works for pairs of base numbers for which there is some integer which both are powers of. Base ten is not well suited for that, as the lowest numbered base system it can be converted to of from in this way would be base one-hundred. Notice that representing base 1 using only a zero character would not work, because 0 times 1 is zero. However, it is possible to represent positive and negative integers in any base system without a zero digit. Making use of this option would allow the number of each base to be represented as a single digit within that base, and also note that the ability to avoid using a zero character does not require any changes to the numbering system and does not eliminate the option of using a zero character.")
fwp.append('It is common to imply or assume base ten, which like any other base should never be called "base 10" since every base system can equally be called that when that base system is either expressed or implied, which makes that an ambiguous way to express what numeric base system is being used. However, it is always a bad idea to imply or assume anything which can be efficiently expressed at least once rather than being assumed or implied. If you want to express the use of base ten in a text conversation, use the word-phrase "base ten" which is not ambiguous.')
fwp.append("While it's good to know how to mathematically convert between two numeric base systems, it is also possible with certain pairs of base systems to make reasonably short conversion tables to directly convert each digit or group of a certain number of digits in one system to a digit or groups of a certain number of digits in the other system. Leading zeros can be added or removed as necessary to make the number of digits you're working with into an integer multiple of the number of digits needed for or prodiced by each step in such a conversion process.")
fwp.append("For example, to convert the octal (base eight) number 100101110101101 into quaternary (base 4), you could break it into groups of two octal digits and then convert each of those with a lookup table or conversion dictionary into a group of three quaternaty digits.")
fwp.append("Since the octal number 100101110101101 has an odd number of digits, it needs a leading zero added to be able to break it into groups of two digits.")
fwp.append("So 100101110101101 becomes 0100101110101101, and that sixteen digit octal number breaks into 01 00 10 11 10 10 11 01, in which case each pair of base eight digits is basically an octal representation of a base sixty-four digit.")
fwp.append("Those representations of base sixty-four digits can then be converted from two octal digits each into three quaternary digits each.")
fwp.append("So 01 00 10 11 10 10 11 01 becomes 001 000 020 021 020 020 021 001, which grouped back together is the twenty-four digit quaternary number 001000020021020020021001.")
fwp.append("And as a final cleanup step, the two leading zeros can be removed from 001000020021020020021001 leaving us with the twenty-two digit quaternary number 1000020021020020021001 as a quaternary representation of the same numeric value as the original fifteen digit octal number 100101110101101.")
fwp.append("It is important to note that, this method is efficient for any size number, once such a lookup table has been memorized, and especially efficient for numbers with large numbers of digits, but between bases which would require large conversion tables it is likely not worth memorize such conversion tables and is likely better to simply use mathematical operations such as dividing the value of the number by the target base, using the remainder as a digit in the target base system, and then repeating that process with the results of that division until there is nothing left to divide. For numbers for a fractional part, the process it a bit more complicated.")
fwp.append(f"\n")
fwt = " ".join(fwp)
with open("base-conversions.txt", "w", encoding = 'utf-8') as f:
  f.write(fwt)
  tupDict = dict()
  cutOff = 37
  for nFrom in range (2, 37): #range of bases to convert from.
    for nTo in range (nFrom+1, 37): #range of bases to convert to.
      r = 1
      while r<cutOff and abs((math.log(nFrom**r,nTo) - int(math.log(nFrom**r,nTo)))) > 0.00000001:
        r += 1
      #if r<cutOff:
      #  print(abs((math.log(nFrom**r,nTo) - int(math.log(nFrom**r,nTo)))))
      groupFrom = r
      r = 1
      while r<cutOff and abs((math.log(nTo**r,nFrom) - int(math.log(nTo**r,nFrom)))) > 0.00000001:
        r += 1
      if r<cutOff:
        print(abs((math.log(nTo**r,nFrom) - int(math.log(nTo**r,nFrom)))))
      groupTo = r
      if (groupTo<cutOff) and (groupFrom<cutOff):
        tupDict[(nFrom, nTo)] = (groupFrom, groupTo)
  #f.write(f"{tupDict}\n\n")
  print(f"{tupDict}\n\n")
  for k in tupDict:
    v = tupDict[k]
    # print(k,v)
    nFrom, groupFrom, nTo, groupTo = k[0], v[0], k[1], v[1]
    n = 0
    sFrom = sTo = ""
    dTo = dict()
    dFrom = dict()
    nTo = k[1]
    nFrom = k[0]
    # print(nFrom)
    # print(nTo)
    while (len(sFrom)<=groupFrom) and (len(sTo)<=groupTo):
      sFrom = toBase(n, nFrom, groupFrom)
      sTo = toBase(n, nTo, groupTo)
      if n == 0:
        sFrom = '0' * groupFrom
        sTo = '0' * groupTo
      # print(n, sFrom, sTo)
      if (len(sFrom)<=groupFrom) and (len(sTo)<=groupTo):
        dFrom[sFrom]=sTo
        dTo[sTo]=sFrom
        if len(str(dFrom)) + len(str(dTo)) > 7000:
          break
      n += 1
    gfd = f"a group of {groupFrom} base {wList[nFrom]} digits"
    gtd = f"a group of {groupTo} base {wList[nTo]} digits"
    if groupFrom == 1:
      gfd = f"a single base {wList[nFrom]} digit"
    if groupTo == 1:
      gtd = f"a single base {wList[nTo]} digit"
    # These next two print calls are strictly to show progress.
    print(f"Recording conversion table for groups of {groupFrom} base {wList[nFrom]} digits into groups of {groupTo} base {wList[nTo]} digits.\n")
    print(f"Recording conversion table for groups of {groupTo} base {wList[nTo]} digits into groups of {groupFrom} base {wList[nFrom]} digits.\n\n")
    f.write(f"Here's how {gfd} can easily be directly converted into {gtd} with a simple lookup table or memorized digit group conversions: {dFrom}. There are {len(dFrom)} entries in this lookup table.\n")
    f.write(f"Here's how {gtd} can easily be directly converted into {gfd} with a simple lookup table or memorized digit group conversions: {dTo} There are {len(dTo)} entries in this lookup table.\n\n")
    # print(f"Here's how groups of {groupFrom} base {wList[nFrom]} digits can easily be directly converted into groups of {groupTo} base {wList[nTo]} digits without mathematical calculations: {dFrom}\n")
    # print(f"Here's how groups of {groupTo} base {wList[nTo]} digits can easily be directly converted into groups of {groupFrom} base {wList[nFrom]} digits without mathematical calculations: {dTo}\n\n")
    #i=input()
f.close()
#😄😄Alt+x