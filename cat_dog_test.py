from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

# load trained data
model = load_model("cat_dog_model.h5")

# load image
img=image.load_img(r"C:\Users\DELL\Desktop\DESKTOP\Nextgenpro\DL\cat_dog_cnn\archive\train\images\cat\cat_355.jpg",
                   target_size=(150,150))
img=image.img_to_array(img)
img=img/255.0
img=np.expand_dims(img,axis=0)



result=model.predict(img)
print(result)  # predict


# output
# if result[0][0] > 0.5:
#     print("Dog")
# else:
#     print("Cat")

# Updated Output Logic
if result[0][0] > 0.5:
    print(f"Prediction: Dog ({result[0][0]:.2f})")
else:
    print(f"Prediction: Cat ({result[0][0]:.2f})")