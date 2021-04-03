import os
import Foto

continue_script = True
path_to_pictures = input("Specify the folder with photos: ")
ind = input("Do you want to proceed with all photos? y/n ")
if ind == "n":
    for idx, f in enumerate(os.listdir(path_to_pictures)):
        print(f'{idx}. {f}')
    ind_list = list(map(int, input("Specify indexes of desired photos (ex.: 0 1 3): ").split()))
else:
    ind_list = None


save = input("Save result to the same folder? y/n ")
if save == "n":
    path_to_save = input("Specify the folder where to save result: ")
else:
    path_to_save = path_to_pictures


if os.path.exists(path_to_save + 'result.jpg'):
    result_exists = input("File result.jpg already exists. Do you want to rewrite it? y/n ")
    if result_exists == 'n':
        continue_script = False
        print('Stop executing. Default name for the collage is "result.jpg"')


if continue_script:
    Foto.collage(path_to_pictures, path_to_save, ind_list)
    print(f"File 'result.jpg' is saved to {path_to_save}")

