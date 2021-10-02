
#pip install easyocr

import easyocr
reader = easyocr.Reader(['en'])
output = reader.readtext('test.jpg')
final_text=""
for i in range(0,len(output)):
    text=output[i][1]
    final_text=final_text +" "+ text
    #print(text)

#print(final_text)
