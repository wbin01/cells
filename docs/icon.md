# Icon
Inherits from: object
Icon.
## Constructor signature
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
