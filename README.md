# Python Pandas By Jacqueline Xu and Kevin Li

### What is Python Panda?
* Developed by Wes McKinney starting 2008
  * Stable release in December 2017
* An open-source Python library that provides
  * Data structures
  * Data analysis tools
* Often used in these fields:
  * Finance
  * Economics
  * Statistics
  * Analytics
* To install, using Python package installer, pip:
  * `pip install pandas`
---

### Data Structures For Pandas
| Series | Data Frames | Panel |
| --- | --- | --- |
| 1D array | 2D array | 3D array |
| labeled | labeled | labeled |
| size-immutable | size-mutable | size-mutable |
| value-mutable | value-mutable | value-mutable |
| homogenous data | heterogeneous data | heterogeneous data |

---

### pandas.Series
Constructor: `pandas.Series( data, index, dtype, copy)`
* `data` can take in different data structures:
  * ndarray, dictionaries, lists, constants, etc
* `index` takes in a list of labels:
  * numbers, letters, strings, etc
  * doesn’t have to start at ‘a’ or 1
* `dtype` takes in the datatype:
  * If not given, it will be assumed
* `copy` means to copy data
  * If not given, default is False

---

### pandas.DataFrame
Constructor: `pandas.DataFrame( data, index, columns, dtype, copy)`
* `data` takes various forms:
  * ndarray, series, map, lists, dict, constants and also another DataFrame.
* `index` can be thought of as the row labels
  * If not given, it will use default integer indexes
* `columns`: column labels
  * If not given, it will use default integer indexes
* `dtype`: data type of each column
  * If not given, it will be assumed
* `copy`: copy data
  * If not given, default is False
* Note: Values are assigned differently based on the data structures received

---

### Basic Tools
* `axes`: Returns a list of the row axis labels.
* `dtype`: Returns the dtype of the object.
* `empty`: Returns True if series is empty.
* `ndim`: Returns the number of dimensions of the underlying data. (Series: 1, DataFrame: 2, Panel: 3)
* `size`: Returns the number of elements in the underlying data.
* `values`: Returns the Series as ndarray.
* `head(n)`: Returns the first n rows.
* `tail(n)`: Returns the last n rows.

**Note:** all methods are pass by reference

---

### Statistical Tools
* `count(n)`: Number of non-null observations
* `sum(n)`: Sum of values (strings are concatenated)
* `mean(n)`: Mean of Values
* `median(n)`: Median of Values
* `mode(n)`: Mode of values
* `std(n)`: Standard Deviation of the Values
* `min(n)`: Minimum Value
* `max(n)`: Maximum Value
* `abs(n)`: Absolute Value
* `prod(n)`: Product of Values

**Note:** `n` is the axis on which the method operates on, the default is 0.
* For a DataFrame:
  * Axis = 0 (Operates vertically)
  * Axis = 0 (Operates horizontally)

---

### Data Summary
`describe()`: summary of statistics pertaining to the DataFrame columns.
* Parameter include:
  * ‘object’, ‘number’, ‘all’
* Data output:
  * count
  * unique, top, freq
  * mean, std, min, 25%, 50%, 75%, max

---

### Text Data
* `lower()`, `upper()`, `len()`, `swapcase`, `islower()`, `isupper()`, `isnumeric()`
* `strip()`: Strips whitespace(including ‘\n’) from each string in the Series/index from both the sides.
* `split(' ')`: Splits each string with the given pattern.
* `cat(sep=' ')`: Concatenates the series/index elements with given separator.
* `contains(pattern)`: Returns a Boolean value True for each element if the substring contains in the element, else False.
* `replace(a,b)`: Replaces the value a with the value b.
* `repeat(value)`: Repeats each element with specified number of times.
* `count(pattern)`: Returns count of appearance of pattern in each element.
* `startswith(pattern)`: Returns true if the element in the Series/Index starts with the pattern.
* `endswith(pattern)`: Returns true if the element in the Series/Index ends with the pattern.
* `find(pattern)`: Returns the first position of the first occurrence of the pattern. (or -1)
* `findall(pattern)`: Returns a list of all occurrence of the pattern.

---

### Missing Data
* `isnull()/notnull()`: replaces the values with Booleans
* `fillna(value)`: replace all null value with the parameter inside
* `dropna()`: drop all rows in which any of their values are null
* `replace(a,b)`: Replaces the value a with the value b.
All NaN values are disregarded in calculation, but this may not be what you want. You can use fillna(0) to manually change null values to 0.

---

### Sorting
* sort_index()
  * axis: default is 0
  * ascending: default is True
* sort_value()
  * by: which column
  * kind: which sort (mergesort, heapsort and quicksort)

---

### Other Features
* Reindexing
* Iteration
* Merging 2 data structures based on common columns
* Concatenating 2 data structures with same columns
