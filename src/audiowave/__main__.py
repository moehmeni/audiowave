import sys
import os

# add audiowave to the path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

if __name__ == "__main__":
    from audiowave import get_waveform_image
    import argparse

    parser = argparse.ArgumentParser(
        description="Generate waveform images from audio files"
    )
    parser.add_argument(
        "audio_path", help="The audio file path to generate the waveform from"
    )
    parser.add_argument(
        "--max_height",
        help="The maximum height of the waveform image",
        default=50,
    )
    parser.add_argument(
        "-c",
        "--wave_color",
        help="The color of the waveform lines",
        default="255,255,255",
    )
    parser.add_argument(
        "-b", "--bg_color", help="The color of the background", default="transparent"
    )
    parser.add_argument("-f", "--format", help="The image format", default="png")
    parser.add_argument("--show", help="Show the image", action="store_true")
    args = parser.parse_args()

    # Coverting the color string to a tuple
    if args.bg_color == "transparent":
        args.bg_color = (255, 255, 255, 0)
    else:
        args.bg_color = tuple(map(int, args.bg_color.split(",")))

    if args.wave_color:
        args.wave_color = tuple(map(int, args.wave_color.split(",")))

    get_waveform_image(
        args.audio_path,
        args.format,
        args.max_height,
        args.wave_color,
        args.bg_color,
        args.show,
    )
