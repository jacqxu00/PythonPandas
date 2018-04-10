# Python Pandas
## Jacqueline Xu, Kevin Li -- Period 9 SoftDev
_For full demo code, see repo._

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
Pandas only deals with these three data structures.

| Series | Data Frames | Panel |
| --- | --- | --- |
| 1D array | 2D array | 3D array |
| labeled | labeled | labeled |
| size-immutable | size-mutable | size-mutable |
| value-mutable | value-mutable | value-mutable |
| homogenous data | heterogeneous data | heterogeneous data |

---

### pandas.Series
Constructor: `pandas.Series( data, index, dtype, copy)` <br>
* `data` can take in different data structures:
  * ndarray, dictionaries, lists, constants, etc
* `index` takes in a list of labels:
  * numbers, letters, strings, etc
  * doesn’t have to start at ‘a’ or 1
* `dtype` takes in the datatype:
  * If not given, it will be assumed
* `copy` means to copy data
  * If not given, default is False

<b> Input </b>
```python
s1 = pd.Series()
print s1
```
Output
```
Series([], dtype: float64)
```
<b> Input </b>
```python
data = np.array(['apple','banana','carrot','dill pickle'])
s2 = pd.Series(data)
print s2
```
Output
```
0          apple
1         banana
2         carrot
3    dill pickle
```
<b> Input </b>
```python
data = np.array(['apple','banana','carrot','dill pickle'])
s3 = pd.Series(data, index=[24,25,26,27])
print s3
```
Output
```
24          apple
25         banana
26         carrot
27    dill pickle
dtype: object
```
<b> Input </b>
```python
dictionary = {'humpty' : 10, 'dumpty' : 12, 'eggs' : 14}
s4 = pd.Series(dictionary)
print s4
```
Output
```
dumpty    12
eggs      14
humpty    10
dtype: int64
```
<b> Input </b>
```python
dictionary = {'humpty' : 10, 'dumpty' : 12, 'eggs' : 14}
s5 = pd.Series(dictionary,index=['humpty','eggs'])
print s5
```
Output
```
humpty    10
eggs      14
dtype: int64
```
<b> Input </b>
```python
dictionary = {'humpty' : 10, 'dumpty' : 12, 'eggs' : 14}
s6 = pd.Series(dictionary,index=['humpty','eggs','wall'])
print s6
```
Output
```
humpty    10.0
eggs      14.0
wall       NaN
dtype: float64
```
<b> Input </b>
```python
period= {'Math' : 7, 'Cycling' : 1, 'Graphics' : 10, 'SoftDev' : 9, 'WaterColor' : 2}
s7 = pd.Series(period)
print s7
```
Output
```
Cycling        1
Graphics      10
Math           7
SoftDev        9
WaterColor     2
dtype: int64
```
<b> Input </b>
```python
print s7[0]
```
Output
```
1
```
<b> Input </b>
```python
print s7[:3]
```
Output
```
Cycling      1
Graphics    10
Math         7
dtype: int64
```
<b> Input </b>
```python
print s7[2:4]
```
Output
```
Math       7
SoftDev    9
dtype: int64
```
<b> Input </b>
```python
print s7['Math']
```
Output
```
7
```
<b> Input </b>
```python
print s7[['SoftDev', 'Graphics']]
```
Output
```
SoftDev      9
Graphics    10
dtype: int64
```
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

<b> Input </b>
```python
data = [['Alex',10],['Bob',12],['Clarke',13]]
df1 = pd.DataFrame(data,columns=['Name','Age'], index=['Entry1', 'Entry2', 'Entry3'])
print df1
```
Output
```
          Name  Age
Entry1    Alex   10
Entry2     Bob   12
Entry3  Clarke   13
```
<b> Input </b>
```python
d = {'one' : pd.Series([1.0, 2.0, 3.0], index=['a', 'b', 'c']),
      'two' : pd.Series([1.0, 2.0, 3.0, 4.0], index=['a', 'b', 'c', 'd'])}

anotherd = {'one' : pd.Series([1.0, 2.0, 3.0], index=['a', 'b', 'c']),
      'two' : pd.Series([6.0, 7.0, 8.0, 10.0], index=['a', 'b', 'c', 'd']),
      'three' : pd.Series([7.0, 3.0, 11.0, 12.0], index=['a', 'b', 'c', 'd'])}
      
df2 = pd.DataFrame(d)
print d['one']
```
Output
```
a    1.0
b    2.0
c    3.0
dtype: float64
```
<b> Input </b>
```python
print d['two']
```
Output
```
a    1.0
b    2.0
c    3.0
d    4.0
dtype: float64
```
<b> Input </b>
```python
print df2
```
Output
```
   one  two
a  1.0  1.0
b  2.0  2.0
c  3.0  3.0
d  NaN  4.0
```
<b> Input </b>
```python
print df2.dropna()
```
Output
```
   one  two
a  1.0  1.0
b  2.0  2.0
c  3.0  3.0
```
<b> Input </b>
```python
df2 = pd.DataFrame(anotherd)
print df2
```
Output
```
   one  three   two
a  1.0    7.0   6.0
b  2.0    3.0   7.0
c  3.0   11.0   8.0
d  NaN   12.0  10.0
```
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

