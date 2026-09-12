import math, cv2, mediapipe as mp

cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

p = [0 for x in range(21)]
finger = [0 for x in range(5)]
while True:
    frame = cap.read()[1]

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands.process(rgb)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(frame, handLms, mpHands.HAND_CONNECTIONS)
            ladon1 = handLms.landmark[5]
            finger1 = handLms.landmark[8]
            rast1 = math.sqrt((finger1.x-ladon1.x)**2 + (finger1.y-ladon1.y)**2)
            first_finger = 0
            print("Первый палец растояние: ", rast1)
            # print(rast1)
            if rast1 < 0.1 :
                first_finger = 0
            elif rast1 > 0.15 :
                first_finger = 1
            print(first_finger)
            ladon2 = handLms.landmark[9]
            finger2 = handLms.landmark[12]
            rast2 = math.sqrt((finger2.x - ladon2.x) ** 2 + (finger2.y - ladon2.y) ** 2)
            second_finger = 0
            print("Второй палец растояние: ", rast2)
            if rast2 < 0.1:
                second_finger = 0
            elif rast2 > 0.17:
                second_finger = 1
            print(second_finger)
            ladon3 = handLms.landmark[13]
            finger3 = handLms.landmark[16]
            rast3 = math.sqrt((finger3.x - ladon3.x) ** 2 + (finger3.y - ladon3.y) ** 2)
            third_finger = 0
            print("Третий палец растояние: ", rast3)
            if rast3 < 0.1:
                third_finger = 0
            elif rast3 > 0.15:
                third_finger = 1
            print(third_finger)
            ladon4 = handLms.landmark[17]
            finger4 = handLms.landmark[20]
            rast4 = math.sqrt((finger4.x - ladon4.x) ** 2 + (finger4.y - ladon4.y) ** 2)
            fourth_finger = 0
            print("Чертвёртый палец растояние: ", rast4)
            if rast4 < 0.1:
                fourth_finger = 0
            elif rast4 > 0.15:
                fourth_finger = 1
            print(fourth_finger)
            ladon5 = handLms.landmark[1]
            finger5 = handLms.landmark[4]
            rast5 = math.sqrt((finger5.x - ladon5.x) ** 2 + (finger5.y - ladon5.y) ** 2)
            fifth_finger = 0
            print("Пятый палец растояние: ", rast5)
            if rast5 < 0.17:
                fifth_finger = 0
            elif rast5 > 0.2:
                fifth_finger = 1
            print(fifth_finger)

            total_finger = first_finger + second_finger + third_finger + fourth_finger + fifth_finger
            cv2.putText(frame,str(total_finger), (100,100), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    cv2.imshow("Frame", frame)
    cv2.waitKey(1)
