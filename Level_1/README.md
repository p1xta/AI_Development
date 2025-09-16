Задание уровня 1 - Обнаружение кругов с помощью преобразования Хафа.

Программа сохраняет выбранное изображение с нарисованными кругами, найденными с помощью cv2.HoughCircles с помощью функции `find_circles()`.
1. С помощью cv2.Canny находятся грани на изображении
2. Далее cv2.HoughCircles находит круги
3. После этого круги рисуются на исходном черно-белом изображении

Использование:
1. Clone the repository:
` git clone `

2. Go to Level_1 task folder:
`cd Level_1`

3. Install requirements: 
`pip install -r requirements.txt`

4. Run CV-1-09.py script:
`python CV-1-09.py --img_path path/to/your/input/image.png --img_output_path path/to/your/output/image.png`