<b> Input </b>
```python
print df2.mean(1)
```
Output
```
a     4.666667
b     4.000000
c     7.333333
d    11.000000
dtype: float64
```

**Note:** `n` is the axis on which the method operates on, the default is 0.
* For a DataFrame:
  * Axis = 0 (Operates vertically)
  * Axis = 1 (Operates horizontally)

---

### Data Summary
`describe()`: summary of statistics pertaining to the DataFrame columns.
* Parameter include:
  * ‘object’, ‘number’, ‘all’
* Data output:
  * count
  * unique, top, freq
  * mean, std, min, 25%, 50%, 75%, max

<b> Input </b>
```python
#DataFrame from https://pandas.pydata.org/pandas-docs/stable/10min.html
dates = pd.date_range('20180302', periods=6)
df3 = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
print df3
print df3.describe()
```
Output
```
                   A         B         C         D
2018-03-02 -1.267543  0.996103 -0.461436 -0.086646
2018-03-03 -0.977688 -0.141044  0.468877 -0.038657
2018-03-04 -0.371006  0.584427 -1.040594 -0.208818
2018-03-05 -0.293554 -2.586353 -0.861468  0.347996
2018-03-06 -0.036818 -0.049934  1.842039 -1.104940
2018-03-07  0.727559 -1.558487 -0.186077  0.256007
              A         B         C         D
count  6.000000  6.000000  6.000000  6.000000
mean  -0.369842 -0.459215 -0.039776 -0.139176
std    0.706591  1.357129  1.065455  0.518444
min   -1.267543 -2.586353 -1.040594 -1.104940
25%   -0.826017 -1.204126 -0.761460 -0.178275
50%   -0.332280 -0.095489 -0.323756 -0.062652
75%   -0.101002  0.425837  0.305139  0.182341
max    0.727559  0.996103  1.842039  0.347996
```
---

### Text Data
You may also use regular Python's string functions with Pandas text data.
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
There are two functions in which you can sort data in Pandas.
* `sort_index()`
  * axis: default is 0
  * ascending: default is True
* `sort_value()`
  * by: which column
  * kind: which sort (mergesort, heapsort and quicksort)

<b> Input </b>
```python
print "printing sorted by index, descending..."
print df3.sort_index(axis=1, ascending=False)
print "\nprinting sorted by B..."
print df3.sort_values(by='B')
print "\nprinting elements where C > 0..."
print df3[df3.C > 0]
```
Output
```
printing sorted by index, descending...
                   D         C         B         A
2018-03-02 -0.086646 -0.461436  0.996103 -1.267543
2018-03-03 -0.038657  0.468877 -0.141044 -0.977688
2018-03-04 -0.208818 -1.040594  0.584427 -0.371006
2018-03-05  0.347996 -0.861468 -2.586353 -0.293554
2018-03-06 -1.104940  1.842039 -0.049934 -0.036818
2018-03-07  0.256007 -0.186077 -1.558487  0.727559

printing sorted by B...
                   A         B         C         D
2018-03-05 -0.293554 -2.586353 -0.861468  0.347996
2018-03-07  0.727559 -1.558487 -0.186077  0.256007
2018-03-03 -0.977688 -0.141044  0.468877 -0.038657
2018-03-06 -0.036818 -0.049934  1.842039 -1.104940
2018-03-04 -0.371006  0.584427 -1.040594 -0.208818
2018-03-02 -1.267543  0.996103 -0.461436 -0.086646

printing elements where C > 0...
                   A         B         C         D
2018-03-03 -0.977688 -0.141044  0.468877 -0.038657
2018-03-06 -0.036818 -0.049934  1.842039 -1.104940
```
---

### Other Features
* Reindexing
* Iteration
* Merging 2 data structures based on common columns
* Concatenating 2 data structures with same columns


