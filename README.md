# Detección de objetos en video 💻

El propósito de este proyecto es implementar un sistema de detección de objetos utilizando el lenguaje de programación [Python](https://www.python.org) ya que se ha convertido en uno de los lenguajes de programación más populares en el ámbito de la inteligencia artificial y el aprendizaje automático debido a su simplicidad, versatilidad y una amplia gama de bibliotecas especializadas disponibles, y la arquitectura [YOLO](https://pjreddie.com/darknet/yolo/)  (*You Only Look Once*) junto con [PyTorch](https://pytorch.org) que es una poderosa biblioteca de aprendizaje automático que proporciona herramientas para construir y entrenar redes neuronales de manera eficiente.

Como dijimos previamente, utilizaremos  [Python](https://www.python.org) y [PyTorch](https://pytorch.org) (entre otras librerías, pero en especial PyTorch) para implementar el algoritmo [YOLO](https://pjreddie.com/darknet/yolo/)  , que es conocido por lograr un equilibrio entre precisión y velocidad, lo que lo convierte en una opción ideal para aplicaciones en tiempo real. Además, aprovecharemos las numerosas librerías disponibles en Python para facilitar el procesamiento de imágenes y la visualización de resultados.

![](https://i0.wp.com/blog.330ohms.com/wp-content/uploads/2020/11/yolo_bounding_boxes.png?w=700&ssl=1)

## Integrantes del grupo del proyecto
- Matías Araya
- Pablo Osorio
- Agustín Sandoval

# 🚨 AVISO 🚨

Las predicciones con este modelo se ven beneficiadas si se cumple con una computadora que tenga una GPU NVIDIA.

Por default este modelo esta pre entrenado para detecta 80 objetos distintos, la lista de estos se encuentra en el archivo [data/coco.names](https://github.com/puigalex/deteccion-objetos-video/blob/master/data/coco.names)

Previamente tiene que tener instalado [Anaconda](https://www.anaconda.com) y [OpenCV](https://opencv.org).

Le sugerimos los siguientes Sitios Webs y video de como hacer una correcta instalación: 

**Anaconda** 🐍

Video:
``` 
https://www.youtube.com/watch?v=QJsyqy0eKBE&t=298s
```
Sitio Web:
``` 
https://linuxhint.com/install-anaconda-ubuntu-22-04/
```

**OpenCV** 🟢🔴🔵

Sitio Web:
``` 
https://geekytheory.com/opencv-en-linux/
```


Los pasos a seguir para poder correr detección de objetos en el video o de una webcam son los siguientes: 


# 1. Clonar o Descargar el Proyecto

Para **Clonar** el repositorio simplmente puede ir a la pestaña que sale en color "Verde" (🟢<> Code🟢) y copiar el HTTPS o **Descargar**.

**Enlace**
``` 
https://github.com/matias-araya-02/ProyectoMetodologia.git
```

**Ejemplo de descarga**

[Descargar](https://raw.githubusercontent.com/matias-araya-02/ProyectoMetodologia/master/Bienvenidos!.txt)

## IMPORTANTE ‼️

Una vez **Clonado** o **Descargado** el Respositorio... deberá realizar los pasos que vienen a continuación dentro de la carpeta de **Deteccion-Objetos**. 
Es decir, a través de la terminal de dicha carpeta. 

# 2. Crear ambiente (Anaconda) 🐍

![](https://microchip.wdfiles.com/local--files/swtools:anaconda/anaconda_logo.png)

Para tener en orden nuestras paqueterías de Python primero tenemos que crear un ambiente en la terminal con el nombre que ustedes deseen, por ejemplo: "deteccionobjetos"el cual va a tener la versión 3.6 de Python.
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
![](https://assets.website-files.com/5f6bc60e665f54db361e52a9/5f6bc60e665f546a6b1e5400_logo_yolo.png) 

Para poder correr el modelo de YOLO tendremos que descargar los pesos de la red neuronal, este tipo de modelos son muy pesados de entrenar desde cero por lo cual descargar el modelo pre entrenado será la mejor opción.
```
bash weights/download_weights.sh
```
Movemos los pesos descargados a la carpeta llamada weights (O simplemente pueden arrastrar o cortar y pegar el archivo **yolov3.weights** y pegarlos en la carpeta **weights**)
```
mv yolov3.weights weights/
```
# 5. Correr el detector de objetos en Webcam 📷

Finalmente usaremos este comando el cual activa la camara web para poder hacer deteccion de video sobre un video **"en vivo"** (REC 🔴)
```
python deteccion_video.py
```
# 6. Correr el de detector de objetos en un Video.mp4 

## IMPORTANTE ‼️

En la carpeta **Video-Transito** se muestran videos de ejemplo (en baja calidad debido a que no se puede subir videos de más de 100 Mb), pero ustedes pueden descargar el video que deseen y de igual forma servirá (formato **MP4**). Eso si, tienen que colocar dicho video dentro de la carpeta **Deteccion-Objetos**.

Si en vez de correr detección de objetos sobre la webcam lo que quieres es correr el modelo sobre un video ya pre grabado **(video.mp4)**, tienes que cambiar el comando para correr el codigo a:
```
python deteccion_video.py --webcam 0 --directorio_video <directorio_al_video.mp4>
```
