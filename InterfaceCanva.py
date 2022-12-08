########################################################
#  Arquivo   : InterfaceCanva.py                       #
#  Nome      : Interface Grafica de Controle Canva     #
#  Autor     : Gabriel Monteiro Magan                  #
#  E-mail    : gabrielmagan2@gmail.com                 #
#  Data      : 28/09/2022                              #
#  Versão    : 1.2                                     #
########################################################
try:
    import threading
    import json
    import serial
    from tkinter import *
    from tkinter import messagebox

    from camPerso import Cam_rois
    from calibrar import calibrar_webcam
    from detecção_dupla import camera_1, camera_2
    from yolo_com_roi import cam_yolo
    from roiVariavel import roi_variable
except ImportError:
    messagebox.showinfo('Alerta', f'não foi possível importar o modulo')
    print('não foi possível importar o modulo')


cond = True
global esp32
def EscolhaCOM():
    portaCom = str
    vc = vCom.get()
    if vc == "COM1":
        portaCom = "COM1"
    elif vc == "COM2":
        portaCom = "COM2"
    elif vc == "COM3":
        portaCom = "COM3"
    elif vc == "COM4":
        portaCom = "COM4"
    elif vc == "COM5":
        portaCom = "COM5"
    elif vc == "COM6":
        portaCom = "COM6"
    elif vc == "COM7":
        portaCom = "COM7"
    elif vc == "COM8":
        portaCom = "COM8"
    elif vc == "COM9":
        portaCom = "COM9"
    elif vc == "COM10":
        portaCom = "COM10"
    elif vc == "COM11":
        portaCom = "COM11"
    elif vc == "COM12":
        portaCom = "COM12"
    elif vc == "COM13":
        portaCom = "COM13"
    elif vc == "COM14":
        portaCom = "COM14"
    elif vc == "COM15":
        portaCom = "COM15"
    elif vc == "COM16":
        portaCom = "COM16"
    elif vc == "COM17":
        portaCom = "COM17"
    elif vc == "COM18":
        portaCom = "COM18"
    elif vc == "COM19":
        portaCom = "COM19"
    elif vc == "COM20":
        portaCom = "COM20"
    else:
        pass

    portaComs = json.dumps(portaCom)

    with open("Pastabanco/COM", "w+") as file:
        file.write(portaComs)
        file.close()

def initCam1():
    with open("Pastabanco/roi1", "r") as file:
        roi_value1 = file.read()
        roi_value1 = json.loads(roi_value1)

    val1 = roi_value1['x1']
    val2 = roi_value1['y1']
    val3 = roi_value1['x2']
    val4 = roi_value1['y2']
    cam = roi_value1['cam']

    x1 = int(val1)
    y1 = int(val2)
    x2 = int(val3)
    y2 = int(val4)
    if cam != "road.mp4":
        camera = int(cam)
    else:
        camera = cam
    tamanho = x1,y1,x2,y2

    with open("Pastabanco/roi2", "r") as file:
        roi_value2 = file.read()
        roi_value2 = json.loads(roi_value2)

    val1_2 = roi_value2['x1']
    val2_2 = roi_value2['y1']
    val3_2 = roi_value2['x2']
    val4_2 = roi_value2['y2']

    x1_2 = int(val1_2)
    y1_2 = int(val2_2)
    x2_2 = int(val3_2)
    y2_2 = int(val4_2)

    tamanho1 = x1_2, y1_2, x2_2, y2_2

    with open("Pastabanco/roi3", "r") as file:
        roi_value2 = file.read()
        roi_value2 = json.loads(roi_value2)

    val1_2 = roi_value2['x1']
    val2_2 = roi_value2['y1']
    val3_2 = roi_value2['x2']
    val4_2 = roi_value2['y2']

    x1_2 = int(val1_2)
    y1_2 = int(val2_2)
    x2_2 = int(val3_2)
    y2_2 = int(val4_2)

    tamanho2 = x1_2, y1_2, x2_2, y2_2

    with open("Pastabanco/Scale", "r") as file:
        escalaF = file.read()
        escalaF = json.loads(escalaF)

    escala = escalaF['escala']
    vizinho = escalaF['vizinhos']

    with open("Pastabanco/cores", "r") as file:
        color = file.read()
        color = json.loads(color)

    cor1 = color['ROI1']
    cor2 = color['ROI2']

    Cam_rois(camera, cor1, cor2, escala, vizinho, tamanho, tamanho1, tamanho2)

