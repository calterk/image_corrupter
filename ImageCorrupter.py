import os
import random

INPUT_DIR = "."
OUTPUT_DIR = "corrupted_images"

os.makedirs(OUTPUT_DIR, exist_ok=True)

def corrupt_image(path, out_path):
    with open(path, "rb") as f:
        data = bytearray(f.read())

    if len(data) < 100:
        return  #too small file

    # signature corrupt
    data[0] = random.randint(0, 255)
    data[1] = random.randint(0, 255)

    # body corrupt
    start = random.randint(50, len(data)//2)
    end = min(start + random.randint(50, 200), len(data))

    for i in range(start, end):
        data[i] = random.randint(0, 255)

    # noize
    for _ in range(50):
        idx = random.randint(0, len(data) - 1)
        data[idx] = random.randint(0, 255)

    # save
    with open(out_path, "wb") as f:
        f.write(data)


for filename in os.listdir(INPUT_DIR):
    if filename.lower().endswith((".jpg", ".jpeg", ".png")):
        input_path = os.path.join(INPUT_DIR, filename)
        output_path = os.path.join(OUTPUT_DIR, filename)

        try:
            corrupt_image(input_path, output_path)
            print(f"Corrupted: {filename}")
        except Exception as e:
            print(f"Error with {filename}: {e}")
