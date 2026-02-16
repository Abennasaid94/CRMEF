from PIL import Image
import numpy as np
extense='png'
file_name='IMG-20230308-WA0000.%s'%(extense)
img = Image.open(file_name)
img = img.convert("RGBA")
datas = img.getdata()
trans_d=1 #10, 1
newData = []
for item in datas:
    if sum(np.array(item[:-1]) > 230*np.ones(3))==3:# and item[1] == 255 and item[2] == 255:
        newData.append(tuple(list(item[:-1])+[0]))
    else:
        #item=tuple([0]*3+[item[-1]])# black_color
        newData.append(tuple(list(item[:-1])+[int(item[-1]/trans_d)]))
            #print(item)


img.putdata(newData)
img.save(file_name.split('.%s'%(extense))[0]+'_tr_head.%s'%(extense), "PNG")
