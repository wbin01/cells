

## <h2 style="color: #4d7c99;">CheckButton</h2>


**Inherits from: _Widget_**

Check Button Widget.


### Signature

```python
__init__(
            self,
            text: str = None,
            value: any = None,
            selected: bool = False,
            orientation: Orientation = Orientation.HORIZONTAL,
            *args, **kwargs) -> None:
```

Class constructor.
  
  
**:param text:** CheckButton text label.
  
**:param selected:** True to start already selected.
  
**:param value:** Value of any type to capture as an identifier.
  


### Properties


#### text

```python
text(self) -> str:
```

Button text.
  
  Pass a new string to update the text.
  

#### selected

```python
selected(self) -> bool:
```

If Widget is selected.

  Use True or False to select or deselect the widget.
  

#### value

```python
value(self) -> any:
```

Button value.
  
  Pass a new value to update.
  
