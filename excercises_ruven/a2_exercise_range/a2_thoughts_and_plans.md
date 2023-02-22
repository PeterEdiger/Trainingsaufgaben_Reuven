```python
>>> range(5)
[0, 1, 2, 3, 4]

>>> range(5,10)
[5, 6, 7, 8, 9]

>>> range(5,20,3)
[5, 8, 11, 14, 17]


```

## Welche Fälle gibt es ?

> - Fall1:  Nur stop **myrange2(4)** 
> - Fall2: Start, Stop positiv  **myrange2(3, 6)**
> - Fall3: Start, Stop, Step positiv **myrange(2, 10, 2)**
> - Fall4: Nur Stop negativ  **myrange(-6)**
> - Fall5: Start positiv, Stop negativ, **myrange(2, -3)**
> - Fall6: Start negativ, Stop positiv, **myrange(-2, 5)**
> - Fall7: Start positiv, Stop positiv, Step positiv **myrange(2, 10, 2)**
> - Fall8: Start positiv, Stop positiv, Step negativ **myrange(2, 10, -2)**
> - Fall9: Start positiv, Stop negativ, Step positiv, **myrange(5, -10, 2)**
> - Fall10. Start positiv, Stop negativ, Step negativ **myrange(3, -10, -2)**
> - Fall11: Start negativ, Stop positiv, Step positiv **myrange(-10, 2, 2 )**
> - Fall12: Start negativ, Stop positiv, Step negativ **myrange(-10,  4,  -3)**
> - Fall13 Start negativ, Stop negativ, Step negativ **myrange(-10, -)**

---

Durch args habe ich die Möglichkeit Die len(args) zu benutzen, und über den index von args Bedingungen aufzustellen. 

Nur positiv. 

> - Fall1: 1 parameter **myrange(5) ** --> stop = 5 -- step = 1
>
> - Fall2: 2 paramter **myrange(2, 5)**--> if len(args) == 2 -- start = args[0] -- stop = args[1]  -- step = 1
>
> - range_list[]
>
>   - if start < step:
>     - print("0")
>   - else: 
>     - num = 0
>     - while start < step:
>       - num += 1
>       - range_list.append(num)
>
> - Fall3: 3 parameter **myrange(2, 10, 3)**
>
>   ​	num = 0
>
>   ​	if len(args) == 3
>
>   ​	start = args[0] , stop = args[1], step = args[2]	
>
>   ​	while start < step:
>
>   ​		num = t
>
>   ​	range_list
>
>   
>
>   
>
>   Ich muss eine Zahl mit einer bestimmten Step immer draufzählen. 
>
>   gesteratet wird bei start --> dann wird eine Zahl draufgehählt
>
>   
>
>   Simulation: 
>
>   eine selbstgebaute kleine range funktion mit 3 parametern --> len(args) == 3 
>
>   



--> Tip eine range Funktion schreiben, die positiv ist.



Was soll passieren?

Wenn ich einen negativen step habe, soll er vom start um den negativen step verringern bis er beim Stop angelang ist. 



>
>
>Was muss die Logik haben Wenn ich einen Positiven step oder negativen step habe. 
>
>Bei 
>
>

```python
"""
Es ist erstmal klar wenn wir 3 Parameter haben, dass es ein step dabei sein muss. 

Beispiel: range(10, 20, 3)
Bei einem Positiven step darf der stop nicht kleiner sein als der Start, 
oder der Stop muss größer sein als der Start. 

Bei einem negativen Step ist es andersherum. 
Also (10, 20, -3)
Der Stop darf nicht größer sein als der Start. 
Der Stop muss kleiner sein als der start. 

Die while Schleife muss je nach dem wie der Step ist umgedreht werden... 

"""

# fdsfdsfdsfs
```





```python
def myrange2(*args):
    start = stop = step = None
    range_list = []
    if len(args) == 1:
        start = 0
        stop = args[0]
        step = 1

    if len(args) == 2:
        start = args[0]
        stop = args[1]
        step = 1

    if len(args) == 3:
        start = args[0]
        stop = args[1]
        step = args[2]
    if len(args) > 3 or len(args) == 0:
        print("Error")
        return []

    num = start

    while (num - stop) * step < 0:
        print(num, (num - stop) * step)
        range_list.append(num)
        num += step

    return range_list


def myrange3(*args):
    start = stop = step = None
    if len(args) == 1:
        start = 0
        stop = args[0]
        step = 1

    if len(args) == 2:
        start = args[0]
        stop = args[1]
        step = 1

    if len(args) == 3:
        start = args[0]
        stop = args[1]
        step = args[2]
    if len(args) > 3 or len(args) == 0:
        print("Error")
        return []

    num = start

    while (num - stop) * step < 0:
        # print(num, (num - stop) * step)
        yield num
        num += step


```

