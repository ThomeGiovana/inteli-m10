from flask import Flask, request, jsonify
from PIL import Image
import io
import numpy as np
from d2l import torch as d2l
import torch

app = Flask(__name__)

def get_net():
    num_classes = 10
    net = d2l.resnet18(num_classes, 3)
    return net

def RunPrediction(img):
    model = get_net()
    model.load_state_dict(torch.load('pond_CIFAR-10/cifar10_model2024-05-27 01_13_44.746601.pth'))
    model.eval()  # Coloque o modelo em modo de avaliação
    with torch.no_grad():
        output = model(img)
        _, predicted = torch.max(output, 1)
    return predicted

def get_class_name(class_idx):
    class_names = [
        "airplane",
        "automobile",
        "bird",
        "cat",
        "deer",
        "dog",
        "frog",
        "horse",
        "ship",
        "truck"
    ]
    return class_names[class_idx]


@app.route('/', methods=['GET'])
def AppGet():
    return 'API running'

@app.route('/predict', methods=['POST'])
def Predic():
    if 'image' not in request.files:
        return 'Unnable to make prediction: you have to send an image'
    file = request.files['image']
    if file.filename == '':
        return 'File must contain a name'
    image = np.array(Image.open(io.BytesIO(file.read())))

    # Pré-processamento da imagem para o formato esperado pelo modelo
    transform = d2l.transforms.ToTensor()
    image = transform(image).unsqueeze(0)  # Adiciona uma dimensão para o batch

    prediction = RunPrediction(image)
    result = get_class_name(prediction.item())
    return result

if __name__ == '__main__':
    app.run()
