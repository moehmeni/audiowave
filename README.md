# audiowave
 Generate waveform images from audio files

 <img src="https://beatly-video.s3.ir-thr-at1.arvanstorage.com/test_waveform.png" />


## Installation
```
git clone https://github.com/mdmomeni/audiowave
```
## Usage
```
python3 src/audiowave test.mp3 --wave_color 89,201,54
```
<sub>test_waveform.png</sub>

 <img src="https://beatly-video.s3.ir-thr-at1.arvanstorage.com/test_waveform_green.png" />

### Other options
```
usage: audiowave [-h] [--max_height MAX_HEIGHT] [-c WAVE_COLOR] [-b BG_COLOR] [-f FORMAT] [--show] audio_path

Generate waveform images from audio files

positional arguments:
  audio_path            The audio file path to generate the waveform from

optional arguments:
  -h, --help            show this help message and exit
  --max_height MAX_HEIGHT
                        The maximum height of the waveform image
  -c WAVE_COLOR, --wave_color WAVE_COLOR
                        The color of the waveform lines
  -b BG_COLOR, --bg_color BG_COLOR
                        The color of the background
  -f FORMAT, --format FORMAT
                        The image format
  --show                Show the image
```
### Usage in Python program
```python
from audiowave import get_waveform_image

get_waveform_image("test.mp3", wave_color = (89, 201, 54))
```

**Feel free to create any issue or PR**