from mainLogic import split_and_process_files
import os

def main():
    # Определяем пути для входной и выходной папок
    input_directory = os.path.join(os.getcwd(), 'input')  # Папка с файлами
    output_directory = os.path.join(os.getcwd(), 'output')  # Директория для сохранения частей

    # Вызываем функцию с относительными путями
    split_and_process_files(input_directory, output_directory, part_size=1024 * 5)

if __name__ == "__main__":
    main()
