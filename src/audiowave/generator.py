from typing import List
from pydub import AudioSegment
import numpy as np
from PIL import Image, ImageDraw

def generate_amplitudes(src) -> List[int]:
    """
    Generates the audio volume amplitudes per second.
    returns a list containing numbers from 0 to 100 with a length of the audio seconds
    """
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


def get_waveform_image(
    src,
    image_format="png",
    max_height=50,
    line_color=(255, 255, 255),
    bg_color=(255, 255, 255, 0),
    show=False,
) -> Image:
    """
    Creates an waveform image from the audio file.
    """
    LINE_WIDTH = 3
    LINE_MARGIN = 1

    if len(bg_color) == 4:
        assert (
            image_format == "png"
        ), "Only PNG supports RGBA backgrounds, use image_format='png'"

    if image_format.lower() == "jpg":
        # PIL doesn't support JPG
        image_format = "JPEG"

    amplitudes = generate_amplitudes(src)
    center_y = round(max_height / 2)

    # normalizing the amplitudes for the custom image height
    max_amp = max(amplitudes)
    amplitudes = list(map(lambda x: round((x * max_height) / max_amp), amplitudes))
    image_width = len(amplitudes) * LINE_WIDTH
    image_size = (image_width, max_height)
    image_mode = "RGBA" if len(bg_color) == 4 else "RGB"

    im = Image.new(image_mode, image_size, bg_color)
    draw = ImageDraw.Draw(im)

    x = 1
    for n in amplitudes:
        # waves are aligned from the center
        start_y = round(center_y + (n / 2))
        end_y = round(center_y - (n / 2))

        coords = (x, start_y, x, end_y)
        draw.line(coords, fill=line_color, width=LINE_WIDTH - LINE_MARGIN)
        x += LINE_WIDTH

    name = src.split("/")[-1].split(".")[0] + "_waveform"
    path = f"{name}.{image_format}"
    im.save(path, image_format)
    if show:
        im.show()
    return im