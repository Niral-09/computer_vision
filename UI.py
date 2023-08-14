import flet as ft
import cv2
import numpy as np
import time
import posemodule as pm


def main(page: ft.Page):
    def button_clicked(e):
        print(exercise_dropdown.value)
        if exercise_dropdown.value == "Right Hand Moves":
            cap = cv2.VideoCapture(0)
            detector = pm.poseDetector()
            count = 0
            dir = 0
            pTime = 0
            while True:
                success, img = cap.read()
                img = cv2.resize(img, (1280, 720))
                # img = cv2.imread("AiTrainer/test.jpg")
                img = detector.findPose(img, False)
                lmList = detector.findPosition(img, False)
                # print(lmList)
                if len(lmList) != 0:
                    # Right Arm
                    angle = detector.findAngle_1(img, 12, 14, 16)
                    # # Left Arm
                    # angle = detector.findAngle(img, 11, 13, 15,False)
                    per = np.interp(angle, (210, 310), (0, 100))
                    bar = np.interp(angle, (220, 310), (650, 100))
                    # print(angle, per)
                    # Check for the dumbbell curls
                    color = (255, 0, 255)
                    if per == 100:
                        color = (0, 255, 0)
                        if dir == 0:
                            count += 0.5
                            dir = 1
                    if per == 0:
                        color = (0, 255, 0)
                        if dir == 1:
                            count += 0.5
                            dir = 0
                    # print(count)
                    # Draw Bar
                    cv2.rectangle(img, (1100, 100), (1175, 650), color, 3)
                    cv2.rectangle(img, (1100, int(bar)), (1175, 650), color,
                                  cv2.FILLED)
                    cv2.putText(
                        img, f"{int(per)} %", (1100, 75),
                        cv2.FONT_HERSHEY_PLAIN, 4, color,
                        4
                    )
                    # Draw Curl Count
                    cv2.rectangle(img, (0, 450), (250, 720), (0, 255, 0),
                                  cv2.FILLED)
                    cv2.putText(
                        img, str(int(count)), (45, 670),
                        cv2.FONT_HERSHEY_PLAIN, 15,
                        (255, 0, 0), 25
                    )

                cTime = time.time()
                fps = 1 / (cTime - pTime)
                pTime = cTime
                cv2.putText(
                    img, str(int(fps)), (50, 100), cv2.FONT_HERSHEY_PLAIN, 5,
                    (255, 0, 0), 5
                )
                cv2.imshow("Image", img)
                cv2.waitKey(1)

        if exercise_dropdown.value == "Adjustable Moves (Both Hands)":
            cap = cv2.VideoCapture(0)
            detector = pm.poseDetector()
            count = 0
            dir = 0
            pTime = 0
            while True:
                success, img = cap.read()
                img = cv2.resize(img, (1280, 720))
                # img = cv2.imread("AiTrainer/test.jpg")
                img = detector.findPose(img, False)
                lmList = detector.findPosition(img, False)
                # print(lmList)
                if len(lmList) != 0:
                    # Right Arm
                    angle = detector.findAngle(img, 11, 13, 15, 12, 14, 16)
                    # # Left Arm
                    # angle = detector.findAngle(img, 11, 13, 15,False)
                    per = np.interp(angle, (210, 310), (0, 100))
                    bar = np.interp(angle, (220, 310), (650, 100))
                    # print(angle, per)
                    # Check for the dumbbell curls
                    color = (255, 0, 255)
                    if per == 100:
                        color = (0, 255, 0)
                        if dir == 0:
                            count += 0.5
                            dir = 1
                    if per == 0:
                        color = (0, 255, 0)
                        if dir == 1:
                            count += 0.5
                            dir = 0
                    print(count)
                    # Draw Bar
                    cv2.rectangle(img, (1100, 100), (1175, 650), color, 3)
                    cv2.rectangle(img, (1100, int(bar)), (1175, 650), color,
                                  cv2.FILLED)
                    cv2.putText(
                        img, f"{int(per)} %", (1100, 75),
                        cv2.FONT_HERSHEY_PLAIN, 4, color,
                        4
                    )
                    # Draw Curl Count
                    cv2.rectangle(img, (0, 450), (250, 720), (0, 255, 0),
                                  cv2.FILLED)
                    cv2.putText(
                        img, str(int(count)), (45, 670),
                        cv2.FONT_HERSHEY_PLAIN, 15,
                        (255, 0, 0), 25
                    )

                cTime = time.time()
                fps = 1 / (cTime - pTime)
                pTime = cTime
                cv2.putText(
                    img, str(int(fps)), (50, 100), cv2.FONT_HERSHEY_PLAIN, 5,
                    (255, 0, 0), 5
                )
                cv2.imshow("Image", img)
                cv2.waitKey(1)

        else:
            # print("inside")
            cap = cv2.VideoCapture(0)
            detector = pm.poseDetector()
            count = 0
            dir = 0
            pTime = 0
            while True:
                success, img = cap.read()
                img = cv2.resize(img, (1280, 720))
                # img = cv2.imread("AiTrainer/test.jpg")
                img = detector.findPose(img, False)
                lmList = detector.findPosition(img, False)
                # print(lmList)
                if len(lmList) != 0:
                    # Right Arm
                    angle = detector.findAngle_1(img, 11, 13, 15)
                    # # Left Arm
                    # angle = detector.findAngle(img, 11, 13, 15,False)
                    per = np.interp(angle, (210, 310), (0, 100))
                    bar = np.interp(angle, (220, 310), (650, 100))
                    # print(angle, per)
                    # Check for the dumbbell curls
                    color = (255, 0, 255)
                    if per == 100:
                        color = (0, 255, 0)
                        if dir == 0:
                            count += 0.5
                            dir = 1
                    if per == 0:
                        color = (0, 255, 0)
                        if dir == 1:
                            count += 0.5
                            dir = 0
                    # print(count)
                    # Draw Bar
                    cv2.rectangle(img, (1100, 100), (1175, 650), color, 3)
                    cv2.rectangle(img, (1100, int(bar)), (1175, 650), color,
                                  cv2.FILLED)
                    cv2.putText(
                        img, f"{int(per)} %", (1100, 75),
                        cv2.FONT_HERSHEY_PLAIN, 4, color,
                        4
                    )
                    # Draw Curl Count
                    cv2.rectangle(img, (0, 450), (250, 720), (0, 255, 0),
                                  cv2.FILLED)
                    cv2.putText(
                        img, str(int(count)), (45, 670),
                        cv2.FONT_HERSHEY_PLAIN, 15,
                        (255, 0, 0), 25
                    )

                cTime = time.time()
                fps = 1 / (cTime - pTime)
                pTime = cTime
                cv2.putText(
                    img, str(int(fps)), (50, 100), cv2.FONT_HERSHEY_PLAIN, 5,
                    (255, 0, 0), 5
                )
                cv2.imshow("Image", img)
                cv2.waitKey(1)
        page.update()

    output_text = ft.Text()
    title = ft.Text(
                "Choose Moves", size=50,
                weight="w300"
            )
    submit_btn = ft.ElevatedButton(text="Submit", on_click=button_clicked)
    exercise_dropdown = ft.Dropdown(
        width=500,
        options=[
            ft.dropdown.Option("Right Hand Moves"),
            ft.dropdown.Option("Left Hand Moves"),
            ft.dropdown.Option("Adjustable Moves (Both Hands)"),
        ],
        autofocus=True
    )
    page.add(title, exercise_dropdown, submit_btn, output_text)


ft.app(target=main)  # , view=ft.WEB_BROWSER)
