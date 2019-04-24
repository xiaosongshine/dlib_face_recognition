import dlib
from imageio import imread
import glob


detector = dlib.get_frontal_face_detector()
win = dlib.image_window()

path = "f1.jpg"
img = imread(path)
dets = detector(img)
print('检测到了 %d 个人脸' % len(dets))
for i, d in enumerate(dets):
	print('- %d：Left %d Top %d Right %d Bottom %d' % (i, d.left(), d.top(), d.right(), d.bottom()))

win.clear_overlay()
win.set_image(img)
win.add_overlay(dets)
dlib.hit_enter_to_continue()