def envioDados():
    roix1_1 = roi1_x1.get()
    roiy1_1 = roi1_y1.get()
    roix2_1 = roi1_x2.get()
    roiy2_1 = roi1_y2.get()

    roix1_2 = roi2_x1.get()
    roiy1_2 = roi2_y1.get()
    roix2_2 = roi2_x2.get()
    roiy2_2 = roi2_y2.get()

    roix1_3 = roi3_x1.get()
    roiy1_3 = roi3_y1.get()
    roix2_3 = roi3_x2.get()
    roiy2_3 = roi3_y2.get()

    with open("Pastabanco/roi1", "r") as file:
        roi_value1 = file.read()
        roi_value1 = json.loads(roi_value1)

    if roix1_1 != "":
        roi_value1["x1"] = roix1_1
    else:
        pass
    if roiy1_1 != "":
        roi_value1["y1"] = roiy1_1
    else:
        pass
    if roix2_1 != "":
        roi_value1["x2"] = roix2_1
    else:
        pass
    if roiy2_1 != "":
        roi_value1["y2"] = roiy2_1
    else:
        pass

    vC = cam.get()

    if vC == "Camera 1":
        roi_value1["cam"] = 0
    elif vC == "Camera 2":
        roi_value1["cam"] = 1
    elif vC == "Camera 3":
        roi_value1["cam"] = 2
    elif vC == "Camera 4":
        roi_value1["cam"] = 3
    elif vC == "Video":
        roi_value1["cam"] = "road.mp4"
    else:
        pass

    roi_value1 = json.dumps(roi_value1)

    with open("Pastabanco/roi1", "w+") as file:
        file.write(roi_value1)
        file.close()

# --------------------------------------------------- roi 2 value ---------------------------------------------------

    with open("Pastabanco/roi2", "r") as file:
        roi_value2 = file.read()
        roi_value2 = json.loads(roi_value2)

    if roix1_2 != "":
        roi_value2["x1"] = roix1_2
    else:
        pass
    if roiy1_2 != "":
        roi_value2["y1"] = roiy1_2
    else:
        pass
    if roix2_2 != "":
        roi_value2["x2"] = roix2_2
    else:
        pass
    if roiy2_2 != "":
        roi_value2["y2"] = roiy2_2
    else:
        pass

    vC = cam.get()

    if vC == "Camera 1":
        roi_value2["cam"] = 0
    elif vC == "Camera 2":
        roi_value2["cam"] = 1
    elif vC == "Camera 3":
        roi_value2["cam"] = 2
    elif vC == "Camera 4":
        roi_value2["cam"] = 3
    elif vC == "Video":
        roi_value2["cam"] = "road.mp4"
    else:
        pass

    roi_value2 = json.dumps(roi_value2)

    with open("Pastabanco/roi2", "w+") as file:
        file.write(roi_value2)
        file.close()

# --------------------------------------------------- roi 3 value ---------------------------------------------------

    with open("Pastabanco/roi3", "r") as file:
        roi_value3 = file.read()
        roi_value3 = json.loads(roi_value3)

    if roix1_3 != "":
        roi_value3["x1"] = roix1_3
    else:
        pass
    if roiy1_3 != "":
        roi_value3["y1"] = roiy1_3
    else:
        pass
    if roix2_3 != "":
        roi_value3["x2"] = roix2_3
    else:
        pass
    if roiy2_3 != "":
        roi_value3["y2"] = roiy2_3
    else:
        pass

    vC = cam.get()

    if vC == "Camera 1":
        roi_value3["cam"] = 0
    elif vC == "Camera 2":
        roi_value3["cam"] = 1
    elif vC == "Camera 3":
        roi_value3["cam"] = 2
    elif vC == "Camera 4":
        roi_value3["cam"] = 3
    elif vC == "Video":
        roi_value3["cam"] = "road.mp4"
    else:
        pass

    roi_value3 = json.dumps(roi_value3)

    with open("Pastabanco/roi3", "w+") as file:
        file.write(roi_value3)
        file.close()

