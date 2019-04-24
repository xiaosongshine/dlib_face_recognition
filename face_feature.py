import dlib
from imageio import imread
import glob


detector = dlib.get_frontal_face_detector()
win = dlib.image_window()

predictor_path = 'shape_predictor_68_face_landmarks.dat'
predictor = dlib.shape_predictor(predictor_path)

path = "f2.jpg"
img = imread(path)
dets = detector(img)
print('检测到了 %d 个人脸' % len(dets))


for i, d in enumerate(dets):
	print('- %d: Left %d Top %d Right %d Bottom %d' % (i, d.left(), d.top(), d.right(), d.bottom()))
	shape = predictor(img, d)
	# 第 0 个点和第 1 个点的坐标
	print('Part 0: {}, Part 1: {}'.format(shape.part(0), shape.part(1)))
win.clear_overlay()
win.set_image(img)
win.add_overlay(dets)
win.add_overlay(shape)


dlib.hit_enter_to_continue()
