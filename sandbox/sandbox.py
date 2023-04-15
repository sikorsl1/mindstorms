# import requests
# import matplotlib.pyplot as plt

# from PIL import Image


# CAMERA_ADDRESS = 'http://192.168.0.31:8080'

# def zoom(zoom_number):
#     if zoom_number < 0 or zoom_number > 30:
#         print('Wrong zoom number.')
#         return
#     requests.get(CAMERA_ADDRESS + f'/ptz?zoom={zoom_number}')

# def disable_torch():
#     requests.get(CAMERA_ADDRESS + '/disabletorch')

# def enable_torch():
#     requests.get(CAMERA_ADDRESS + '/enabletorch')

# def get_image(plot_context):
#     # get image from camera
#     try:
#         command = '/photo.jpg'
#         image_path = 'images/image.png'
#         resp = requests.get(CAMERA_ADDRESS + command)

#         # save the image locally
#         with open(image_path, 'wb') as image_file:
#             image_file.write(resp.content)
#     except:
#         print('Something went wrong during image downloading.')
#         return

#     # draw the image
#     with Image.open(image_path) as img:
#             plot_context.imshow(img)
#             plot_context.draw()
#             plot_context.pause(2)
#     print('The new image has dropped!')

def main():

    camera = camera.Camera()

    supported_commands = ['go', 'get image', 'exit', 'help', 'unroll', 'roll up', 'torch on', 'toch off', 'zoom']

    plt.ion()
    plt.show()

    while True:
        input_command = input('Input the command: ')
        if input_command == "go":
            print('Jazda z kurwami.')
        elif input_command == "unroll":
            print('Unrolling.')
        elif input_command == "roll up":
            print('Rolling up.')
        elif input_command == "get image":
            camera.get_image(plt)
        elif input_command == 'torch on':
            camera.enable_torch()
        elif input_command == 'torch off':
            camera.disable_torch()
        elif 'zoom' in input_command:
            camera.zoom(int(input_command.split()[1]))
        elif input_command == "exit":
            print('Goodbye.')
            break
        elif input_command == 'help':
            print(f'The following commands are supported: {"".join([command + ", " for command in supported_commands])}')
        else:
            print("I don't understant the command :/")

if __name__ == "__main__":
    main()
