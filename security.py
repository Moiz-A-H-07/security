import cv2
import dropbox
import time
import random
starttime=time.time()
def takesnapshot():
    number=random.randint(0,100)
    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=videoCaptureObject.read()
        img_name="img"+str(number)+".png"
        cv2.imwrite(img_name,frame)
        starttime=time.time()
        result=False
    return img_name
    print("snapshot taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()
def uploadfiles(img_name):
    accesstoken:'sl.AuWIf3mT0OPxNvC3FAjj42W2Ejnhq1PO_uJKciHDg5gDKAvlsGMn295Xsq-DUFvGdDFUPXs5UHQxfqwncfs8EHTnMzS4hd3OPzlBRVzRU2gwfQuGhmgzK_BL4BfEvn8KVxpAtcw'
    file=img_counter
    filefrom=file
    fileto="/newfolder/"+(img_name)
    dbx=dropbox.Dropbox(accesstoken)
    with open(filefrom,'rb')as f:
        dbx.files_upload(f.read(),fileto,node=dropbox.files.WriteMode.overwrite)
        print("files uploaded")

def main():
    while(True):
        if((time.time()-starttime)>=300):
            name=takesnapshot()
            uploadfiles(name)
main()