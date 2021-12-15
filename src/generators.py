from pydub import AudioSegment
import numpy as np
import uuid
from PIL import Image, ImageDraw
import os


def audio_amplitudes(src):
    audio = AudioSegment.from_file(src)
    bars = int(audio.duration_seconds)
    file_bytes = audio._data
    data = np.frombuffer(file_bytes, np.int16)
    length = len(data)
    bucket_count = round(length / bars)
    highest_amp = max(data)
    amplitudes = []
    for i in range(bars):
        i += 1
        start = (i - 1) * bucket_count
        end = (i * bucket_count) - 1
        bucket_bytes = data[start:end]
        bucket_max_number = round((max(bucket_bytes) * 100) / highest_amp)
        amplitudes.append(bucket_max_number)
    return amplitudes


def image_from_amplitudes(
    amplitudes, max_height=50, line_colors=(255, 255, 255), bg_color=(255, 255, 255, 1)
):
    LINE_WIDTH = 3
    LINE_MARGIN = 1

    center_y = round(max_height / 2)

    # normalizing the amplitudes for the custom image height
    max_amp = max(amplitudes)
    amplitudes = list(map(lambda x: round((x * max_height) / max_amp), amplitudes))

    im = Image.new("RGBA", (len(amplitudes) * LINE_WIDTH, max_height), bg_color)
    draw = ImageDraw.Draw(im)
    
    x = 1
    for n in amplitudes:
        # waves are aligned from the center
        start_y = round(center_y + (n / 2))
        end_y = round(center_y - (n / 2))

        coords = (x, start_y, x, end_y)
        draw.line(coords, fill=line_colors, width=LINE_WIDTH - LINE_MARGIN)
        x += LINE_WIDTH

    ex = "png"
    name = f"{str(uuid.uuid4()).replace('-' , '')}.{ex}"
    im.save(os.path.join("waves", name), ex)
    im.show()


src = "Billie Eilish - Bad Guy.mp3"
image_from_amplitudes(audio_amplitudes(src), max_height=50)
