import cv2,os,json
from glob import glob
def yolo_to_coco(bbox,img_width,img_height):
    yolo_x,yolo_y,yolo_w,yolo_h = bbox
    min_x = max(0,int((yolo_x - .5*yolo_w) * img_width))
    min_y = max(0,int((yolo_y - .5*yolo_h) * img_height))
    max_x = min(img_width,int((yolo_x + .5*yolo_w) * img_width))
    max_y = min(img_height,int((yolo_y + .5*yolo_h) * img_height))
    
    return [min_x,min_y,(max_x-min_x),(max_y-min_y)]

image = cv2.imread('./sample_img/sample.jpg')
img_h,img_w,_ = image.shape

with open('./sample_img/sample.txt') as txt_file:
    for lines in txt_file:
        cls,yolo_x,yolo_y,yolo_w,yolo_h = map(float,lines.split('\n')[0].split(' '))
        min_x,min_y,w,h = yolo_to_coco([yolo_x,yolo_y,yolo_w,yolo_h],img_w,img_h)
        cv2.rectangle(image,(min_x,min_y),(w+min_x,h+min_y),(0,0,0),2)
        
cv2.imshow('test',image)
cv2.waitKey(0)
cv2.destroyAllWindows()


    
    