def envioDados2():
    roix1_1 = cam2_roi1_x1.get()
    roiy1_1 = cam2_roi1_y1.get()
    roix2_1 = cam2_roi1_x2.get()
    roiy2_1 = cam2_roi1_y2.get()

    roix1_2 = cam2_roi2_x1.get()
    roiy1_2 = cam2_roi2_y1.get()
    roix2_2 = cam2_roi2_x2.get()
    roiy2_2 = cam2_roi2_y2.get()

    roix1_3 = cam2_roi3_x1.get()
    roiy1_3 = cam2_roi3_y1.get()
    roix2_3 = cam2_roi3_x2.get()
    roiy2_3 = cam2_roi3_y2.get()

    with open("Pastabanco/roi1_cam2", "r") as file:
        roi_value1 = file.read()
        roi_value1 = json.loads(roi_value1)

    if roix1_1 != "":
        roi_value1["x1"] = roix1_1
    else:
        pass
    if roiy1_1 != "":
        roi_value1["y1"] = roiy1_1
    else:
        pass
    if roix2_1 != "":
        roi_value1["x2"] = roix2_1
    else:
        pass
    if roiy2_1 != "":
        roi_value1["y2"] = roiy2_1
    else:
        pass

    vC = cam_1.get()

    if vC == "Camera 1":
        roi_value1["cam"] = 0
    elif vC == "Camera 2":
        roi_value1["cam"] = 1
    elif vC == "Camera 3":
        roi_value1["cam"] = 2
    elif vC == "Camera 4":
        roi_value1["cam"] = 3
    elif vC == "Video":
        roi_value1["cam"] = "road.mp4"
    else:
        pass

    roi_value1 = json.dumps(roi_value1)

    with open("Pastabanco/roi1_cam2", "w+") as file:
        file.write(roi_value1)
        file.close()

    # --------------------------------------------------- roi 2 value ---------------------------------------------------

    with open("Pastabanco/roi2_cam2", "r") as file:
        roi_value2 = file.read()
        roi_value2 = json.loads(roi_value2)

    if roix1_2 != "":
        roi_value2["x1"] = roix1_2
    else:
        pass
    if roiy1_2 != "":
        roi_value2["y1"] = roiy1_2
    else:
        pass
    if roix2_2 != "":
        roi_value2["x2"] = roix2_2
    else:
        pass
    if roiy2_2 != "":
        roi_value2["y2"] = roiy2_2
    else:
        pass

    vC = cam.get()

    if vC == "Camera 1":
        roi_value2["cam"] = 0
    elif vC == "Camera 2":
        roi_value2["cam"] = 1
    elif vC == "Camera 3":
        roi_value2["cam"] = 2
    elif vC == "Camera 4":
        roi_value2["cam"] = 3
    elif vC == "Video":
        roi_value2["cam"] = "road.mp4"
    else:
        pass

    roi_value2 = json.dumps(roi_value2)

    with open("Pastabanco/roi2_cam2", "w+") as file:
        file.write(roi_value2)
        file.close()

    # --------------------------------------------------- roi 3 value ---------------------------------------------------

    with open("Pastabanco/roi3_cam2", "r") as file:
        roi_value3 = file.read()
        roi_value3 = json.loads(roi_value3)

    if roix1_3 != "":
        roi_value3["x1"] = roix1_3
    else:
        pass
    if roiy1_3 != "":
        roi_value3["y1"] = roiy1_3
    else:
        pass
    if roix2_3 != "":
        roi_value3["x2"] = roix2_3
    else:
        pass
    if roiy2_3 != "":
        roi_value3["y2"] = roiy2_3
    else:
        pass

    vC = cam.get()

    if vC == "Camera 1":
        roi_value3["cam"] = 0
    elif vC == "Camera 2":
        roi_value3["cam"] = 1
    elif vC == "Camera 3":
        roi_value3["cam"] = 2
    elif vC == "Camera 4":
        roi_value3["cam"] = 3
    elif vC == "Video":
        roi_value3["cam"] = "road.mp4"
    else:
        pass

    roi_value3 = json.dumps(roi_value3)

    with open("Pastabanco/roi3_cam2", "w+") as file:
        file.write(roi_value3)
        file.close()

