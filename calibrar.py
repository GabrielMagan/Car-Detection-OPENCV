def calibrar_webcam(video, roi_1, roi_2, roi_3):
    import json
    import time
    from tkinter import messagebox
    def nada(x):
        pass

    with open("Pastabanco/Scale", "r") as file:
        Scale_value = file.read()
        Scale_value = json.loads(Scale_value)
        file.close()

    x = Scale_value['escala']
    y = Scale_value['vizinhos']
    x = (x*1000)-1000

    import cv2
    frameWidth = 640
    frameHeight = 360

    cv2.namedWindow("Resultado")
    cv2.resizeWindow("Resultado", frameWidth, frameHeight)
    cv2.createTrackbar("escala", "Resultado", int(x), 100, nada)
    cv2.createTrackbar("vizinhos", "Resultado", y, 100, nada)

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

        escalaValor = 1 + (cv2.getTrackbarPos("escala", "Resultado") / 1000)
        neig = cv2.getTrackbarPos("vizinhos", "Resultado")

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

        gray1 = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        gray2 = cv2.cvtColor(roi2, cv2.COLOR_BGR2GRAY)
        gray3 = cv2.cvtColor(roi3, cv2.COLOR_BGR2GRAY)

        start = time.time()
        prova = haar.detectMultiScale(gray1, scaleFactor=escalaValor, minNeighbors=neig)
        prova2 = haar.detectMultiScale(gray2, scaleFactor=escalaValor, minNeighbors=neig)
        prova3 = haar.detectMultiScale(gray3, scaleFactor=escalaValor, minNeighbors=neig)
        end = time.time()

        for (x, y, w, h) in prova:
            cv2.rectangle(roi, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.rectangle(roi, (x, y), (x + w, y + h), (0, 0, 0), 2)
            cv2.rectangle(roi, (x, y), (x + w, y + h), (0, 0, 255), 1)
            cv2.putText(roi, "carro", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
            cv2.putText(roi, "carro", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)

        for (x, y, w, h) in prova2:
            cv2.rectangle(roi2, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.rectangle(roi2, (x, y), (x + w, y + h), (0, 0, 0), 2)
            cv2.rectangle(roi2, (x, y), (x + w, y + h), (0, 0, 255), 1)
            cv2.putText(roi2, "carro", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
            cv2.putText(roi2, "carro", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)

        for (x, y, w, h) in prova3:
            cv2.rectangle(roi3, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.rectangle(roi3, (x, y), (x + w, y + h), (0, 0, 0), 2)
            cv2.rectangle(roi3, (x, y), (x + w, y + h), (0, 0, 255), 1)
            cv2.putText(roi3, "carro", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
            cv2.putText(roi3, "carro", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)

        fps = f'FPS: {round((1.0 / (end - start)), 2)}'

        cv2.putText(frame, fps, (0, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 4)
        cv2.putText(frame, fps, (0, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (119, 0, 255), 2)

        cv2.imshow("Resultado", frame)

        if cv2.waitKey(1) & 0xFF == 27:
            valor_da_escala = escalaValor
            valor_dos_vizinhos = neig
            valores = {"escala": valor_da_escala, "vizinhos": valor_dos_vizinhos}

            valores = json.dumps(valores)

            with open("Pastabanco/Scale", "w+") as file:
                file.write(valores)
                file.close()
            break

    if __name__ == "__main__":
        cap.release()
        cv2.destroyAllWindows()

    elif __name__ != "__main__":
        cap.release()
        cv2.destroyWindow("Resultado")

if __name__ == "__main__":
    calibrar_webcam("road.mp4",(50,400,550,700), (700,400,1200,700),(750,200,1000,390))


