# dem-generator: Shitcode Edition
A simple shitcode-lib for creating demotivators

**Install:**
```
git clone https://github.com/bluepanee/dem-generator
```
```
cd dem-generator
```
```
python setup.py install
```

**Usage:**
```python
import dem_generator
from PIL import Image

img = Image.open("test.jpg")
dem = dem_generator.Generator()

top_text = "Top text"
bottom_text = "Bottom text"
copyright_ = "@welcomeza"
min_size, max_size = 720, 720

result = dem.create(img, top_text, bottom_text, copyright_, min_size, max_size)
result.show()
```