def initCam2():
    with open("Pastabanco/roi1_cam2", "r") as file:
        roi_value1 = file.read()
        roi_value1 = json.loads(roi_value1)

    val1 = roi_value1['x1']
    val2 = roi_value1['y1']
    val3 = roi_value1['x2']
    val4 = roi_value1['y2']
    cam = roi_value1['cam']

    x1 = int(val1)
    y1 = int(val2)
    x2 = int(val3)
    y2 = int(val4)
    if cam != "road.mp4":
        camera = int(cam)
    else:
        camera = cam

    tamanho = x1, y1, x2, y2

    with open("Pastabanco/roi2_cam2", "r") as file:
        roi_value2 = file.read()
        roi_value2 = json.loads(roi_value2)

    val1_2 = roi_value2['x1']
    val2_2 = roi_value2['y1']
    val3_2 = roi_value2['x2']
    val4_2 = roi_value2['y2']

    x1_2 = int(val1_2)
    y1_2 = int(val2_2)
    x2_2 = int(val3_2)
    y2_2 = int(val4_2)

    tamanho1 = x1_2, y1_2, x2_2, y2_2

    with open("Pastabanco/roi3_cam2", "r") as file:
        roi_value2 = file.read()
        roi_value2 = json.loads(roi_value2)

    val1_2 = roi_value2['x1']
    val2_2 = roi_value2['y1']
    val3_2 = roi_value2['x2']
    val4_2 = roi_value2['y2']

    x1_2 = int(val1_2)
    y1_2 = int(val2_2)
    x2_2 = int(val3_2)
    y2_2 = int(val4_2)

    tamanho2 = x1_2, y1_2, x2_2, y2_2

    with open("Pastabanco/Scale", "r") as file:
        escalaF = file.read()
        escalaF = json.loads(escalaF)

    escala = escalaF['escala']
    vizinho = escalaF['vizinhos']

    with open("Pastabanco/cores", "r") as file:
        color = file.read()
        color = json.loads(color)

    cor1 = color['ROI1']
    cor2 = color['ROI2']

    Cam_rois(camera, cor1, cor2, escala, vizinho, tamanho, tamanho1, tamanho2)

def calibrar():
    with open("Pastabanco/roi1", "r") as file:
        roi_value1 = file.read()
        roi_value1 = json.loads(roi_value1)

    val1 = roi_value1['x1']
    val2 = roi_value1['y1']
    val3 = roi_value1['x2']
    val4 = roi_value1['y2']
    cam = roi_value1['cam']

    x1 = int(val1)
    y1 = int(val2)
    x2 = int(val3)
    y2 = int(val4)
    if cam != "road.mp4":
        camera = int(cam)
    else:
        camera = cam

    tamanho = x1, y1, x2, y2

    with open("Pastabanco/roi2", "r") as file:
        roi_value2 = file.read()
        roi_value2 = json.loads(roi_value2)

    val1_2 = roi_value2['x1']
    val2_2 = roi_value2['y1']
    val3_2 = roi_value2['x2']
    val4_2 = roi_value2['y2']

    x1_2 = int(val1_2)
    y1_2 = int(val2_2)
    x2_2 = int(val3_2)
    y2_2 = int(val4_2)

    tamanho1 = x1_2, y1_2, x2_2, y2_2

    with open("Pastabanco/roi3", "r") as file:
        roi_value2 = file.read()
        roi_value2 = json.loads(roi_value2)

    val1_2 = roi_value2['x1']
    val2_2 = roi_value2['y1']
    val3_2 = roi_value2['x2']
    val4_2 = roi_value2['y2']

    x1_2 = int(val1_2)
    y1_2 = int(val2_2)
    x2_2 = int(val3_2)
    y2_2 = int(val4_2)

    tamanho2 = x1_2, y1_2, x2_2, y2_2
    calibrar_webcam(camera, tamanho, tamanho1, tamanho2)

