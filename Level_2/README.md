Задание уровня 2 - Улучшение удаления фона с добавлением бинаризации и морфологических операций (на основе CV-1-16).

Программа сохраняет выбранное изображение с удалённым зелёным фоном с помощью функций `create_mask()` и `final_img()`.

С помощью преобразования `cv2.cvtColor` изображение переводится в HSV.

Затем по заданным диапазонам `lower_color_green` и `upper_color_green` создаётся бинарная маска (`cv2.inRange`).

Маска очищается от шумов при помощи морфологической операции opening (`cv2.morphologyEx`).

Маска расширяется с помощью dilation (`cv2.dilate`), чтобы лучше захватить границы объектов.

Итоговая маска применяется к исходному изображению (`cv2.bitwise_and`), и результат сохраняется и отображается.

Использование:
1. Clone the repository:
```
git clone
```

2. Go to Level_2 task folder:
```
cd Level_2
```

3. Install requirements: 
```
pip install -r requirements.txt
```

4. Run CV-2-06.py script:
```
python CV-2-06.py
```
5. Enter input and output files.