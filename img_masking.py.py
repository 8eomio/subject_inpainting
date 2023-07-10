import cv2
import numpy as np
import argparse


def draw_mask(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        param['drawing'] = True
        param['ix'], param['iy'] = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if param['drawing'] == True:
            cv2.rectangle(param['img'], (param['ix'], param['iy']), (x, y), (255, 255, 255), -1)

    elif event == cv2.EVENT_LBUTTONUP:
        param['drawing'] = False
        cv2.rectangle(param['img'], (param['ix'], param['iy']), (x, y), (255, 255, 255), -1)


def draw_mask_on_image(image_path):
    img = cv2.imread(image_path)
    mask = np.zeros_like(img, dtype=np.uint8)

    cv2.namedWindow('image')
    cv2.setMouseCallback('image', draw_mask, {'drawing': False, 'ix': -1, 'iy': -1, 'img': mask})

    while True:
        img_show = cv2.bitwise_or(img, mask)
        cv2.imshow('image', img_show)
        k = cv2.waitKey(1) & 0xFF
        if k == ord('s'):  # press 's' to save and exit
            cv2.imwrite('mask.png', mask)
            cv2.destroyAllWindows()
            break
        elif k == 27:  # press 'ESC' to exit without saving
            cv2.destroyAllWindows()
            break


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Draw a mask on an image.')
    parser.add_argument('image_path', type=str, help='The path to the image file')

    args = parser.parse_args()

    draw_mask_on_image(args.image_path)
