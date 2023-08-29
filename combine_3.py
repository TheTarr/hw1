from PIL import Image
import os

def combine_images(image_paths):
    images = [Image.open(path) for path in image_paths]
    image_width, image_height = images[0].size

    total_width = image_width * 3
    total_height = image_height * ((len(images) + 2) // 3)  # Calculate the number of rows needed

    combined_image = Image.new('RGB', (total_width, total_height))

    x_offset = 0
    y_offset = 0

    for img in images:
        combined_image.paste(img, (x_offset, y_offset))

        x_offset += image_width
        if x_offset >= total_width:
            x_offset = 0
            y_offset += image_height

    return combined_image

if __name__ == "__main__":
    # path
    dir_path = './sample_images'

    # get all picture from that path
    files = [os.path.join(dir_path, file) for file in os.listdir(dir_path)]
    file_names = []
    for file in files:
        # file_names.append('sample_images/'+file[16:])
        # file_names.append('grey_enhanced/'+file[16:])
        # file_names.append('hsv_enhanced/'+file[16:])

        file_names = ['sample_images/'+file[16:], 'grey_enhanced/'+file[16:], 'hsv_enhanced/'+file[16:]]  # File names without extensions
        image_paths = [f"./{name}" for name in file_names]  # Adjust the extensions accordingly

        combined_image = combine_images(image_paths)
        combined_image.show()  # Display the generated image
        combined_image.save("combined_image"+file[16:])  # Save the generated image