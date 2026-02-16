from PIL import Image 
from pdf2image import convert_from_path
import os,subprocess as spr
##PDF_path = r"C:\Users\abenna\Desktop\conference-latex-template_10-17-19\Journals-articles\Motor_imagery_delta_LH,RH,LL,RL_1"
pdf_name="Annexe7.pdf"
#print(PDF_file)
pages = convert_from_path(pdf_name, 300)
imagelist=[]
##rec_dir=r"c:\users\abenna\desktop\pdftoimages"
pages[0].save('PageGarde.png')
##for i,d in enumerate(pages[1:]):
##    imagelist.append(d.convert('RGB'))
##    d.save(rec_dir+'\\'+'page_%d.png'%(i+1))
##pages[0].save(PDF_path+"\\"+"ST_EN_Springer (Proceedings) - Copy_im.pdf",save_all=True, append_images=imagelist)