def botao_On_all_cam():
    global esp32
    with open("Pastabanco/roi1", "r") as file:
        roi_value1 = file.read()
        roi_value1 = json.loads(roi_value1)

    val1 = roi_value1['x1']
    val2 = roi_value1['y1']
    val3 = roi_value1['x2']
    val4 = roi_value1['y2']
    cam = roi_value1['cam']

    x1 = int(val1)
    y1 = int(val2)
    x2 = int(val3)
    y2 = int(val4)
    if cam != "road.mp4":
        camera = int(cam)
    else:
        camera = cam
    tamanho = x1,y1,x2,y2

    with open("Pastabanco/roi2", "r") as file:
        roi_value2 = file.read()
        roi_value2 = json.loads(roi_value2)

    val1_2 = roi_value2['x1']
    val2_2 = roi_value2['y1']
    val3_2 = roi_value2['x2']
    val4_2 = roi_value2['y2']

    x1_2 = int(val1_2)
    y1_2 = int(val2_2)
    x2_2 = int(val3_2)
    y2_2 = int(val4_2)

    tamanho1 = x1_2, y1_2, x2_2, y2_2

    with open("Pastabanco/roi3", "r") as file:
        roi_value2 = file.read()
        roi_value2 = json.loads(roi_value2)

    val1_2 = roi_value2['x1']
    val2_2 = roi_value2['y1']
    val3_2 = roi_value2['x2']
    val4_2 = roi_value2['y2']

    x1_2 = int(val1_2)
    y1_2 = int(val2_2)
    x2_2 = int(val3_2)
    y2_2 = int(val4_2)

    tamanho2 = x1_2, y1_2, x2_2, y2_2

#-------------------------------------------------------------------camera 2 ------------------------------------------------
    with open("Pastabanco/roi1_cam2", "r") as file:
        roi_value1 = file.read()
        roi_value1 = json.loads(roi_value1)

    val1 = roi_value1['x1']
    val2 = roi_value1['y1']
    val3 = roi_value1['x2']
    val4 = roi_value1['y2']
    cam = roi_value1['cam']

    x1 = int(val1)
    y1 = int(val2)
    x2 = int(val3)
    y2 = int(val4)
    if cam != "road.mp4":
        camera1 = int(cam)
    else:
        camera1 = cam

    tamanho_1 = x1, y1, x2, y2

    with open("Pastabanco/roi2_cam2", "r") as file:
        roi_value2 = file.read()
        roi_value2 = json.loads(roi_value2)

    val1_2 = roi_value2['x1']
    val2_2 = roi_value2['y1']
    val3_2 = roi_value2['x2']
    val4_2 = roi_value2['y2']

    x1_2 = int(val1_2)
    y1_2 = int(val2_2)
    x2_2 = int(val3_2)
    y2_2 = int(val4_2)

    tamanho1_1 = x1_2, y1_2, x2_2, y2_2

    with open("Pastabanco/roi3_cam2", "r") as file:
        roi_value2 = file.read()
        roi_value2 = json.loads(roi_value2)

    val1_2 = roi_value2['x1']
    val2_2 = roi_value2['y1']
    val3_2 = roi_value2['x2']
    val4_2 = roi_value2['y2']

    x1_2 = int(val1_2)
    y1_2 = int(val2_2)
    x2_2 = int(val3_2)
    y2_2 = int(val4_2)

    tamanho2_1 = x1_2, y1_2, x2_2, y2_2

    with open("Pastabanco/Scale", "r") as file:
        escalaF = file.read()
        escalaF = json.loads(escalaF)

    escala_1 = escalaF['escala']
    vizinho_1 = escalaF['vizinhos']

    camera_1_theads = threading.Thread(target=camera_1, args=[camera, escala_1 , vizinho_1, tamanho, tamanho1, tamanho2, esp32])
    camera_2_theads = threading.Thread(target=camera_2, args=[camera1, escala_1, vizinho_1, tamanho_1, tamanho1_1, tamanho2_1, esp32])

    camera_1_theads.start()
    camera_2_theads.start()

