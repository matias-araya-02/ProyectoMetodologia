device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

os.makedirs("output", exist_ok=True)

# Configuración del modelo
model = Darknet(opt.model_def, img_size=opt.img_size).to(device)

if opt.weights_path.endswith(".weights"):
    model.load_darknet_weights(opt.weights_path)
else:
    model.load_state_dict(torch.load(opt.weights_path))

model.eval()  # Modo de evaluación

dataloader = DataLoader(
    ImageFolder(opt.image_folder, img_size=opt.img_size),
    batch_size=opt.batch_size,
    shuffle=False,
    num_workers=opt.n_cpu,
)

classes = load_classes(opt.class_path)  # Cargar las etiquetas de clase

Tensor = torch.cuda.FloatTensor if torch.cuda.is_available() else torch.FloatTensor

imgs = []  # Lista de rutas de imágenes
img_detections = []  # Lista de detecciones de imágenes

print("\nRealizando detección de objetos:")
prev_time = time.time()
for batch_i, (img_paths, input_imgs) in enumerate(dataloader):
    # Configurar la entrada
    print("INPUT_IMGS-----", input_imgs)
    input_imgs = Variable(input_imgs.type(Tensor))

    # Detecciones
    with torch.no_grad():
        detections = model(input_imgs)
        detections = non_max_suppression(detections, opt.conf_thres, opt.nms_thres)

    # Guardar en el registro
    current_time = time.time()
    inference_time = datetime.timedelta(seconds=current_time - prev_time)
    prev_time = current_time
    print("\t+ Lote %d, Tiempo de inferencia: %s" % (batch_i, inference_time))

    # Guardar la imagen y las detecciones
    imgs.extend(img_paths)
    img_detections.extend(detections)

# Colores para las cajas delimitadoras
cmap = plt.get_cmap("tab20b")
colors = [cmap(i) for i in np.linspace(0, 1, 20)]

print("\nGuardando imágenes:")
# Iterar a través de las imágenes y guardar la representación gráfica de las detecciones
for img_i, (path, detections) in enumerate(zip(imgs, img_detections)):
    print("(%d) Imagen: '%s'" % (img_i, path))

    # Crear la representación gráfica
    img = np.array(Image.open(path))
    plt.figure()
    fig, ax = plt.subplots(1)
    ax.imshow(img)

    # Dibujar las cajas delimitadoras y etiquetas de las detecciones
    if detections is not None:
        # Reescalar las cajas al tamaño de la imagen original
        detections = rescale_boxes(detections, opt.img_size, img.shape[:2])
        unique_labels = detections[:, -1].cpu().unique()
        n_cls_preds = len(unique_labels)
        bbox_colors = random.sample(colors, n_cls_preds)
        for x1, y1, x2, y2, conf, cls_conf, cls_pred in detections:
            print("\t+ Etiqueta: %s, Confianza: %.5f" % (classes[int(cls_pred)], cls_conf.item()))

            box_w = x2 - x1
            box_h = y2 - y1

            color = bbox_colors[int(np.where(unique_labels == int(cls_pred))[0])]
            # Crear un parche de rectángulo (Rectangle patch)
            bbox = patches.Rectangle((x1, y1), box_w, box_h, linewidth=2, edgecolor=color, facecolor="none")
            # Añadir la caja delimitadora a la representación gráfica
            ax.add_patch(bbox)
            # Añadir etiqueta
            plt.text(
                x1,
                y1,
                s=classes[int(cls_pred)],
                color="white",
                verticalalignment="top",
                bbox={"color": color, "pad": 0},
            )

    # Guardar la imagen generada con las detecciones
    plt.axis("off")
    plt.gca().xaxis.set_major_locator(NullLocator())
    plt.gca().yaxis.set_major_locator(NullLocator())
    filename = path.split("/")[-1].split(".")[0]
    plt.savefig(f"output/{filename}.png", bbox_inches="tight", pad_inches=0.0)
    plt.close()
