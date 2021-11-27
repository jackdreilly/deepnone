# DeepNone

_Safe, simple access to optional nested attributes_

## Install [PyPI](https://pypi.org/project/deepnone/)

```bash
pip install deepnone
```


## How

Wrap untrusted value in `dn()`, transform it, then `get` it.

- If any transform step fails, it will return `None`.
- Otherwise, you'll get the transformed value from `get`.

```python title="how.py"
(
    dn(untrusted_value)
    .some_attribute[4]
    .fn(json.loads)[3]
    .upper()
    .get
)
```

## Why

Let's write a function to uppercase the name of the first batter in a JSON string.

If there's any failures in data extraction, we just want to return `None`.

### With `dn`

```python title="with_dn.py"
def first_batter_name_upper(value: str) -> str:
    return dn(value).fn(json.loads)['batters'][0].upper().get
```

### Without `dn`

99% of the code is error-checking to handle unexpected input.

```python title="without_dn.py"
def first_batter_name_upper(input_string: str) -> str:
    try:
        value = json.loads(input_string)
    except:
        return
    if not isinstance(value, dict):
        return
    if 'batters' not in value:
        return
    batters = value['batters']
    if not isinstance(batters, list):
        return
    if len(batters) < 1:
        return
    batter = batters[0]
    if not isinstance(batter, dict):
        return
    if 'name' not in batter:
        return
    name = batter['name']
    if not isinstance(name, str):
        return
    return name.upper()
```

## Tour

```python title="usage.py"
--8<-- "test_deepnone.py"
```

## Actions

### Access item `x[y]`

```python
assert ds({'x': 3})['x'].get == 3
```

### Get attribute `x.myfield`

```python
assert ds(fraction(5,8)).numerator.get == 5
```

### Call method `x.upper()`

```python
assert ds('asdf').upper() == 'ASDF'
```

### Transform `double_number(x)`

```python
assert ds(4).fn(double_number).get == 8
```

### Iterable coercion

```python
assert len((x for x in ds('a').bad_attr)) == 0
assert [x * 2 for x in ds({'x': [3, 4, 5]}).x] == [6, 8, 10]
```

### Truthiness

Directly assert the `bool` value of `dn`

```python
assert not dn(234).junk
```

### Equality

Compare `dn` directly against its built value.

```python
assert dn('asdf').upper() == 'ASDF'
```
