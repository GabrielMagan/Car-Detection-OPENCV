# -----------------------------------------------
#  Arquivo   : yolo_com_roi.py
#  Nome      : Yolo custom
#  Autor     : Gabriel Monteiro Magan
#  E-mail    : gabrielmagan2@gmail.com
#  Data      : 10/10/2022
#  Versão    : 1
# -----------------------------------------------
import json
import serial
if __name__ == "__main__":
    esp32 = serial.Serial("COM1", 115200)
def cam_yolo(video, cor1, cor2, roi_1, roi_2, roi_3, esp, condicao):
    import cv2
    import time
    esp32 = esp

    global muitoscarros
    global muitoscarros2

    muitoscarros = bool
    muitoscarros2 = bool

    cor_roi1 = (cor1[0], cor1[1], cor1[2])
    cor_roi2 = (cor2[0], cor2[1], cor2[2])
    carros = []
    carros2 = []
    carros3 = []
    CORES = [(0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255)]

    with open('nomes/classes.txt', 'r') as f:
        class_name = [cname.strip() for cname in f.readlines()]

    r_x1, r_y1, r_x2, r_y2 = roi_1
    r1_x1, r1_y1, r1_x2, r1_y2 = roi_2
    r2_x1, r2_y1, r2_x2, r2_y2 = roi_3
    cap = cv2.VideoCapture(video)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
    net = cv2.dnn.readNet('yolov4-tiny.weights', 'yolov4-tiny.cfg')
    model = cv2.dnn_DetectionModel(net)
    model.setInputParams(size=(416, 416), scale=1 / 255)

    while True:
        _, frame = cap.read()
        roi = frame[r_y1:r_y2, r_x1:r_x2]
        roi2 = frame[r1_y1:r1_y2, r1_x1:r1_x2]
        roi3 = frame[r2_y1:r2_y2, r2_x1:r2_x2]
        cv2.rectangle(frame, (r1_x1, r1_y1), (r1_x2, r1_y2), (cor_roi1), 2)
        cv2.rectangle(frame, (r_x1, r_y1), (r_x2, r_y2), (cor_roi1), 2)
        cv2.rectangle(frame, (r2_x1, r2_y1), (r2_x2, r2_y2), (cor_roi2), 2)

        cv2.putText(frame, f"Cruzamento 1.0", (r_x1, r_y1-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
        cv2.putText(frame, f"Cruzamento 1.0", (r_x1, r_y1-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (207, 0, 255), 1)

        cv2.putText(frame, f"Cruzamento 1.1", (r1_x1, r1_y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
        cv2.putText(frame, f"Cruzamento 1.1", (r1_x1, r1_y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (207, 0, 255), 1)

        cv2.putText(frame, f"Cruzamento 2.0", (r2_x1, r2_y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        cv2.putText(frame, f"Cruzamento 2.0", (r2_x1, r2_y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (46, 46, 46), 1)

        start = time.time()
        classes, scores, boxes = model.detect(roi, 0.1, 0.2)  #0.1 , 0.2
        classes1, scores1, boxes1 = model.detect(roi2, 0.1, 0.2)
        classes2, scores2, boxes2 = model.detect(roi3, 0.1, 0.2)
        end = time.time()
        carros.clear()
        carros2.clear()
        carros3.clear()

        for (classid, score, box) in zip(classes, scores, boxes):
            color = CORES[int(classid) % len(CORES)]
            label = f"{class_name[classid]} : {score * 100:,.2f}%"
            cv2.rectangle(roi, box, (0, 0, 0), 2)
            cv2.rectangle(roi, box, color, 1)
            cv2.putText(roi, label, (box[0], box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
            cv2.putText(roi, label, (box[0], box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)
            carros.append(classid)

        for (classid, score, box) in zip(classes1, scores1, boxes1):
            color = CORES[int(classid) % len(CORES)]
            label = f"{class_name[classid]} : {score * 100:,.2f}%"
            cv2.rectangle(roi2, box, (0, 0, 0), 2)
            cv2.rectangle(roi2, box, color, 1)
            cv2.putText(roi2, label, (box[0], box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
            cv2.putText(roi2, label, (box[0], box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)
            carros2.append(classid)

        for (classid, score, box) in zip(classes2, scores2, boxes2):
            color = CORES[int(classid) % len(CORES)]
            label = f"{class_name[classid]} : {score * 100:,.2f}%"
            cv2.rectangle(roi3, box, (0, 0, 0), 2)
            cv2.rectangle(roi3, box, color, 1)
            cv2.putText(roi3, label, (box[0], box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
            cv2.putText(roi3, label, (box[0], box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)
            carros3.append(classid)
        fps = f'FPS: {round((1.0 / (end - start)), 2)}'

        cv2.putText(frame, fps, (0, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 4)
        cv2.putText(frame, fps, (0, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (119, 0, 255), 2)
        total = (len(carros3))+(len(carros2))+(len(carros))

        if not condicao:
            if (len(carros2) + len(carros)) >= 4:
                if muitoscarros:
                    print("3 enviado")
                    esp32.write(b'3')
                    muitoscarros = False
            elif (len(carros2) + len(carros)) <= 3:
                muitoscarros = True
            else:
                pass
            if len(carros3) >= 4:
                if muitoscarros2:
                    print("2 enviado")
                    esp32.write(b'2')
                    muitoscarros2 = False
            elif len(carros3) <= 3:
                muitoscarros2 = True
            else:
                pass
        elif condicao:
            if (len(carros2) + len(carros)) >= 4:
                if muitoscarros:
                    print("5 enviado")
                    esp32.write(b'5')
                    muitoscarros = False
            elif (len(carros2) + len(carros)) <= 3:
                muitoscarros = True
            else:
                pass
            if len(carros3) >= 4:
                if muitoscarros2:
                    print("4 enviado")
                    esp32.write(b'4')
                    muitoscarros2 = False
            elif len(carros3) <= 3:
                muitoscarros2 = True
            else:
                pass
        else:
            pass

        cv2.putText(frame, f"CRUZAMENTO 1 : {(len(carros2)) + (len(carros))}", (1700, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
        cv2.putText(frame, f"CRUZAMENTO 1 : {(len(carros2)) + (len(carros))}", (1700, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

        cv2.putText(frame, f"CRUZAMENTO 2 : {(len(carros3))}", (1700, 45), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
        cv2.putText(frame, f"CRUZAMENTO 2 : {(len(carros3))}", (1700, 45), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

        if total >= 4:
            cv2.putText(frame, f"TOTAL : {(len(carros3))+(len(carros2))+(len(carros))}", (1700, 65), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
            cv2.putText(frame, f"TOTAL : {(len(carros3))+(len(carros2))+(len(carros))}", (1700, 65), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
        elif total <= 3:
            cv2.putText(frame, f"TOTAL : {(len(carros3)) + (len(carros2)) + (len(carros))}", (1700, 65), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
            cv2.putText(frame, f"TOTAL : {(len(carros3)) + (len(carros2)) + (len(carros))}", (1700, 65), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

        cv2.imshow("Resultado", frame)

        if cv2.waitKey(1) == 27:
            break

    if __name__ == "__main__":
        cap.release()
        cv2.destroyAllWindows()
    elif __name__ != "__main__":
        try:
            cap.release()
            cv2.destroyWindow("Resultado")
        except cv2.error:
            pass

if __name__ == "__main__":
    with open("Pastabanco/Scale", "r") as file:
        Scale_value = file.read()
        Scale_value = json.loads(Scale_value)
        file.close()

    escala = Scale_value['escala']
    vizinho = Scale_value['vizinhos']

    with open("Pastabanco/cores", "r") as file:
        Scale_value = file.read()
        Scale_value = json.loads(Scale_value)
        file.close()

    cor1 = Scale_value['ROI1']
    cor2 = Scale_value['ROI2']

    cam_yolo(1,(cor1[0],cor1[1],cor1[2]),(cor2[0],cor2[1],cor2[2]), (537, 14, 880, 193), (1043, 601, 1386, 1066), (21, 205, 506, 489),esp32,False )



