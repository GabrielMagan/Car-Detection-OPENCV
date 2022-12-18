<div style="display: inline_block" ><br>
  <h1 align="center">
   <img align="center" alt="mgn-Csharp" height="30" width="40" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/opencv/opencv-original.svg"> Detecção de veículos utilizando OPENCV <img align="center" alt="mgn-Csharp" height="30" width="40" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/opencv/opencv-original.svg">
  

### ⚠️(Aviso)⚠️
- Para utilização da função "video" é necessário baixar um vídeo contendo o nome "road.mp4" e jogá-lo na mesma pasta que estam os arquivos .py

### 📋(Sobre)📋
- Desenvolvi um software de detecção de veículos para a challenge FIAP & BOSCH 2022.

- O software se consiste em um sistema de detecção de veículos que contem 2 algoritmos de visão computacional para a identificação de carros.
<h1 align="center">
  <img alt="NextLevelWeek" title="#NextLevelWeek" src="https://user-images.githubusercontent.com/111460258/208217573-04859efa-200f-4dfc-91e0-78a4b74b4fe3.png" />
</h1>

- Esse software utilizava a rede neural Yolo v4 e o modelo Haar Cascade para identificar os objetos.

<h1 align="center">
  <img alt="NextLevelWeek" title="#NextLevelWeek" src="https://user-images.githubusercontent.com/111460258/208217871-bd2b00f1-f3d6-487e-bf1f-cf70a85e660e.png" />

  <img alt="NextLevelWeek" title="#NextLevelWeek" src="https://user-images.githubusercontent.com/111460258/208217910-f60aa7b1-9327-4f03-bfae-15db69b096a9.png" />
</h1>

- Foi criada uma maquete da Avenida Paulista para assim poder simular um tráfego de veículos.

<h1 align="center">
  <img alt="NextLevelWeek" title="#NextLevelWeek" src="https://user-images.githubusercontent.com/111460258/208218028-1b80ef7d-3699-4fc7-a441-ea6b8d0b77de.png" />
</h1>

- Com MVP pronto conseguimos testar esse sistema com excelência.

<h1 align="center">
  <img alt="NextLevelWeek" title="#NextLevelWeek" src="https://user-images.githubusercontent.com/111460258/208218088-8b93835f-da35-4174-9b3d-164de036d9e5.png" />
</h1>

### 💻(Yolo)💻

- Para utilização da rede neural yolo, desenvolvi um script básico que utiliza a webcam para detecção de objetos.

<h4 align="center">Importando as bibliotecas necessárias</h4>

```bash
import cv2      # Importa a lib OPENCV
import time     # importa a lib time
```

<h4 align="center">Criando uma lista de cores</h4>

```bash
COLORS = [(0,255,0), (255,0,0),  (255,0,0), (255,255,0)]      # Cria uma lista de cores no modelo BGR
```

<h4 align="center">Abrindo o aquirvo de nomes</h4>

```bash
with open('nomes/coco.names', 'r') as f:      # Abre o arquivo de nomes da YOLO
   class_name = [cname.strip() for cname in f.readlines()]      # importa os nomes do arquivo para uma lista
```

<h4 align="center">Configurando a webcam</h4>

```bash
cap = cv2.VideoCapture(0)   # A funcao VideoCapture() recebe o video de uma camera ou de um arquivo
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)     # seta a largura do video
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)      # seta a altura do video
```

<h4 align="center">Configurando a rede neural</h4>

```bash
net = cv2.dnn.readNet('yolov4-tiny.weights','yolov4-tiny.cfg')      # Descarrega os dados dos arquivos da YOLO em uma variavel
model = cv2.dnn_DetectionModel(net)     # Aplica a variavel no modelo de treino
model.setInputParams(size=(416,416), scale=1/255)     # Seta os parametros para funcionamento do modelo 
```

<h4 align="center">Iniciando loop para verificação</h4>

```bash
while True:
    _, frame = cap.read()     # Funcao .read() le o frame atual de um video
    start = time.time()     # Inicia um contator para calcular o FPS do video
    classes, scores, boxes = model.detect(frame, 0.1, 0.2)      # Aplica o modelo de deteccao de objetos 
    end = time.time()     # Finaliza o contator para calcular o FPS do video
    frame = cv2.flip(frame, 1)      # Inverte o frame horizontalmente
```

<h4 align="center">Verificação de objetos no frame</h4>

```bash
    for (classid, score, box) in zip(classes, scores, boxes):     # Utilizando um for distribuimos os dados em listas
        color = COLORS[int(classid) % len(COLORS)]      # Criamos a variavel color para receber uma cor especifica
        label = f"{class_name[classid]} {score*100} "     # Criamos a variavel label para receber o nome do objeto e o score dele
        cv2.rectangle(frame, box, color, 2)     # Gera o retangulo em volta do objeto detectado 
        cv2.putText(frame, label, (box[0], box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color , 2)      # Escreve a variavel label no frame
```

<h4 align="center">FPS no frame</h4>

```bash
    fps_label = f'FPS: {round((1.0/(end-start)),2)}'      # Faz o calculo de quantos FPS contem no video
    cv2.putText(frame,fps_label, (0,25), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,0), 5)      # Cria uma sombra no texto de FPS
    cv2.putText(frame, fps_label, (0, 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)     # Crka o texto de FPS
    cv2.imshow('camera', frame)      # Exibe o frame com o nome "camera"
```

<h4 align="center">Finalização</h4>

```bash
     if cv2.waitKey(1) == 27:     # funcao .waitKey() cria um delay e combinada com o if, gera uma tecla de escape
        break     # Pare o while 
cap.release()     # Libera a webcam
cv2.destroyAllWindows()     # Destroi todas as janelas criadas
```





    




