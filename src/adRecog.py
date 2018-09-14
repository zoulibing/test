from keras.layers import Dense,Conv2D,Dropout
import cv2 as cv
path='/home/li/zoulb/datasets/datasets/train/'
path_yolo='/home/li/zoulb/datasets/yolo_datasets/train/'


def showimage(im_name,points):
    im=cv.imread(path+im_name)
    print (points)
    cv.rectangle(im,points[0],points[1],(255, 0, 0))
    cv.imshow('im',im)
    cv.waitKey(1000)

def yoloFormatC(src_f,obj_f):
    print ('begin convert format')
    f = open(src_f)
    fw= open(obj_f,'w')
    width=416
    height=416
    scalar_x=0.0
    scalar_y=0.0
    yolo_path=''


    lines = f.readlines()
    pre = '';
    pre_pic=''
    tmp=''

    results=list()
    im=None
    for str in lines:
        #print(str)
        strs=str.split()
        if len(strs)>3:
            if(pre_pic==strs[0]):

                x_min = int(int(strs[2]) * scalar_x)
                y_min = int(int(strs[3]) * scalar_y)
                x_max = int(int(strs[4]) * scalar_x)
                y_max = int(int(strs[5]) * scalar_y)

                frame_str = '{},{},{},{},{}'.format(x_min, y_min, x_max, y_max, strs[1])
                tmp=tmp+' '+frame_str
                cv.rectangle(im, (x_min, y_min), (x_max,y_max), (255, 0, 0))
            else:
                if len(tmp)>10:
                    scalar_x = 0.0
                    scalar_y = 0.0
                    results.append(tmp+'\n')
                    print(tmp)
                    #cv.imwrite(yolo_path,im)
                    tmp=''
                    #cv.imshow('im', im)
                    #cv.waitKey(1000)
#
                pre_pic=strs[0]
                im = cv.imread(path+strs[0])
                yolo_path=path_yolo+strs[0]
                scalar_x = width / im.shape[1]
                scalar_y = height / im.shape[0]

                x_min = int(int(strs[2]) * scalar_x)
                y_min = int(int(strs[3]) * scalar_y)
                x_max = int(int(strs[4]) * scalar_x)
                y_max = int(int(strs[5]) * scalar_y)

                frame_str = '{},{},{},{},{}'.format(x_min, y_min, x_max, y_max, strs[1])
                tmp = path_yolo + strs[0] + ' ' + frame_str
                print(im.shape)
                im = cv.resize(im, (width, height), interpolation=cv.INTER_CUBIC)
                cv.rectangle(im, (x_min, y_min), (x_max, y_max), (255, 0, 0))

    fw.writelines(results)
    fw.close()
    f.close()
    return results




def loadDatas(file,isshow):
    f=open(file)
    pics=list()
    lines=f.readlines()
    pre='';

    for str in lines:
        print(str)
        strs=str.split()
        if isshow:
            pics.append(str)
            lrs=[(int(strs[2]),int(strs[3])),(int(strs[4]),int(strs[5]))]
            showimage(strs[0],lrs)
    return pics


if __name__ == '__main__':
    #pics=loadDatas('/home/li/zoulb/datasets/datasets/train.txt',True)
    pics = yoloFormatC('/home/li/zoulb/datasets/datasets/train.txt','/home/li/zoulb/datasets/datasets/for_yolo.txt')
    for info in pics:
        print (info)

