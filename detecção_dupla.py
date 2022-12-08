import json
from tkinter import messagebox
import serial
if __name__ == "__main__":
    esp32 = serial.Serial("COM9", 115200)
def camera_1(video, escala, vizinhos, roi_1, roi_2, roi_3, esp):
    esp32 = esp
    import time
    import cv2
    global muitoscarros
    global muitoscarros2

    contador1 = 0
    contador2 = 0
    contador3 = 0

    muitoscarros = bool
    muitoscarros2 = bool

    cor_roi1 = (107, 60, 1)
    cor_roi2 = (203, 126, 1)

    cap = cv2.VideoCapture(video)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
    haar = cv2.CascadeClassifier("carros_reais_2.xml")

    r_x1, r_y1, r_x2, r_y2 = roi_1
    r1_x1 ,r1_y1, r1_x2, r1_y2 = roi_2
    r2_x1, r2_y1, r2_x2, r2_y2 = roi_3

    while True:
        ret, frame = cap.read()
        if ret == False:
            messagebox.showinfo('Alerta!', f'Camera não encontrada.')
            break
        roi = frame[r_y1:r_y2, r_x1:r_x2]
        roi2 = frame[r1_y1:r1_y2, r1_x1:r1_x2]
        roi3 = frame[r2_y1:r2_y2, r2_x1:r2_x2]

        cv2.putText(frame, f"Cruzamento 1.0", (r_x1, r_y1-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
        cv2.putText(frame, f"Cruzamento 1.0", (r_x1, r_y1-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (207, 0, 255), 1)

        cv2.putText(frame, f"Cruzamento 1.1", (r1_x1, r1_y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
        cv2.putText(frame, f"Cruzamento 1.1", (r1_x1, r1_y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (207, 0, 255), 1)

        cv2.putText(frame, f"Cruzamento 2.0", (r2_x1, r2_y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        cv2.putText(frame, f"Cruzamento 2.0", (r2_x1, r2_y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (46, 46, 46), 1)

        cv2.rectangle(frame, (r_x1, r_y1), (r_x2, r_y2), (cor_roi1), 2)
        cv2.rectangle(frame, (r1_x1, r1_y1), (r1_x2, r1_y2), (cor_roi1), 2)
        cv2.rectangle(frame, (r2_x1, r2_y1), (r2_x2, r2_y2), (cor_roi2), 2)

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
            cv2.rectangle(roi, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.rectangle(roi, (x, y), (x + w, y + h), (0, 0, 255), 1)
            cv2.putText(roi, "carro", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
            cv2.putText(roi, "carro", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
            try:
                contador1 = int(prova.shape[0])
            except AttributeError:
                pass

        for (x, y, w, h) in prova2:
            cv2.rectangle(roi2, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.rectangle(roi2, (x, y), (x + w, y + h), (0, 0, 255), 1)
            cv2.putText(roi2, "carro", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
            cv2.putText(roi2, "carro", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
            try:
                contador2 = int(prova2.shape[0])
            except AttributeError:
                pass

        for (x, y, w, h) in prova3:
            cv2.rectangle(roi3, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.rectangle(roi3, (x, y), (x + w, y + h), (0, 0, 255), 1)
            cv2.putText(roi3, "carro", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
            cv2.putText(roi3, "carro", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
            try:
                contador3 = int(prova3.shape[0])
            except AttributeError:
                pass

        contadorAv1 = contador1 + contador2

        if contadorAv1 >= 4:
             if muitoscarros:
                 esp32.write(b'2')
                 muitoscarros = False

        elif contadorAv1 <=3:
            muitoscarros = True
        else:
            pass

        if contador3 >= 4:
            if muitoscarros2:
                esp32.write(b'3')
                muitoscarros2 = False
        elif contador3 <=3:
            muitoscarros2 = True
        else:
            pass

        total = (contador3) + (contador2) + (contador1)

        fps = f'FPS: {round((1.0 / (end - start)), 2)}'
        cv2.putText(frame, fps, (0, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 4)
        cv2.putText(frame, fps, (0, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (119, 0, 255), 2)

        cv2.putText(frame, f"CRUZAMENTO 1 : {(contador2) + (contador1)}", (1700, 25), cv2.FONT_HERSHEY_SIMPLEX,
                    0.5, (0, 0, 0), 2)
        cv2.putText(frame, f"CRUZAMENTO 1 : {(contador2) + (contador1)}", (1700, 25), cv2.FONT_HERSHEY_SIMPLEX,
                    0.5, (0, 255, 0), 1)

        cv2.putText(frame, f"CRUZAMENTO 2 : {(contador3)}", (1700, 45), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
        cv2.putText(frame, f"CRUZAMENTO 2 : {(contador3)}", (1700, 45), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0),
                    1)


        if total >= 5:
            cv2.putText(frame, f"TOTAL : {(contador3) + (contador2) + (contador1)}", (1700, 65),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
            cv2.putText(frame, f"TOTAL : {(contador3) + (contador2) + (contador1)}", (1700, 65),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
        elif total <= 4:
            cv2.putText(frame, f"TOTAL : {(contador3) + (contador2) + (contador1)}", (1700, 65),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
            cv2.putText(frame, f"TOTAL : {(contador3) + (contador2) + (contador1)}", (1700, 65),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

        cv2.imshow("Camera 1", frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

    if __name__ == "__main__":
        cap.release()
        cv2.destroyAllWindows()
    elif __name__ != "__main__":
        try:
            cap.release()
            cv2.destroyWindow("Camera 1")
        except cv2.error:
            pass

def camera_2(video, escala, vizinhos, roi_1, roi_2, roi_3, esp):
    import cv2
    import time
    esp32 = esp

    global muitoscarros_1
    global muitoscarros2_1

    contador1_1 = 0
    contador2_1 = 0
    contador3_1 = 0

    muitoscarros_1 = bool
    muitoscarros2_1 = bool

    cor_roi1 = (107, 60, 1)
    cor_roi2 = (203, 126, 1)

    cap = cv2.VideoCapture(video)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
    haar = cv2.CascadeClassifier("carros_reais_2.xml")

    r_x1, r_y1, r_x2, r_y2 = roi_1
    r1_x1, r1_y1, r1_x2, r1_y2 = roi_2
    r2_x1, r2_y1, r2_x2, r2_y2 = roi_3

    while True:
        ret, frame2 = cap.read()
        if ret == False:
            messagebox.showinfo('Alerta!', f'Camera não encontrada.')
            break

        roi = frame2[r_y1:r_y2, r_x1:r_x2]
        roi2 = frame2[r1_y1:r1_y2, r1_x1:r1_x2]
        roi3 = frame2[r2_y1:r2_y2, r2_x1:r2_x2]

        cv2.putText(frame2, f"Cruzamento 1.0", (r_x1, r_y1-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
        cv2.putText(frame2, f"Cruzamento 1.0", (r_x1, r_y1-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (207, 0, 255), 1)

        cv2.putText(frame2, f"Cruzamento 1.1", (r1_x1, r1_y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
        cv2.putText(frame2, f"Cruzamento 1.1", (r1_x1, r1_y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (207, 0, 255), 1)

        cv2.putText(frame2, f"Cruzamento 2.0", (r2_x1, r2_y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        cv2.putText(frame2, f"Cruzamento 2.0", (r2_x1, r2_y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (46, 46, 46), 1)

        cv2.rectangle(frame2, (r_x1, r_y1), (r_x2, r_y2), (cor_roi1), 2)
        cv2.rectangle(frame2, (r1_x1, r1_y1), (r1_x2, r1_y2), (cor_roi1), 2)
        cv2.rectangle(frame2, (r2_x1, r2_y1), (r2_x2, r2_y2), (cor_roi2), 2)

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
            cv2.rectangle(roi, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.rectangle(roi, (x, y), (x + w, y + h), (0, 0, 255), 1)
            cv2.putText(roi, "carro", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
            cv2.putText(roi, "carro", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
            try:
                contador1_1 = int(prova.shape[0])
            except AttributeError:
                pass

        for (x, y, w, h) in prova2:
            cv2.rectangle(roi2, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.rectangle(roi2, (x, y), (x + w, y + h), (0, 0, 255), 1)
            cv2.putText(roi2, "carro", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
            cv2.putText(roi2, "carro", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
            try:
                contador2_1 = int(prova2.shape[0])
            except AttributeError:
                pass

        for (x, y, w, h) in prova3:
            cv2.rectangle(roi3, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.rectangle(roi3, (x, y), (x + w, y + h), (0, 0, 255), 1)
            cv2.putText(roi3, "carro", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
            cv2.putText(roi3, "carro", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
            try:
                contador3_1 = int(prova3.shape[0])
            except AttributeError:
                pass

        contadorAv2 = contador1_1 + contador2_1

        if contadorAv2 >= 4:
            if muitoscarros_1:
                esp32.write(b'2')
                muitoscarros_1 = False

        elif contadorAv2 <= 3:
            muitoscarros_1 = True
        else:
            pass
        if contador3_1 >= 4:
            if muitoscarros2_1:
                esp32.write(b'3')
                #muitoscarros2_1 = False
        elif contador3_1 <= 3:
            muitoscarros2_1 = True
        else:
            pass

        total_1 = (contador3_1) + (contador2_1) + (contador1_1)

        fps = f'FPS: {round((1.0 / (end - start)), 2)}'
        cv2.putText(frame2, fps, (0, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 4)
        cv2.putText(frame2, fps, (0, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (119, 0, 255), 2)

        cv2.putText(frame2, f"CRUZAMENTO 1 : {(contador2_1) + (contador1_1)}", (1700, 25), cv2.FONT_HERSHEY_SIMPLEX,
                    0.5, (0, 0, 0), 2)
        cv2.putText(frame2, f"CRUZAMENTO 1 : {(contador2_1) + (contador1_1)}", (1700, 25), cv2.FONT_HERSHEY_SIMPLEX,
                    0.5, (0, 255, 0), 1)

        cv2.putText(frame2, f"CRUZAMENTO 2 : {(contador3_1)}", (1700, 45), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
        cv2.putText(frame2, f"CRUZAMENTO 2 : {(contador3_1)}", (1700, 45), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0),
                    1)


        if total_1 >= 5:
            cv2.putText(frame2, f"TOTAL : {(contador3_1) + (contador2_1) + (contador1_1)}", (1700, 65),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
            cv2.putText(frame2, f"TOTAL : {(contador3_1) + (contador2_1) + (contador1_1)}", (1700, 65),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
        elif total_1 <= 4:
            cv2.putText(frame2, f"TOTAL : {(contador3_1) + (contador2_1) + (contador1_1)}", (1700, 65),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
            cv2.putText(frame2, f"TOTAL : {(contador3_1) + (contador2_1) + (contador1_1)}", (1700, 65),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

        cv2.imshow("Camera 2", frame2)

        if cv2.waitKey(1) & 0xFF == 27:
            break

    if __name__ == "__main__":
        cap.release()
        cv2.destroyAllWindows()
    elif __name__ != "__main__":
        try:
            cap.release()
            cv2.destroyWindow("Camera 2")
        except cv2.error:
            pass


if __name__ == "__main__":
    with open("Pastabanco/Scale", "r") as file:
        Scale_value = file.read()
        Scale_value = json.loads(Scale_value)
        file.close()

    escala = Scale_value['escala']
    vizinho = Scale_value['vizinhos']

    camera_1("road.mp4", escala, vizinho, (10, 10, 20, 20), (100, 200, 200, 300),(100, 300, 1200, 700), esp32)