def init_yolo1():
    with open("Pastabanco/roi1", "r") as file:
        roi_value1 = file.read()
        roi_value1 = json.loads(roi_value1)

    val1 = roi_value1['x1']
    val2 = roi_value1['y1']
    val3 = roi_value1['x2']
    val4 = roi_value1['y2']
    cam = roi_value1['cam']

    x1 = int(val1)
    y1 = int(val2)
    x2 = int(val3)
    y2 = int(val4)
    if cam != "road.mp4":
        camera = int(cam)
    else:
        camera = cam
    tamanho = x1, y1, x2, y2

    with open("Pastabanco/roi2", "r") as file:
        roi_value2 = file.read()
        roi_value2 = json.loads(roi_value2)

    val1_2 = roi_value2['x1']
    val2_2 = roi_value2['y1']
    val3_2 = roi_value2['x2']
    val4_2 = roi_value2['y2']

    x1_2 = int(val1_2)
    y1_2 = int(val2_2)
    x2_2 = int(val3_2)
    y2_2 = int(val4_2)

    tamanho1 = x1_2, y1_2, x2_2, y2_2

    with open("Pastabanco/roi3", "r") as file:
        roi_value2 = file.read()
        roi_value2 = json.loads(roi_value2)

    val1_2 = roi_value2['x1']
    val2_2 = roi_value2['y1']
    val3_2 = roi_value2['x2']
    val4_2 = roi_value2['y2']

    x1_2 = int(val1_2)
    y1_2 = int(val2_2)
    x2_2 = int(val3_2)
    y2_2 = int(val4_2)

    tamanho2 = x1_2, y1_2, x2_2, y2_2


    with open("Pastabanco/cores", "r") as file:
        color = file.read()
        color = json.loads(color)

    cor1 = color['ROI1']
    cor2 = color['ROI2']

    cam_yolo(camera, cor1, cor2, tamanho, tamanho1, tamanho2, esp32, False)

def init_yolo2():
    with open("Pastabanco/roi1_cam2", "r") as file:
        roi_value1 = file.read()
        roi_value1 = json.loads(roi_value1)

    val1 = roi_value1['x1']
    val2 = roi_value1['y1']
    val3 = roi_value1['x2']
    val4 = roi_value1['y2']
    cam = roi_value1['cam']

    x1 = int(val1)
    y1 = int(val2)
    x2 = int(val3)
    y2 = int(val4)
    if cam != "road.mp4":
        camera = int(cam)
    else:
        camera = cam

    tamanho = x1, y1, x2, y2

    with open("Pastabanco/roi2_cam2", "r") as file:
        roi_value2 = file.read()
        roi_value2 = json.loads(roi_value2)

    val1_2 = roi_value2['x1']
    val2_2 = roi_value2['y1']
    val3_2 = roi_value2['x2']
    val4_2 = roi_value2['y2']

    x1_2 = int(val1_2)
    y1_2 = int(val2_2)
    x2_2 = int(val3_2)
    y2_2 = int(val4_2)

    tamanho1 = x1_2, y1_2, x2_2, y2_2

    with open("Pastabanco/roi3_cam2", "r") as file:
        roi_value2 = file.read()
        roi_value2 = json.loads(roi_value2)

    val1_2 = roi_value2['x1']
    val2_2 = roi_value2['y1']
    val3_2 = roi_value2['x2']
    val4_2 = roi_value2['y2']

    x1_2 = int(val1_2)
    y1_2 = int(val2_2)
    x2_2 = int(val3_2)
    y2_2 = int(val4_2)

    tamanho2 = x1_2, y1_2, x2_2, y2_2

    with open("Pastabanco/cores", "r") as file:
        color = file.read()
        color = json.loads(color)

    cor1 = color['ROI1']
    cor2 = color['ROI2']

    cam_yolo(camera, cor1, cor2, tamanho, tamanho1, tamanho2, esp32 ,True)

def ligar():
    global esp32
    global cond
    with open("Pastabanco/COM", "r") as file:
        PortaCOM = file.read()
        PortaCOM = json.loads(PortaCOM)

    portCOM = str(PortaCOM)
    if cond == True:
        esp32 = serial.Serial(portCOM, 115200)
        cond = False
    try:
        esp32.write(b'1')
        messagebox.showinfo("Iniciando!", f'LIGANDO SEMÁFOROS')
    except:
        return messagebox.showinfo("Alerta!!", f'A porta serial {portCOM} não esta disponivel')

def desligar():
    with open("Pastabanco/COM", "r") as file:
        PortaCOM = file.read()
        PortaCOM = json.loads(PortaCOM)

    portCOM = str(PortaCOM)
    try:
        esp32.write(b'0')
        messagebox.showinfo("Encerrando!", f'DESLIGANDO SEMÁFOROS')
    except:
        return messagebox.showinfo("Alerta!!", f'A porta serial {portCOM} não esta disponivel')

