import cv2
import numpy as np

def nothing(x):
    pass

drawing = False # true if mouse is pressed

#mouse callback function
def draw(event,x,y,flags,param):
    
    global drawing,r,g,b,z

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.circle(img2,(x,y),z,(b,g,r),-1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
       




# Create a black image, a window
img = np.zeros((300,512,3), np.uint8)
img2 = np.zeros((800,800,3),np.uint8)
img2.fill(255)
cv2.namedWindow('image')
cv2.namedWindow('paint')
cv2.setMouseCallback('paint',draw)



# create trackbars for color change
cv2.createTrackbar('R','image',0,255,nothing)
cv2.createTrackbar('G','image',0,255,nothing)
cv2.createTrackbar('B','image',0,255,nothing)
cv2.createTrackbar('brush radius','image',0,25,nothing)

# create switch for ON/OFF functionality
switch = '0 : OFF \n1 : ON'
cv2.createTrackbar(switch, 'image',0,1,nothing)

while(1):
    cv2.imshow('image',img)
    cv2.imshow('paint',img2)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    # get current positions of four trackbars
    r = cv2.getTrackbarPos('R','image')
    g = cv2.getTrackbarPos('G','image')
    b = cv2.getTrackbarPos('B','image')
    s = cv2.getTrackbarPos(switch,'image')
    z = cv2.getTrackbarPos('brush radius','image')

    if s == 0:
        img[:] = 0
    else:
        img[:] = [b,g,r]


cv2.destroyAllWindows()
