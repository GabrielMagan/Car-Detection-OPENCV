from tkinter import messagebox
import json
def roi_variable(video, cond):
    import cv2

    cor_roi1 = (0,255,0)
    def nada(x):
        pass

    cap = cv2.VideoCapture(video)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

    frameWidth = 700
    frameHeight = 200
    x1 = 400
    x2 = 400
    y1 = 700
    y2 = 700

    cv2.namedWindow("Resultado")
    cv2.resizeWindow("Resultado", frameWidth, frameHeight)
    cv2.createTrackbar("x1", "Resultado", x1, 1920, nada)
    cv2.createTrackbar("y1", "Resultado", x2, 1080, nada)
    cv2.createTrackbar("x2", "Resultado", y1, 1920, nada)
    cv2.createTrackbar("y2", "Resultado", y2, 1080, nada)

    while True:
        r_x1 = cv2.getTrackbarPos("x1", "Resultado")
        r_y1 = cv2.getTrackbarPos("y1", "Resultado")
        r_x2 = cv2.getTrackbarPos("x2", "Resultado")
        r_y2 = cv2.getTrackbarPos("y2", "Resultado")
        ret, frame = cap.read()
        if ret == False:
            messagebox.showinfo('Alerta!', f'Camera não encontrada.')
            break

        cv2.rectangle(frame, (r_x1, r_y1), (r_x2, r_y2), (0,0,0), 3)
        cv2.rectangle(frame, (r_x1, r_y1), (r_x2, r_y2), (cor_roi1), 2)
        cv2.circle(frame, (r_x1, r_y1), 5, (0, 0, 0), 12, 0)
        cv2.circle(frame, (r_x1, r_y1), 5, (0,0,255),10,0)
        cv2.putText(frame, f"(x1, y1)", (r_x1 - 110, r_y1 - 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 4)
        cv2.putText(frame, f"(x1, y1)", (r_x1 - 110, r_y1 - 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.circle(frame, (r_x2, r_y2), 5, (0, 0, 0), 12, 0)
        cv2.circle(frame, (r_x2, r_y2), 5, (0, 0, 255), 10, 0)
        cv2.putText(frame, f"(x2, y2)", (r_x2-15, r_y2 + 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 4)
        cv2.putText(frame, f"(x2, y2)", (r_x2 -15, r_y2 + 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        b = cv2.resize(frame, (1280, 720))
        cv2.resizeWindow("Resultado", 1280, 720)
        cv2.imshow("Resultado", b)

        if cond == True:
            # --------------------------------------------- roi 1 ------------------------------------------
            if cv2.waitKey(1) == 49:
                messagebox.showinfo('Informação!', f'Posição 1 salva')
                with open("Pastabanco/roi1", "r") as file:
                    roi_value1 = file.read()
                    roi_value1 = json.loads(roi_value1)

                roi_value1["x1"] = r_x1
                roi_value1["y1"] = r_y1
                roi_value1["x2"] = r_x2
                roi_value1["y2"] = r_y2

                roi_value1 = json.dumps(roi_value1)

                with open("Pastabanco/roi1", "w+") as file:
                    file.write(roi_value1)
                    file.close()
             # --------------------------------------------- roi 2 ------------------------------------------
            elif cv2.waitKey(1) == 50:
                messagebox.showinfo('Informação!', f'Posição 2 salva')
                with open("Pastabanco/roi2", "r") as file:
                    roi_value2 = file.read()
                    roi_value2 = json.loads(roi_value2)

                roi_value2["x1"] = r_x1
                roi_value2["y1"] = r_y1
                roi_value2["x2"] = r_x2
                roi_value2["y2"] = r_y2

                roi_value2 = json.dumps(roi_value2)

                with open("Pastabanco/roi2", "w+") as file:
                    file.write(roi_value2)
                    file.close()
             # --------------------------------------------- roi 3 ------------------------------------------
            elif cv2.waitKey(1) == 51:
                messagebox.showinfo('Informação!', f'Posição 3 salva')
                with open("Pastabanco/roi3", "r") as file:
                    roi_value3 = file.read()
                    roi_value3 = json.loads(roi_value3)

                roi_value3["x1"] = r_x1
                roi_value3["y1"] = r_y1
                roi_value3["x2"] = r_x2
                roi_value3["y2"] = r_y2

                roi_value3 = json.dumps(roi_value3)

                with open("Pastabanco/roi3", "w+") as file:
                    file.write(roi_value3)
                    file.close()

        elif cond == False:
        # --------------------------------------------- roi 1 ------------------------------------------
            if cv2.waitKey(1) == 49:
                print("a")
                messagebox.showinfo('Informação!', f'Posição 1 salva')
                with open("Pastabanco/roi1_cam2", "r") as file:
                    roi_value1 = file.read()
                    roi_value1 = json.loads(roi_value1)

                roi_value1["x1"] = r_x1
                roi_value1["y1"] = r_y1
                roi_value1["x2"] = r_x2
                roi_value1["y2"] = r_y2

                roi_value1 = json.dumps(roi_value1)

                with open("Pastabanco/roi1_cam2", "w+") as file:
                    file.write(roi_value1)
                    file.close()
                # --------------------------------------------- roi 2 ------------------------------------------
            elif cv2.waitKey(1) == 50:
                messagebox.showinfo('Informação!', f'Posição 2 salva')
                with open("Pastabanco/roi2_cam2", "r") as file:
                    roi_value2 = file.read()
                    roi_value2 = json.loads(roi_value2)

                roi_value2["x1"] = r_x1
                roi_value2["y1"] = r_y1
                roi_value2["x2"] = r_x2
                roi_value2["y2"] = r_y2

                roi_value2 = json.dumps(roi_value2)

                with open("Pastabanco/roi2_cam2", "w+") as file:
                    file.write(roi_value2)
                    file.close()
            # --------------------------------------------- roi 3 ------------------------------------------
            elif cv2.waitKey(1) == 51:
                messagebox.showinfo('Informação!', f'Posição 3 salva')
                with open("Pastabanco/roi3_cam2", "r") as file:
                    roi_value3 = file.read()
                    roi_value3 = json.loads(roi_value3)

                roi_value3["x1"] = r_x1
                roi_value3["y1"] = r_y1
                roi_value3["x2"] = r_x2
                roi_value3["y2"] = r_y2

                roi_value3 = json.dumps(roi_value3)

                with open("Pastabanco/roi3_cam2", "w+") as file:
                    file.write(roi_value3)
                    file.close()

        if cv2.waitKey(1) == 27:
            break


    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    roi_variable('road.mp4', False)