def autoroi_1():
    with open("Pastabanco/roi1", "r") as file:
        roi_value1 = file.read()
        roi_value1 = json.loads(roi_value1)
    cam = roi_value1['cam']

    roi_variable(cam, True)

def autoroi_2():
    with open("Pastabanco/roi1_cam2", "r") as file:
        roi_value1 = file.read()
        roi_value1 = json.loads(roi_value1)
    cam = roi_value1['cam']

    roi_variable(cam, False)

tela = Tk()
tela.title("CONTROL SMART TRAFFIC WAY")
tela.geometry("989x860")
tela.configure(background="white")
tela.iconbitmap("image/bosch.ico")

bg = PhotoImage(file="image/back.png")
fundo = Label(tela, image=bg)
fundo.place(x=0,y=0)


COMs = ["COM1","COM2","COM3","COM4","COM5","COM6","COM7","COM8","COM9","COM10","COM11","COM12","COM13","COM14","COM15","COM16","COM17","COM18","COM19","COM20"]
vCom=StringVar()
vCom.set(COMs[0])
menuDeOpcoes = OptionMenu(tela,vCom, *COMs)
menuDeOpcoes.place(x= 756, y=22, width=120 , height=35, bordermode=OUTSIDE)

Button(tela, text='SEND', command=EscolhaCOM, background='white', font=('arial',12,"bold"), foreground='#013C6B', borderwidth=0).place(x= 883, y=21, width=87 , height=35)

# -----------------------------------------------------------  camera 1  -----------------------------------------------------------

roi1_x1 = Entry(tela, font=("arial",12,"bold"))
roi1_x1.place(x=76, y=224, width=57 , height=36, )

roi1_y1 = Entry(tela, font=("arial",12,"bold"))
roi1_y1.place(x=143, y=224, width=57 , height=36)

roi1_x2 = Entry(tela, font=("arial",12,"bold"))
roi1_x2.place(x=76, y=293, width=57 , height=36)

roi1_y2 = Entry(tela, font=("arial",12,"bold"))
roi1_y2.place(x=143, y=293, width=57 , height=36)


roi2_x1 = Entry(tela, font=("arial",12,"bold"))
roi2_x1.place(x=76, y=408, width=57 , height=36)

roi2_y1 = Entry(tela, font=("arial",12,"bold"))
roi2_y1.place(x=143, y=408, width=57 , height=36)

roi2_x2 = Entry(tela, font=("arial",12,"bold"))
roi2_x2.place(x=76, y=476, width=57 , height=36)

roi2_y2 = Entry(tela, font=("arial",12,"bold"))
roi2_y2.place(x=143, y=476, width=57 , height=36)


roi3_x1=Entry(tela, font=("arial",12,"bold"))
roi3_x1.place(x=76, y=593, width=57 , height=36)

roi3_y1=Entry(tela, font=("arial",12,"bold"))
roi3_y1.place(x=143, y=593, width=57 , height=36)

roi3_x2=Entry(tela, font=("arial",12,"bold"))
roi3_x2.place(x=76, y=661, width=57 , height=36)

roi3_y2=Entry(tela, font=("arial",12,"bold"))
roi3_y2.place(x=143, y=661, width=57 , height=36)

cams = ["Camera 1","Camera 2","Camera 3","Camera 4","Video"]
cam = StringVar()
cam.set(cams[0])
menuDeOpcoes2 = OptionMenu(tela,cam, *cams)
menuDeOpcoes2.place(x= 62, y=725, width=241 , height=28)

Button(tela, text='AUTO', command=autoroi_1, background='White', font=('arial',12, "bold"), foreground='#013C6B', borderwidth=0).place(x=62, y=769, width=70, height=35)

Button(tela, text="SEND", command=envioDados, background='white', font=('arial',12,"bold"), foreground='#013C6B', borderwidth=0).place(x=147, y=769, width=70, height=35)

Button(tela, text="TEST", command=initCam1, background='white', font=('arial',12,"bold"), foreground='#013C6B', borderwidth=0).place(x=232, y=769, width=70, height=35)

# # -----------------------------------------------------------  camera 2  -----------------------------------------------------------


