

## <h2 style="color: #4d7c99;">Application</h2>


**Inherits from: _object_**

Application manager.

 Configures parameters and events external to the application.
 


### Signature

```python
__init__(self, *args, **kwargs) -> None:
```

Class constructor.


### Properties


#### frame

```python
frame(self) -> QtWidgets:
```

Application frame.
  
  That is, the main application window.
  

#### icon

```python
icon(self) -> str:
```

Frame icon path string.

  Application Icon.
  

#### frame_id

```python
frame_id(self) -> list:
```

Frame identity list.

  List containing app identity information.
  The first item is the main file, __file__, followed by an ID
  Example:
   [__file__, 'app_id', 'App Name']

  ID name must be 3 characters or more, and can only contain lowercase 
  letters, numbers or underscores '_', such as:
   [__file__, 'app_4_me', 'App 4 me' ]

  When set the list, all items are optional, but the order is mandatory.
  
