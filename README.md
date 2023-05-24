# Deteccion de objetos en video 💻

El propósito de este proyecto es implementar un sistema de detección de objetos utilizando el lenguaje de programación [Python](https://www.python.org) ya que se ha convertido en uno de los lenguajes de programación más populares en el ámbito de la inteligencia artificial y el aprendizaje automático debido a su simplicidad, versatilidad y una amplia gama de bibliotecas especializadas disponibles, y la arquitectura [YOLO](https://pjreddie.com/darknet/yolo/)  (*You Only Look Once*) junto con [PyTorch](https://pytorch.org) que es una poderosa biblioteca de aprendizaje automático que proporciona herramientas para construir y entrenar redes neuronales de manera eficiente.

Como dijimos previamente, utilizaremos  [Python](https://www.python.org) y [PyTorch](https://pytorch.org) (entre otras librerías, pero en especial PyTorch) para implementar el algoritmo [YOLO](https://pjreddie.com/darknet/yolo/)  , que es conocido por lograr un equilibrio entre precisión y velocidad, lo que lo convierte en una opción ideal para aplicaciones en tiempo real. Además, aprovecharemos las numerosas librerías disponibles en Python para facilitar el procesamiento de imágenes y la visualización de resultados.

![](https://i0.wp.com/blog.330ohms.com/wp-content/uploads/2020/11/yolo_bounding_boxes.png?w=700&ssl=1)

## Integrantes del grupo del proyecto
- Matías Araya
- Pablo Osorio
- Agustín Sandoval

# 🚨 AVISO 🚨

Tanto el entrenamiento como predicciones con este modelo se ven beneficiadas si se cumple con una computadora que tenga una GPU NVIDIA.

Por default este modelo esta pre entrenado para detecta 80 distintos objetos, la lista de estos se encuentra en el archivo [data/coco.names](https://github.com/puigalex/deteccion-objetos-video/blob/master/data/coco.names)

Los pasos a seguir para poder correr detección de objetos en el video o de una webcam son los siguientes (Previamente tiene que tener instalado [Anaconda](https://linuxhint.com/install-anaconda-ubuntu-22-04/) y [OpenCV](https://geekytheory.com/opencv-en-linux/)):

# 1. Clonar o Descargar el Proyecto (Aviso importante‼️)
Aun **NO! **es necesario **Clonar** o **Descargar** el repositorio ya que todavía está en desarrollo. Una vez finalizado... se colocarán las correspondientes direcciones para clonar o descargar.

# 2. Crear ambiente (Anaconda) 🐍
![](https://o.remove.bg/downloads/03d59b4b-97f1-4b6e-ac20-1252fd7c7ae4/kisspng-anaconda-pip-installation-python-5be51c73cb3bb1.4617931315417416838325-removebg-preview.png)

Para tener en orden nuestras paqueterías de Python primero vamos a crear un ambiente a través de la terminal con el nombre que ustedes deseen, por ejemplo: "deteccionobjetos"el cual tiene la versión 3.6 de Python.
``` 
conda create -n deteccionobjetos python=3.6
```

Una vez creado, activamos el ambiente **deteccionobjetos** para asegurarnos que estemos en el ambiente correcto al momento de hacer la instalación de todas las paqueterías necesarias.
```
source activate deteccionobjetos
```

# 3. Instalación de las paqueterias  📚

Estando dentro de nuestro ambiente vamos a instalar todas las paqueterías necesarias para correr nuestro detector de objetos en video, la lista de los paquetes y versiones a instalar están dentro del archivo **requirements.txt** por lo cual instalaremos haciendo referencia a ese archivo
```
pip install -r requirements.txt
```
# 4. Descargar los pesos del modelo entrenado (YOLO) 🔎🧠
![](https://assets.website-files.com/5f6bc60e665f54db361e52a9/5f6bc60e665f546a6b1e5400_logo_yolo.png)Para poder correr el modelo de YOLO tendremos que descargar los pesos de la red neuronal, los pesos son los valores que tienen todas las conexiones entre las neuronas de la red neuronal de YOLO, este tipo de modelos son computacionalmente muy pesados de entrenar desde cero por lo cual descargar el modelo pre entrenado es una buena opción.
```
bash weights/download_weights.sh
```
Movemos los pesos descargados a la carpeta llamada weights (O simplemente pueden arrastrar o cortar y pegar el archivo **yolov3.weights** y pegarlos en la carpeta **weights**  )
```
mv yolov3.weights weights/
```
# 5. Correr el detector de objetos en Webcam 📷

Finalmente usaremos este comando el cual activa la camara web para poder hacer deteccion de video sobre un video **"en vivo"** (REC 🔴)
```
python deteccion_video.py
```
# 6. Correr el de detector de objetos en un Video.mp4 

Si en vez de correr detección de objetos sobre la webcam lo que quieres es correr el modelo sobre un video que ya fue pre grabado **(video.mp4)**, tienes que cambiar el comando para correr el codigo a:
```
python deteccion_video.py --webcam 0 --directorio_video <directorio_al_video.mp4>
```
