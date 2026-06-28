# Image Corruptor

A simple Python script that intentionally corrupts image files by modifying their binary data.

## Features

* Supports JPG, JPEG, and PNG images.
* Corrupts the file signature.
* Randomly modifies a portion of the image data.
* Adds random byte noise.
* Saves the corrupted images to a separate `corrupted_images` folder.
* Keeps the original images unchanged.

## How It Works

The script scans the current directory for supported image files, applies several random binary modifications to each image, and saves the corrupted versions into the output folder.

## Disclaimer

This project is intended for experimentation and educational purposes only. The generated files will be unreadable.

---

# Image Corruptor

Простой Python-скрипт, который намеренно повреждает файлы изображений, изменяя их бинарные данные.

## Возможности

* Поддержка изображений JPG, JPEG и PNG.
* Повреждение сигнатуры файла.
* Случайное изменение части данных изображения.
* Добавление случайного бинарного шума.
* Сохранение поврежденных файлов в папку `corrupted_images`.
* Оригинальные изображения остаются без изменений.

## Как это работает

Скрипт сканирует текущую папку на наличие поддерживаемых изображений, применяет к каждому несколько случайных бинарных изменений и сохраняет поврежденные версии в отдельную папку.

## Примечание

Проект предназначен для экспериментов и образовательных целей. Полученные файлы будут нечитаемыми.
