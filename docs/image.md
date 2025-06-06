

## <h2 style="color: #5697bf;"><u>Image</u></h2>

<span style="color: #888;">Class</span>

**Inherits from: _Widget_**

Image Widget.

```python
__init__(
            self,
            path: str = None,
            width: int = None,
            height: int = None,
            aspect_ratio: bool = True,
            smooth: bool = False,
            *args, **kwargs) -> None:
```

Class constructor.

The Image is rendered from the path of a passed file.



**:param path:** 
Image path or Icon() object.


**:param width:** 
Integer with the value of the image width.


**:param height:** 
Integer with the value of the image height.


**:param aspect_ratio:** 
Flattening or stretching the image with width or height values not 
equivalent to the original image. True will maintain the aspect 
ratio without distorting or stretching.


**:param smooth:** 
It improves the appearance of scaled images, but the processing is 
a little slower.


### <h2 style="color: #5e5d84;">Properties</h2>

#### path

**_str_**

Image path.

Pass a new path to update the Image.


---