cam2_roi1_x1 = Entry(tela, font=("arial",12,"bold"))
cam2_roi1_x1.place(x=390, y=224, width=57 , height=36)

cam2_roi1_y1 = Entry(tela, font=("arial",12,"bold"))
cam2_roi1_y1.place(x=458, y=224, width=57 , height=36)

cam2_roi1_x2 = Entry(tela, font=("arial",12,"bold"))
cam2_roi1_x2.place(x=390, y=293, width=57 , height=36)

cam2_roi1_y2 = Entry(tela, font=("arial",12,"bold"))
cam2_roi1_y2.place(x=458, y=293, width=57 , height=36)


cam2_roi2_x1 = Entry(tela, font=("arial",12,"bold"))
cam2_roi2_x1.place(x=390, y=408, width=57 , height=36)

cam2_roi2_y1 = Entry(tela, font=("arial",12,"bold"))
cam2_roi2_y1.place(x=458, y=408, width=57 , height=36)

cam2_roi2_x2 = Entry(tela, font=("arial",12,"bold"))
cam2_roi2_x2.place(x=390, y=476, width=57 , height=36)

cam2_roi2_y2 = Entry(tela, font=("arial",12,"bold"))
cam2_roi2_y2.place(x=458, y=476, width=57 , height=36)


cam2_roi3_x1=Entry(tela, font=("arial",12,"bold"))
cam2_roi3_x1.place(x=390, y=593, width=57 , height=36)

cam2_roi3_y1=Entry(tela, font=("arial",12,"bold"))
cam2_roi3_y1.place(x=458, y=593, width=57 , height=36)

cam2_roi3_x2=Entry(tela, font=("arial",12,"bold"))
cam2_roi3_x2.place(x=390, y=661, width=57 , height=36)

cam2_roi3_y2=Entry(tela, font=("arial",12,"bold"))
cam2_roi3_y2.place(x=458, y=661, width=57 , height=36)

cams_1 = ["Camera 1","Camera 2","Camera 3","Camera 4","Video"]
cam_1=StringVar()
cam_1.set(cams[1])
menuDeOpcoes3 = OptionMenu(tela,cam_1, *cams_1)
menuDeOpcoes3.place(x= 376, y=725, width=241 , height=28)


Button(tela, text='AUTO', command=autoroi_2, background='white', font=('arial',12,"bold"), foreground='#013C6B', borderwidth=0).place(x=376, y=769, width=70, height=35)

Button(tela, text="SEND", command=envioDados2, background='white', font=('arial',12,"bold"), foreground='#013C6B', borderwidth=0).place(x=461, y=769, width=70, height=35)

Button(tela, text="TEST", command=initCam2, background='white', font=('arial',12,"bold"), foreground='#013C6B', borderwidth=0).place(x=546, y=769, width=70, height=35)


imgbotao1 = PhotoImage(file="image/botao/on.png")
imgbotao2 = PhotoImage(file="image/botao/off.png")

botao_on = Button(tela, image=imgbotao1, command=ligar, borderwidth=0, background="#013C6B").place(x=717, y=201, width=76, height=75)

botao_off = Button(tela, image=imgbotao2, command=desligar, borderwidth=0, background="#013C6B").place(x=825, y=201, width=76, height=75)


imgbotao3 = PhotoImage(file="image/botao/start.png")
imgbotao4 = PhotoImage(file="image/botao/calibrar.png")

botao_On_all = Button(tela, image=imgbotao3, command=botao_On_all_cam, borderwidth=0, background="#013C6B").place(x=717, y=419, width=184, height=74)

botao_cali = Button(tela, image=imgbotao4,background="#013C6B" ,command=calibrar, borderwidth=0).place(x=717, y=310, width=184, height=74)


imgYolo1 = PhotoImage(file="image/botao/1.png")

imgYolo2 = PhotoImage(file="image/botao/2.png")

botao_fiap = Button(tela, image=imgYolo1,background="#013C6B" ,command=init_yolo1, borderwidth=0).place(x=717, y=583, width=184, height=74)

botao_alura = Button(tela, image=imgYolo2,background="#013C6B" ,command=init_yolo2, borderwidth=0).place(x=717, y=690, width=184, height=74)

tela.mainloop()