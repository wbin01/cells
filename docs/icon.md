

## <h2 style="color: #4d7c99;">Icon</h2>


**Inherits from: _object_**

Icon.


### Signature

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


### Properties


#### height

```python
height(self) -> int:
```

Returns the height of the Icon.

  Pass a new integer value to update the height.
  

#### path

```python
path(self) -> str:
```

Icon path.

  Pass a new path to update the icon image.
  

#### width

```python
width(self) -> int:
```

Returns the Widget width.

  Pass a new integer value to update the width.
  

#### _obj

```python
_obj(self):
```

Direct access to Qt classes.

  Warning: Direct access is discouraged and may break the project. 
  This access is considered a hacking for complex Qt implementations, 
  and should only be used for testing and analysis purposes.
  
