import os
import cv2
import numpy as np
import matplotlib.pyplot as plt


DILATE_ITERS = 1
KERNEL_SIZE = 3

def load_img(file_path):
    """
    Функция проверяет, существует ли файл по указанному пути;
    пытается загрузить изображение с помощью OpenCV в цвете (BGR);
    проверяет, успешно ли загружено изображение;
    возвращает загруженное изображение в виде массива NumPy.

    :param file_path: путь к файлу
    :return: image - изображение
             None - если файл не найден или загрузка не удалась.
    """

    if not os.path.exists(file_path):
        print("Error: file not found\n")
        return None

    image = cv2.imread(file_path, cv2.IMREAD_COLOR)

    if image is None:
        print("Error: the image was not uploaded\n")
        return None

    return image


def brg_to_hsv(image):
    """
        Функция преобразует изображение из цветовой модели BRG в HSV

        :param image: изображение в BRG
        :return: image_hsv - изображение в HSV
    """
    return cv2.cvtColor(image, cv2.COLOR_BGR2HSV)


def create_mask(image_hsv, lower_color_green = np.array([35, 40, 40]),
                upper_color_green = np.array([85, 255, 255]), kernel_size=(KERNEL_SIZE, KERNEL_SIZE)):
    """
        Создает инвертированную маску для заданного изображения в цветовом пространстве HSV.

        :param image_hsv: Изображение в формате HSV
        :param lower_color_green: Нижняя граница диапазона цвета.
            Используется для выделения областей, которые нужно замаскировать.
        :param upper_color_green: Верхняя граница диапазона цвета
        :param kernel_size: Размер структурного элемента для морфологических операций.
            Чем больше ядро, тем сильнее "зачищаются" шумы и закрываются дырки.
        :return: inv_mask - бинарная инвертированная маска,
        где зеленые области из исходного изображения черные,
        а все остальное белое.
    """

    mask_ = cv2.inRange(image_hsv, lower_color_green, upper_color_green)
    inv_mask = cv2.bitwise_not(mask_)

    # kernel = np.ones(kernel_size, np.uint8)

    # inv_mask = cv2.morphologyEx(inv_mask, cv2.MORPH_OPEN, kernel) # даление шумов
    # inv_mask = cv2.dilate(inv_mask, kernel, iterations=DILATE_ITERS) # расширение маски

    return inv_mask


def final_img(image, mask_, f_res):
    """
    Применяет маску к изображению, сохраняет результат и отображает его.

    :param image: исходное изображение в формате BGR
    :param mask_: бинарная маска, применяемая к изображению
    :param f_res: путь и имя файла для сохранения результата
    """

    result = cv2.bitwise_and(image, image, mask=mask_)

    cv2.imwrite(f_res, result)
    result = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)

    plt.imshow(result)
    plt.show()


if __name__ == "__main__":
    file_input = input("Enter input image path: ")
    file_output = input("Enter output image path: ")

    img = load_img(file_input)

    img_hsv = brg_to_hsv(img)
    mask = create_mask(img_hsv)
    final_img(img, mask, file_output)
