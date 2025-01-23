import cv2

def capture_and_decorate_image():
    # 카메라 캡쳐 객체, 0은 컴퓨터의 기본 카메라
    cap = cv2.VideoCapture(0)

    # 카메라가 정상적으로 열리지 않은 경우
    if not cap.isOpened():
        print("카메라를 열 수 없습니다.")
        exit()

    while True:
        # 카메라 프레임 읽기
        ret, frame = cap.read()

        # 프레임을 제대로 읽지 못했다면 중단
        if not ret:
            print("프레임을 읽을 수 없습니다.")
            break

        # 프레임에 텍스트 추가
        cv2.putText(frame, '사진 찍는 중!', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
        
        # 프레임에 원 추가
        cv2.circle(frame, (320, 240), 100, (0, 255, 0), 3)

        # 꾸며진 프레임 표시
        cv2.imshow('Decorated Camera', frame)

        # 'q' 키를 누르면 루프에서 탈출
        if cv2.waitKey(1) == ord('q'):
            break
        # 'c' 키를 누를 경우 이미지 캡처 및 저장
        elif cv2.waitKey(1) == ord('c'):
            cv2.imwrite('decorated_image.jpg', frame)
            print("이미지가 저장되었습니다.")

    # 작업 완료 후 해제
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    capture_and_decorate_image()
