import cv2
import mediapipe as mp
import time
import math


class poseDetector:
    def __init__(
        self, mode=False, smooth=True, detectionCon=0.5,
        trackCon=0.5
    ):
        self.mode = mode
        self.smooth = smooth
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(
            static_image_mode=self.mode,
            smooth_landmarks=self.smooth,
            min_detection_confidence=self.detectionCon,
            min_tracking_confidence=self.trackCon
        )

    def findPose(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)
        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(
                    img, self.results.pose_landmarks,
                    self.mpPose.POSE_CONNECTIONS
                )
        return img

    def findPosition(self, img, draw=True):
        self.lmList = []
        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h, w, c = img.shape
                # print(id, lm)
                cx, cy = int(lm.x * w), int(lm.y * h)
                self.lmList.append([id, cx, cy])
                # if draw:
                #     cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)
        return self.lmList

    def findAngle(self, img, le1, le2, le3, ri1, ri2, ri3, draw=True):
        # Get the landmarks
        x1, y1 = self.lmList[le1][1:]
        x2, y2 = self.lmList[le2][1:]
        x3, y3 = self.lmList[le3][1:]

        x4, y4 = self.lmList[ri1][1:]
        x5, y5 = self.lmList[ri2][1:]
        x6, y6 = self.lmList[ri3][1:]
        # Calculate the Angle
        angle_le = math.degrees(
            math.atan2(y3 - y2, x3 - x2) - math.atan2(y1 - y2, x1 - x2))
        if angle_le < 0:
            angle_le += 360
        # print(angle)
        print("X4: ", x4, y4)
        print("X5: ", x5, y5)
        print("X6: ", x6, y6)

        angle_re = math.degrees(
            math.atan2(y6 - y5, x6 - x5) - math.atan2(y4 - y5, x4 - x5))
        if angle_re < 0:
            angle_re += 360

        print("Left", angle_le)
        print("Right", angle_re)
        angle_le = 360 - angle_le
        if math.isclose(angle_re, angle_le):
            angle = max(angle_re, angle_le)
            print(math.isclose(angle_re, angle_le), "angle", angle)
        else:
            angle = min(angle_re, angle_le)
        # Draw
        if draw:
            cv2.line(img, (x1, y1), (x2, y2), (255, 255, 255), 3)
            cv2.line(img, (x3, y3), (x2, y2), (255, 255, 255), 3)
            cv2.circle(img, (x1, y1), 10, (0, 0, 255), cv2.FILLED)
            cv2.circle(img, (x1, y1), 15, (0, 0, 255), 2)
            cv2.circle(img, (x2, y2), 10, (0, 0, 255), cv2.FILLED)
            cv2.circle(img, (x2, y2), 15, (0, 0, 255), 2)
            cv2.circle(img, (x3, y3), 10, (0, 0, 255), cv2.FILLED)
            cv2.circle(img, (x3, y3), 15, (0, 0, 255), 2)
            cv2.putText(
                img,
                str(int(angle_le)),
                (x2 - 50, y2 + 50),
                cv2.FONT_HERSHEY_PLAIN,
                2,
                (0, 0, 255),
                2,
            )
            cv2.line(img, (x4, y4), (x5, y5), (255, 255, 255), 3)
            cv2.line(img, (x6, y6), (x5, y5), (255, 255, 255), 3)
            cv2.circle(img, (x4, y4), 10, (0, 0, 255), cv2.FILLED)
            cv2.circle(img, (x4, y4), 15, (0, 0, 255), 2)
            cv2.circle(img, (x5, y5), 10, (0, 0, 255), cv2.FILLED)
            cv2.circle(img, (x5, y5), 15, (0, 0, 255), 2)
            cv2.circle(img, (x6, y6), 10, (0, 0, 255), cv2.FILLED)
            cv2.circle(img, (x6, y6), 15, (0, 0, 255), 2)
            cv2.putText(
                img,
                str(int(angle_re)),
                (x2 - 50, y2 + 50),
                cv2.FONT_HERSHEY_PLAIN,
                2,
                (0, 0, 255),
                2,
            )
        return angle

    def findAngle_1(self, img, p1, p2, p3, draw=True):
        # Get the landmarks
        x1, y1 = self.lmList[p1][1:]
        x2, y2 = self.lmList[p2][1:]
        x3, y3 = self.lmList[p3][1:]

        # Calculate the Angle
        angle = math.degrees(
            math.atan2(y3 - y2, x3 - x2) - math.atan2(y1 - y2, x1 - x2))
        if angle < 0:
            angle += 360
        print(angle)

        # Draw
        if draw:
            cv2.line(img, (x1, y1), (x2, y2), (255, 255, 255), 3)
            cv2.line(img, (x3, y3), (x2, y2), (255, 255, 255), 3)
            cv2.circle(img, (x1, y1), 10, (0, 0, 255), cv2.FILLED)
            cv2.circle(img, (x1, y1), 15, (0, 0, 255), 2)
            cv2.circle(img, (x2, y2), 10, (0, 0, 255), cv2.FILLED)
            cv2.circle(img, (x2, y2), 15, (0, 0, 255), 2)
            cv2.circle(img, (x3, y3), 10, (0, 0, 255), cv2.FILLED)
            cv2.circle(img, (x3, y3), 15, (0, 0, 255), 2)
            cv2.putText(
                img,
                str(int(angle)),
                (x2 - 50, y2 + 50),
                cv2.FONT_HERSHEY_PLAIN,
                2,
                (0, 0, 255),
                2,
            )
        return angle


def main():
    cap = cv2.VideoCapture("PoseVideos/1.mp4")
    pTime = 0
    detector = poseDetector()
    while True:
        success, img = cap.read()
        img = detector.findPose(img)
        lmList = detector.findPosition(img, draw=False)
        if len(lmList) != 0:
            print(lmList[14])
            cv2.circle(img, (lmList[14][1], lmList[14][2]), 15, (0, 0, 255),
                       cv2.FILLED)

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(
            img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3,
            (255, 0, 0), 3
        )

        cv2.imshow("Image", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()
