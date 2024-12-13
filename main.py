from logger import logger
from fastapi import FastAPI
import uvicorn
from PIL import Image
import torch
import numpy as np
from numpy.linalg import norm
# Load model directly
import timm
from transformers import AutoImageProcessor, AutoModelForImageClassification, AutoModel, SwinModel, SwinConfig, \
    AutoConfig
import config as cnf

from src.routes.routes import router


app = FastAPI()
app.include_router(router)

if __name__ == '__main__':
    logger.info("Fast API application running on port: %s and host: %s", cnf.port, cnf.host)
    # uvicorn.run(app='main:app', port=int(cnf.port),host=cnf.host)
    processor1 = AutoImageProcessor.from_pretrained("microsoft/swin-tiny-patch4-window7-224")
    model1 = AutoModelForImageClassification.from_pretrained("microsoft/swin-tiny-patch4-window7-224")
    # torch.save(model1.state_dict(), f"routes/FE-swin.pt")
    # processor = AutoImageProcessor.from_pretrained("routes/preprocessor_config.json")
    # model = AutoModel.from_pretrained("routes/config.json")
    img = Image.open('/home/rahul/Documents/pytest-learning/signature (1).jpg')
    # inputs = processor(images=img, return_tensors="pt")
    # outputs = model(**inputs)
    # p = outputs.pooler_output.tolist()
    # print(outputs)
    # print(len(p[0]))
    # logger.info("original model")
    inputs = processor1(images=img, return_tensors="pt")
    outputs = model1(**inputs)
    A = outputs.logits[0].tolist()
    print(len(outputs.logits[0].tolist()))
    # logger.info("original model")
    # # p = outputs.pooler_output.tolist()
    # print(outputs)
    # # print(len(p[0]))
    # logits = outputs.logits
    # sizes = [224, 224, 224, 384]
    # num_heads = [[3, 6, 12, 24]]
    # depths = [[2, 2, 6, 2]]
    # embed_dims = [96]
    # window_sizes = [7]
    processor = AutoImageProcessor.from_pretrained("routes/preprocessor_config.json")
    config = AutoConfig.from_pretrained('routes/config.json')
    print(config)
    # config = SwinConfig(image_size=sizes[0], depths=depths[0],
    #                     embed_dim=embed_dims[0], num_heads=num_heads[0],
    #                     window_size=window_sizes[0])
    # model = SwinModel(config)
    model = AutoModelForImageClassification.from_config(config)
    # print(model)
    #
    model.load_state_dict(torch.load('routes/FE-swin.pt'))
    img = Image.open('/home/rahul/Documents/pytest-learning/signature (1).jpg')
    inputs = processor(images=img, return_tensors="pt")
    outputs = model(**inputs)
    B = outputs.logits[0].tolist()
    # print(outputs.logits)
    print(len(outputs.logits[0].tolist()))
    # # config = SwinConfig.from_pretrained('microsoft/swin-tiny-patch4-window7-224')
    # # model = SwinModel(config)
    # # print(len(logits[0]))
    # # model = timm.create_model('swin_tiny_patch4_window7_224', pretrained=False)
    # # # model = torch.load('routes/pytorch_model.bin', weights_only=False)
    # # model = model.load_state_dict(torch.load('routes/FE-swin.pt'))
    # print(model.eval())
    # model = AutoModel.from_pretrained('/home/rahul/Downloads/tf_model.h5')
    cosine = np.dot(A, B) / (norm(A) * norm(B))
    print("Cosine Similarity:", cosine)
    # model.save_pretrained('routes/', safe_serialization=False)
    print("qwerty")



