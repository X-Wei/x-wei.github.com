Title: [learning torch] 1. Tensor 
Date: 2016-10-07 15:30 
Slug:  learn-torch-1-tensor 
Tags: torch 
Series: torch学习笔记 
 
[TOC]
      
 
A `Tensor` is the fondamental data type in torch, (similar to numpy for tensorflow), it's a potentially multi-dimensional matrix. 
 
See doc: <https://github.com/torch/torch7/blob/master/doc/tensor.md> 
 
basic ops 
--------- 
 
 
* Indicate shape in constructor: 
 
 
	th> x = torch.Tensor(3,4) 
	                                                                      [0.0000s] 
	th> x 
	 3.7366e+193  9.4775e+170  3.3018e+180   4.8950e-85 
	 1.3808e+267  7.6859e+261   3.7512e-81  1.4692e+195 
	 9.7016e+189  6.9641e+252  9.1815e+170  4.5239e+217 
	[torch.DoubleTensor of size 3x4] 
 
 
By default the elements of a newly allocated memory are **not initialized**, might contain arbitrary numbers !  
 
 
* ``x:dim()``: return nb of dimensions 
* ``x:nElement()``: return nb of elements ("size") 
* ``x:size()``: return "shape", shortcut is: ``#x`` 
* ``x:resize(sz1, sz2, ...)``: will not throw exception when total size is inconsistent! 
 
```lua 
	th> #x 
	 3 
	 4 
	[torch.LongStorage of size 2] 
	                                                                      [0.0001s] 
	th> x:size() 
	 3 
	 4 
	[torch.LongStorage of size 2] 
	 
	                                                                      [0.0001s] 
	th> x:dim() 
	2 
	 
	th> x = torch.Tensor(3,4) 
	                                                                      [0.0000s] 
	th> x:resize(2,6) 
	 1.7479e+270  7.0981e+194  7.4861e-114  1.7479e+270  8.2791e-114  3.6822e+180 
	  4.8548e-27   6.9204e-72  8.8289e+199  1.1567e+247   4.8548e-27  7.7700e-109 
	[torch.DoubleTensor of size 2x6] 
	 
	                                                                      [0.0002s] 
	th> x:resize(2,7) 
	Columns 1 to 6 
	 1.7479e+270  7.0981e+194  7.4861e-114  1.7479e+270  8.2791e-114  3.6822e+180 
	  6.9204e-72  8.8289e+199  1.1567e+247   4.8548e-27  7.7700e-109   6.9006e-72 
	 
	Columns 7 to 7 
	  4.8548e-27 
	 1.0240e-259 
	[torch.DoubleTensor of size 2x7] 
	 
	                                                                      [0.0001s] 
	th> x:resize(2,4) 
	 1.7479e+270  7.0981e+194  7.4861e-114  1.7479e+270 
	 8.2791e-114  3.6822e+180   4.8548e-27   6.9204e-72 
	[torch.DoubleTensor of size 2x4] 
``` 
 
 
* fill with constant value: 
 
 
	th> x:fill(1) 
	 1  1  1  1 
	 1  1  1  1 
	 1  1  1  1 
	[torch.DoubleTensor of size 3x4] 
 
 
* other constructors: 
 
 
```lua 
	th> y = torch.Tensor(x) -- note: y is just a reference of x!!! 
	                                                                      [0.0001s] 
	th> y = torch.Tensor({ {2,3,4},{1,2,3} }) 
	                                                                      [0.0000s] 
	th> y 
	 2  3  4 
	 1  2  3 
	[torch.DoubleTensor of size 2x3] 
``` 
 
 
 
Storage 
------- 
 
>One could say that a ``Tensor`` is a particular way of viewing a ``Storage``: a ``Storage`` only represents a chunk of memory, while the ``Tensor`` interprets this chunk of memory as having dimensions.  
 
```lua
	th> s = x:storage() -- 'flatten' version of x 
	                                                                      [0.0000s] 
	th> for i=1,#s do s[i]=i end 
	                                                                      [0.0000s] 
	th> x 
	  1   2   3   4 
	  5   6   7   8 
	  9  10  11  12 
	[torch.DoubleTensor of size 3x4] 
``` 
 
 
short for range: torch.range(1,5) 
 
Slicing 
------- 
 
<https://github.com/torch/torch7/blob/master/doc/tensor.md#extracting-sub-tensors> 
 
 
* Slicing using ``sub()`` and ``select()``.  
 
```lua
	th> x 
	  1   2   3   4 
	  5   6   7   8 
	  9  10  11  12 
	[torch.DoubleTensor of size 3x4] 
	 
	th> print(x:sub(2,3,2,4)) -- x[2:3, 2:4] slicing 
	  6   7   8 
	 10  11  12 
	[torch.DoubleTensor of size 2x3] 
	 
	th> print(x:select(2,2)) -- select(dim, index), dim=1 for rows, =2 for cols 
	  2 
	  6 
	 10 
	[torch.DoubleTensor of size 3] 
	 
``` 
 
 
 
