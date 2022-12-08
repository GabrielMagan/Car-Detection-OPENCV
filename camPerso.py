import json
from tkinter import messagebox
def Cam_rois(video, cor1, cor2, escala, vizinhos, roi_1, roi_2, roi_3):
    import cv2
    import time
    cor_roi1 = (cor1[0], cor1[1], cor1[2])
    cor_roi2 = (cor2[0], cor2[1], cor2[2])


    cap = cv2.VideoCapture(video)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
    haar = cv2.CascadeClassifier("carros_reais_2.xml")

    r_x1, r_y1, r_x2, r_y2 = roi_1
    r1_x1, r1_y1, r1_x2, r1_y2 = roi_2
    r2_x1, r2_y1, r2_x2, r2_y2 = roi_3

    while True:
        carros = 0
        carros2 = 0
        carros3 = 0
        ret, frame = cap.read()
        if ret == False:
            messagebox.showinfo('Alerta!', f'Camera não encontrada.')
            break

        roi = frame[r_y1:r_y2, r_x1:r_x2]
        roi2 = frame[r1_y1:r1_y2, r1_x1:r1_x2]
        roi3 = frame[r2_y1:r2_y2, r2_x1:r2_x2]

        cv2.rectangle(frame, (r_x1, r_y1), (r_x2, r_y2), (cor_roi1), 2)
        cv2.rectangle(frame, (r1_x1, r1_y1), (r1_x2, r1_y2), (cor_roi1), 2)
        cv2.rectangle(frame, (r2_x1, r2_y1), (r2_x2, r2_y2), (cor_roi2), 2)

        cv2.putText(frame, f"Cruzamento 1.0", (r_x1, r_y1-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
        cv2.putText(frame, f"Cruzamento 1.0", (r_x1, r_y1-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (207, 0, 255), 1)

        cv2.putText(frame, f"Cruzamento 1.1", (r1_x1, r1_y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
        cv2.putText(frame, f"Cruzamento 1.1", (r1_x1, r1_y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (207, 0, 255), 1)

        cv2.putText(frame, f"Cruzamento 2.0", (r2_x1, r2_y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        cv2.putText(frame, f"Cruzamento 2.0", (r2_x1, r2_y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (46, 46, 46), 1)

        try:
            gray1 = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        except cv2.error:
            messagebox.showinfo('Alerta!', f'Não foi possivel criar o Roi 1.')
            break

        try:
            gray2 = cv2.cvtColor(roi2, cv2.COLOR_BGR2GRAY)
        except cv2.error:
            messagebox.showinfo('Alerta!', f'Não foi possivel criar o Roi 2.')
            break
        try:
            gray3 = cv2.cvtColor(roi3, cv2.COLOR_BGR2GRAY)
        except cv2.error:
            messagebox.showinfo('Alerta!', f'Não foi possivel criar o Roi 3.')
            break

        start = time.time()
        prova = haar.detectMultiScale(gray1, scaleFactor=escala, minNeighbors=vizinhos)
        prova2 = haar.detectMultiScale(gray2, scaleFactor=escala, minNeighbors=vizinhos)
        prova3 = haar.detectMultiScale(gray3, scaleFactor=escala, minNeighbors=vizinhos)
        end = time.time()

        for (x, y, w, h) in prova:
            cv2.rectangle(roi, (x, y),  (x + w, y + h),(0, 0, 0), 2)
            cv2.rectangle(roi, (x, y), (x + w, y + h), (0, 0, 255), 1)
            cv2.putText(roi, "carro", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
            cv2.putText(roi, "carro", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 1)
            try:
                carros = int(prova.shape[0])
            except AttributeError:
                pass

        for (x, y, w, h) in prova2:
            cv2.rectangle(roi2, (x, y),  (x + w, y + h),(0, 0, 0), 2)
            cv2.rectangle(roi2, (x, y), (x + w, y + h), (0, 0, 255), 1)
            cv2.putText(roi2, "carro", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
            cv2.putText(roi2, "carro", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
            try:
                carros2 = int(prova.shape[0])
            except AttributeError:
                pass

        for (x, y, w, h) in prova3:
            cv2.rectangle(roi3, (x,y),  (x + w, y + h),(0, 0, 0), 2)
            cv2.rectangle(roi3, (x, y), (x + w, y + h), (0, 0, 255), 1)
            cv2.putText(roi3, "carro", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
            cv2.putText(roi3, "carro", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
            try:
                carros3 = int(prova.shape[0])
            except AttributeError:
                pass

        fps = f'FPS: {round((1.0 / (end - start)), 2)}'
        print(carros2)

        cv2.putText(frame, fps, (0, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 4)
        cv2.putText(frame, fps, (0, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (119, 0, 255), 2)
        total = (carros3) + (carros2) + (carros)

        cv2.putText(frame, f"CRUZAMENTO 1 : {(carros2) + (carros)}", (1700, 25), cv2.FONT_HERSHEY_SIMPLEX,
                    0.5, (0, 0, 0), 2)
        cv2.putText(frame, f"CRUZAMENTO 1 : {(carros2) + (carros)}", (1700, 25), cv2.FONT_HERSHEY_SIMPLEX,
                    0.5, (0, 255, 0), 1)

        cv2.putText(frame, f"CRUZAMENTO 2 : {(carros3)}", (1700, 45), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
        cv2.putText(frame, f"CRUZAMENTO 2 : {(carros3)}", (1700, 45), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0),
                    1)

        if total >= 5:
            cv2.putText(frame, f"TOTAL : {(carros3) + (carros2) + (carros)}", (1700, 65),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
            cv2.putText(frame, f"TOTAL : {(carros3) + (carros2) + (carros)}", (1700, 65),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
        elif total <= 4:
            cv2.putText(frame, f"TOTAL : {(carros3) + (carros2) + (carros)}", (1700, 65),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
            cv2.putText(frame, f"TOTAL : {(carros3) + (carros2) + (carros)}", (1700, 65),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

        cv2.imshow("Resultado", frame)

        if cv2.waitKey(1) & 0xFF == 27:
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

    Cam_rois(0,(cor1[0],cor1[1],cor1[2]),(cor2[0],cor2[1],cor2[2]), escala, vizinho, (50, 400, 550, 700), (700, 400, 1200, 700), (100, 200, 200, 300))



