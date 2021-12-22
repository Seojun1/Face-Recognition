import cv2

# haarcascade 선언
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_alt.xml')
eye_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_eye.xml')

cv2.WINDOW_AUTOSIZE

# 이미지 가져오기
img = cv2.imread('1.jpg')
color = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 안면 구현

# Cascade classifier를 이용해 얼굴을 찾음.
face = face_cascade.detectMultiScale(color, 1.3, 5)
#얼굴에 사각형을 그리고 눈을 찾는다.
for (x, y, w, h) in face:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # 눈 구현

    # 이미지를 얼굴 크기 만큼 잘라서 color스케일 이미지와 clolor2를 만듬
    eye_color = img[y:y + h, x:x + w]
    eye_color2 = color[y:y + h, x:x + w]
    # 등록한 cascade classifier를 이용해 눈을 찾음.
    eyes = eye_cascade.detectMultiScale(eye_color2)
    # 눈: 이미지 프레임에 (x, y)에서 시작, (x+넓이, y+길이)까지의 사각형을 그림.
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(eye_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

# image 출력
cv2.imshow('image', img)

key = cv2.waitKey(0)
cv2.destroyAllWindows()
