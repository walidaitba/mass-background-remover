import os
from rembg import remove

input_folder = 'input_folder'
output_folder = 'output_folder'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

counter = 0

for filename in os.listdir(input_folder):
    if counter == 2500:
        break

    input_path = os.path.join(input_folder, filename)
    output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + '.png')

    with open(input_path, 'rb') as i:
        with open(output_path, 'wb') as o:
            input_data = i.read()
            output_data = remove(input_data)
            o.write(output_data)

    counter += 1
