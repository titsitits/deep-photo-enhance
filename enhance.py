from LPGAN import TF, TF_HDR, FUNCTION
import os

UPLOAD_FOLDER = 'static/data/input'
PROCESSED_FOLDER = 'static/data/output'

photo = '86cbc4e50304576bc52092b6b21655c7_l.png'
file_name = TF_HDR.getInputPhoto(photo)
print(FUNCTION.current_time() + "Processing image " + file_name)
file_out_no_ext = os.path.splitext(photo)[0]+"-enhanced"
enhanced_img_name = TF.processImg(file_name , file_out_no_ext)
enhanced_img = os.path.join(PROCESSED_FOLDER, enhanced_img_name)

print(FUNCTION.current_time() + "Processing HDR image " + file_name)
file_out_no_ext_HDR = os.path.splitext(file_name)[0]+"-HDR"
hdr_img_name = TF_HDR.processImg(file_name , file_out_no_ext_HDR)
hdr_img  = os.path.join(PROCESSED_FOLDER, hdr_img_name)

print(FUNCTION.current_time(), hdr_img)
