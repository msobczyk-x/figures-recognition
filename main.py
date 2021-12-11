import cv2

img = cv2.imread("image.png")

img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
img = cv2.GaussianBlur(img, (5,5),0)

_, progowane = cv2.threshold(img, 100,200,cv2.THRESH_BINARY)

kontury, _ = cv2.findContours(progowane, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

font = cv2.FONT_HERSHEY_SIMPLEX
texted=True

for k in kontury:
    x,y,w,h=cv2.boundingRect(k)

    if w>10 and h>10:
        rogi = cv2.approxPolyDP(k, 0.02 * cv2.arcLength(k, True), True)

        col = (0,0,0)
        text = "*"

        if len(rogi) == 4:
            col=(255,0,0)
            text="prostokat"
        elif len(rogi)==3:
            col=(0,255,0)
            text="trojkat"
        elif len(rogi) > 4:
            col=(0,0,255)
            text="wielokat"
        cv2.drawContours(img,[rogi],0,col,2)

        if texted:
            cv2.putText(img, text, (x,y), font, 0.7, (100,100,100),2)

cv2.imshow("kształty",img)
cv2.waitKey(0)