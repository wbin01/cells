

## <h2 style="color: #5697bf;"><u>Application</u></h2>

<span style="color: #888;">Class</span>

**Inherits from: _object_**

Application manager.

 Configures parameters and events external to the application.
 

```python
__init__(self, *args, **kwargs) -> None:
```

Class constructor.

### <h2 style="color: #5e5d84;">Properties</h2>

#### frame

**_  QtWidgets_**

Application frame.

That is, the main application window.



#### icon

**_  str_**

Frame icon path string.

Application Icon.



#### frame_id

**_  list_**

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