import bitstring
import time

#Reading input file in an array
value = "enwik8"
value1=value+'Binary.txt'
value2=value+'Answer.txt'
#value=value+'.txt'

print('you will find the encrypted file as :'+value1)
print('you will find the file after decryption as :'+value2)

f= open(value,encoding='utf-8')
read_data=f.read()
chars = list(read_data)  


#Initializing the dectionary with all possible characters
EncodingDectionary={}
EncodingIndex=0 

for i in range(1111998):
    x=chr(i)
    EncodingDectionary[x]=i
    EncodingIndex+=1

#Encoding
print('Started Encoding Please Wait...')
startTime = time.time()

BasePointer = ""
MatchingPointer = "" 
BasePointer += chars[0]
EncodingArray=[]
for i in range(len(chars)):
    if i != len(chars) - 1:
        MatchingPointer += chars[i + 1] 
    if (BasePointer + MatchingPointer) in EncodingDectionary:   #There Is Matching
        BasePointer = BasePointer + MatchingPointer 
    else:                                                       #New Entry to the dictionary
        EncodingArray.append(bin(EncodingDectionary[BasePointer])[2:].zfill(24))
        EncodingDectionary[BasePointer + MatchingPointer] = EncodingIndex 
        EncodingIndex+=1
        BasePointer = MatchingPointer
    MatchingPointer = ""
EncodingArray.append(bin(EncodingDectionary[BasePointer])[2:].zfill(24))

print("--- Finished Encoding in %s seconds ---" % (time.time() - startTime))

#Convert bits t bytes
print('Started Converting Please Wait...')
startTime = time.time()

EncodingArray=''.join(EncodingArray)
def String_To_Byte(text):
    i=0
    solly=bytearray()
    while i+8<=len(text):
        b=text[i:i+8]
        b=int(b,2)
        solly.append(b & 0xff)
        i += 8

    remain = len(text) - i
    if remain ==0:
        return solly
    b=text[i:]
    b+='0'*(8-remain)
    b= int(b,2)
    solly.append(b & 0xff)
    return solly

toWrite = String_To_Byte(EncodingArray)
print("--- Finished Converting in %s seconds ---" % (time.time() - startTime))


#Save the file
a= open(value1,'wb')
a.write(toWrite)
a.close()

#Load the file
a2= open(value1,'r')
toRead = bitstring.Bits(a2)

#Convert it back
print('Started Converting Please Wait...')
startTime = time.time()

ReadingData=[]
ReadingData = [int(str(toRead[i : i + 24]),0) for i in range(0, len(toRead), 24)]
   
print("--- Finished Converting in %s seconds ---" % (time.time() - startTime))

#Initializing the dectionary with all possible characters
DecodingDectionary={}
DecodingIndex=0 
  
for i in range(1111998):
    x=chr(i)
    DecodingDectionary[i]=x
    DecodingIndex+=1

#Decoding
print('Started Decoding Please Wait...')
startTime = time.time()

DecodingArray=[]
PreviousEntryIndex = ReadingData[0] 
Pattern = DecodingDectionary[PreviousEntryIndex]
FirstSymbolOfNewEntry=Pattern[0] 
DecodingArray.append(Pattern)
for i in range(len(ReadingData)-1): 
    NewEntryIndex = ReadingData[i + 1] 
    if (NewEntryIndex in DecodingDectionary):
        Pattern = DecodingDectionary[NewEntryIndex]
    else:
        Pattern = DecodingDectionary[PreviousEntryIndex] 
        Pattern = Pattern + FirstSymbolOfNewEntry
    DecodingArray.append(Pattern)
    FirstSymbolOfNewEntry = Pattern[0] 
    DecodingDectionary[DecodingIndex] = DecodingDectionary[PreviousEntryIndex] + FirstSymbolOfNewEntry
    DecodingIndex+=1 
    PreviousEntryIndex = NewEntryIndex

print("--- Finished Decoding in %s seconds ---" % (time.time() - startTime))

DecodingArray=''.join(DecodingArray)
f2= open(value2,'wb')
f2.write(DecodingArray.encode('utf-8', 'ignore'))   

