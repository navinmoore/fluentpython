

### 容器序列 (能存放不同类型的数据, 存放的是他们包含的任意类型对象的引用)

1. list

2. tuple

3. collections.deque


### 扁平序列 (只能容纳同一中类型， 存放的是值而不是引用， 是一段连续的内存空间)

1. str

2. bytes

3. bytearray

4. memoryview

5. array.array


## 按是否能被修改分类

### 可变类型

1. list

2. bytearray

3. array.array

4. collections.deque

5. memoryview

### 不可变类型

1. tuple

2. str

3. bytes