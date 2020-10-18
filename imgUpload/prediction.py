from keras.applications.resnet50 import ResNet50
from keras.preprocessing import image
from keras.applications.resnet50 import preprocess_input, decode_predictions
import numpy as np


def find():
    model = ResNet50(weights='imagenet')

    img = image.load_img('userimages/img.jpg', target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)

    preds = model.predict(x)

    html = decode_predictions(preds, top=3)[0]
    result = []
    for e in html:
        result.append((e[1], np.round(e[2] * 100, 2)))

    return result
