

## <h2 style="color: #5697bf;"><u>Icon</u></h2>

<span style="color: #888;">Class</span>

**Inherits from: _object_**

Icon.

```python
__init__(
            self,
            path: str = 'document-new',
            fallback_path: str = 'document-new',
            width: int = 22,
            height: int = 22,
            *args, **kwargs) -> None:
```

Class constructor.

The icon is rendered from the path of a passed file, or from the name 
of an icon in the current operating system, such as 

### <h2 style="color: #5e5d84;">Properties</h2>

#### height

**_int_**

Returns the height of the Icon.

Pass a new integer value to update the height.


#### path

**_str_**

Icon path.

Pass a new path to update the icon image.


#### width

**_int_**

Returns the Widget width.

Pass a new integer value to update the width.


#### _obj

Direct access to Qt classes.

Warning: Direct access is discouraged and may break the project. 
This access is considered a hacking for complex Qt implementations, 
and should only be used for testing and analysis purposes.


---