import requests
import matplotlib.pyplot as plt

from PIL import Image


CAMERA_ADDRESS = 'http://192.168.0.31:8080'

class Camera:

    def __init__(self):
        
        plt.ion()
        plt.show()

    def zoom(self, zoom_number):
        if zoom_number < 0 or zoom_number > 30:
            print('Wrong zoom number.')
            return
        requests.get(CAMERA_ADDRESS + f'/ptz?zoom={zoom_number}')

    def disable_torch(self):
        requests.get(CAMERA_ADDRESS + '/disabletorch')

    def enable_torch(self):
        requests.get(CAMERA_ADDRESS + '/enabletorch')

    def get_image(self):
        # get image from camera
        try:
            command = '/photo.jpg'
            image_path = 'tmp_images/image.png'
            resp = requests.get(CAMERA_ADDRESS + command)

            # save the image locally
            with open(image_path, 'wb') as image_file:
                image_file.write(resp.content)
        except:
            print('Something went wrong during image downloading.')
            return

        # draw the image
        with Image.open(image_path) as img:
                plt.imshow(img)
                plt.draw()
                plt.pause(2)
        print('The new image has dropped!')