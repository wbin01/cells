

## <h2 style="color: #5697bf;"><u>Application</u></h2>

<span style="color: #AAA;">Class</span>

**Inherits from: _object_**

Application manager.

 Configures parameters and events external to the application.
 


### <h2 style="color: #5e5d84;">Signature</h2>

```python
__init__(self, *args, **kwargs) -> None:
```

Class constructor.


### <h2 style="color: #5e5d84;">Properties</h2>


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
  


---