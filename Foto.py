import os
import math
from PIL import Image

# cat = Image.open('zophie.png')
# print(cat.size)
# cat.save('zophie.jpg')
# crop_im = cat.crop((335, 345, 565, 560))
# crop_im.save('cropped.png')
# cat_copy = cat.copy()
# cat_copy.paste(crop_im, (0, 0))
# cat_copy.save('pasted.png')
#
# w, h = cat.size
# quarter_cat = cat.resize((int(w / 2), int(h / 2)))
# quarter_cat.save('quarter.png')
#
# cat.rotate(90).save('rotated90.png')
# cat.rotate(10, expand=True).save('rotated10expand.png')
#
# cat.transpose(Image.FLIP_LEFT_RIGHT).save('horizflip.png')

# read imgs and save to one list

def read_imgs(path_dir, img_indexes=None):
    all_img = []
    for filename in os.listdir(path_dir):
        im = Image.open(path_dir+filename)
        all_img.append(im)

    if img_idnexes is not None:
        all_img_ind = []
        for el in img_idnexes:
            all_img_ind.append(all_img[el])
        return all_img_ind

    return all_img

# all = read_imgs('C:/Projects/Pictures/')
# for one in all:
#     print(one.size)


# convert all imgs to square accorging to biggest size
def make_all_square(list_imgs):
    list_imgs_copy = list_imgs
    for i in range(len(list_imgs)):
        width, height = list_imgs[i].size
        if width != height:
            sq_size = max(width, height)
            # create new white image
            new_img = Image.new("RGB", (sq_size, sq_size), (255, 255, 255, 0))
            if width > height:
                new_img.paste(list_imgs_copy[i], (0, (sq_size - height)//2))
            else:
                new_img.paste(list_imgs_copy[i], ((sq_size - width)//2, 0))

            list_imgs_copy[i] = new_img

    return list_imgs_copy


# new_all = make_all_square(all)
# for one in new_all:
#     print(one.size)


# create A4 empty picture (3508 x 2480) - ~15 pxls frame
def new_A4():
    return Image.new("RGB", (2480 - 15, 3508 - 15), (255, 255, 255))

# calculate the size of the squares according to number of pictures: sqrt(number_of_pictures) - number of img in a row -> width = height
def picture_size(n_pict):
    w_A4 = (2480 - 15)
    im_in_row = math.ceil(math.sqrt(n_pict))  # ceil to get max number
    size = w_A4 // im_in_row
    return round(size)

# print(picture_size(15))

# resize all pictures to one size (given one)
def resize_all(list_imgs, size):
    list_imgs_copy = list_imgs
    for i in range(len(list_imgs_copy)):
        list_imgs_copy[i] = list_imgs_copy[i].resize((size, size))
    return list_imgs_copy

# all = read_imgs('C:/Projects/Pictures/')
# new_all = make_all_square(all)
# s = picture_size(len(new_all))
# res_all = resize_all(new_all, s)
# for k in res_all:
#     print(k.size)


# place pictures to the empty A4
def combine_all(A4, list_imgs):
    width_p, height_p = list_imgs[0].size
    width_A4, height_A4 = A4.size

    im_row = math.ceil(math.sqrt(len(list_imgs)))
    im_col = math.ceil(len(list_imgs)/im_row)
    k = 0
    # forleft point in range width A4 with step of picture size
    for top in range(0, height_p * im_row, height_p):
        for left in range(0, width_p * im_col, width_p):
            if k >= len(list_imgs):
                break
            A4.paste(list_imgs[k], (left, top))
            k += 1

    return A4

# all = read_imgs('C:/Projects/Pictures/')
# new_all = make_all_square(all)
# s = picture_size(len(new_all))
# res_all = resize_all(new_all, s)
# result = combine_all(new_A4(), res_all)
# result.save("resA4.jpg")


# all = read_imgs('C:/Projects/Pictures/', [0, 2, 3, 7])
# new_all = make_all_square(all)
# s = picture_size(len(new_all))
# res_all = resize_all(new_all, s)
# result = combine_all(new_A4(), res_all)
# result.save("C:/Projects/Pictures/resA4indexes.jpg")
# print(result.size)

def collage(path_to_folder, path_to_save, ind_list=None):
    img_list = read_imgs(path_to_folder, ind_list)
    sq_imgs = make_all_square(img_list)
    size = picture_size(len(sq_imgs))
    resized_imgs = resize_all(sq_imgs, size)
    result = combine_all(new_A4(), resized_imgs)
    result.save(path_to_save+"result.jpg")

# collage('C:/Projects/Pictures/', 'C:/Projects/Pictures/')

# read_imgs(path_dir, img_inexes=None)
# make_all_square(list_imgs)
# new_A4()
# picture_size(n_pict)
# resize_all(list_imgs, size)
# combine_all(A4, list_imgs)






