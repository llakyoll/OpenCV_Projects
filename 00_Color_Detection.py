import cv2 as cv

img = cv.imread('../DATA/color_4.png')
img = cv.resize(img, (600, 600), interpolation=cv.INTER_LINEAR)
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)


def color_picker(event, x, y, flags, params):

    color_name = ''
    if event == cv.EVENT_LBUTTONDOWN:
        point = (x, y)
        pixel_center = hsv[y, x]
        print(pixel_center)
        rbg_color = tuple(img[y, x])
        b, g, r = int(rbg_color[0]), int(rbg_color[1]), int(rbg_color[2])
        hue_value = pixel_center[0]
        validation_value = pixel_center[2]
        if hue_value == 0 and validation_value == 255:
            color_name = 'White'
        elif hue_value == 0 and validation_value == 0:
            color_name = 'Black'
        elif 6 < hue_value < 20 and 200 < validation_value < 256:
            color_name = 'Orange'
        elif 20 < hue_value < 25 and 200 < validation_value < 256:
            color_name = 'Yellow'
        elif 25 < hue_value < 80 and 180 < validation_value < 245:
            color_name = 'Green'
        elif -1 < hue_value < 5 and 200 < validation_value < 256:
            color_name = 'Red'
        elif 80 < hue_value < 120 and 155 < validation_value < 256:
            color_name = 'Blue'
        elif 140 < hue_value < 160 and 200 < validation_value < 256:
            color_name = 'Pink'
        elif 120 < hue_value < 150 and 140 < validation_value < 256:
            color_name = 'Purple'
        elif 10 < hue_value < 15 and 90 < validation_value < 110:
            color_name = 'Brown'
        elif 155 < hue_value < 180 and 190 < validation_value < 256:
            color_name = 'Pink'
        cv.putText(img, color_name, (x, y+20), 0, 0.5, (0, 0, 0), 2)
        cv.circle(img, center=(x, y), radius=3, color=(0, 0, 0), thickness=-1)


cv.namedWindow('Colors')
cv.setMouseCallback('Colors', color_picker)

while True:
    cv.imshow('Colors', img)
    k = cv.waitKey(20) & 0xFF
    if k == 27:
        break


cv.destroyAllWindows()