* Or use slicing/indexing **shortcut**: ``[{ {dim1start, dim1end},...}] [dim1, dim2,...]`` 
 
```lua
	th> x 
	  1   2   3   4   5   6 
	  7   8   9  10  11  12 
	 13  14  15  16  17  18 
	 19  20  21  22  23  24 
	 25  26  27  28  29  30 
	[torch.DoubleTensor of size 5x6] 
	 
	                                                                      [0.0002s] 
	th> x[2][3] 
	9	 
	                                                                      [0.0000s] 
	th> x[{2,3}] 
	9	 
	                                                                      [0.0000s] 
	th> x[{2,{2,5}}] 
	  8 
	  9 
	 10 
	 11 
	[torch.DoubleTensor of size 4] 
	 
	                                                                      [0.0001s] 
	th> x[{ {}, 3}] 
	  3 
	  9 
	 15 
	 21 
	 27 
	[torch.DoubleTensor of size 5] 
``` 
 
 
 
All are references 
------------------ 
 
>All tensor operations in this class do not make any memory copy. **All these methods transform the existing tensor, or return a new tensor referencing the same storage**.  
 
```lua
	th> y = torch.Tensor(x) 
	                                                                      [0.0000s] 
	th> y 
	  1   2   3   4 
	  5   6   7   8 
	  9  10  11  12 
	[torch.DoubleTensor of size 3x4] 
	 
	                                                                      [0.0001s] 
	th> y:select(1,1):zero() -- x will be effected 
	                                                                      [0.0001s] 
	th> y 
	  0   0   0   0 
	  5   6   7   8 
	  9  10  11  12 
	[torch.DoubleTensor of size 3x4] 
	 
	                                                                      [0.0001s] 
	th> x 
	  0   0   0   0 
	  5   6   7   8 
	  9  10  11  12 
	[torch.DoubleTensor of size 3x4] 
 
``` 
 
If don't want to modify original tensor, use ``clone()``: 
 
```lua
    th> y = x:clone() 
                                                                          [0.0000s] 
    th> y:sub(1,3,1,2):fill(-1) 
    -1 -1 
    -1 -1 
    -1 -1 
    [torch.DoubleTensor of size 3x2] 
 
                                                                          [0.0001s] 
    th> y 
     -1  -1   0   0 
     -1  -1   7   8 
     -1  -1  11  12 
    [torch.DoubleTensor of size 3x4] 
 
                                                                          [0.0001s] 
    th> x 
      0   0   0   0 
      5   6   7   8 
      9  10  11  12 
    [torch.DoubleTensor of size 3x4] 
``` 
 
 
Matrix ops 
---------- 
 
Some matrix operations 
 
 
* random matrix: 
 
```lua
	th> torch.manualSeed(1) 
	                                                                      [0.0000s] 
	th> A = torch.rand(3,4) 
	                                                                      [0.0001s] 
	th> print(A)  
	 0.4170  0.9972  0.7203  0.9326 
	 0.0001  0.1281  0.3023  0.9990 
	 0.1468  0.2361  0.0923  0.3966 
	[torch.DoubleTensor of size 3x4] 
 
``` 
 
* transpose  
 
```lua
	th> At = A:t() 
	                                                                      [0.0000s] 
	th> At 
	 0.4170  0.0001  0.1468 
	 0.9972  0.1281  0.2361 
	 0.7203  0.3023  0.0923 
	 0.9326  0.9990  0.3966 
	[torch.DoubleTensor of size 4x3] 
``` 
 
* matrix mul is just ``*`` 
 
```lua
	th> A * At  
	 2.5568  1.2773  0.7330 
	 1.2773  1.1059  0.4544 
	 0.7330  0.4544  0.2431 
	[torch.DoubleTensor of size 3x3] 
``` 
 
 
* inner product: ``dot()`` 
 
```lua
	th> A[1]:dot(At:select(2,1)) 
	2.5568154905493 
	 
``` 
 
* inverse: ``torch.inverse(sq_mat)``    
 
 
 
More operations 
--------------- 
 
can be found at:  
 
<https://github.com/torch/torch7/blob/master/doc/maths.md> 
 
example:  
 
* ``torch.ones()/eye()/zeros()`` 
* ``torch.cat()``: concat tensors    
 
 
```lua
		th> torch.cat(torch.ones(3, 2), torch.zeros(2, 2), 1) 
		 1  1 
		 1  1 
		 1  1 
		 0  0 
		 0  0 
		[torch.DoubleTensor of size 5x2] 
``` 
 
* ``torch.conv2()`` 
 
