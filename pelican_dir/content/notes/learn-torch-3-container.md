Title: [learning torch] 3. Container (models) 
Date: 2016-10-07 20:20 
Slug:  learn-torch-3-container 
Tags: torch 
Series: torch学习笔记 
 
      
 
doc: <https://github.com/torch/nn/blob/master/doc/containers.md>     
ref: <http://rnduja.github.io/2015/10/04/deep_learning_with_torch_step_2_nn_containers/>   
  
Container, similarly to Module, is the abstract class defining the base methods inherited from concrete containers. *Container contains modules (layers)*.  
 
Container class 
--------------- 
 
important methods:  
 
 
* ``add(module)`` 
* ``get(index)``: get module at the index 
* ``size()`` 
 
 
important subclasses: 
 
 
* ``Sequential`` 
* ``Parallel`` 
* ``Concat`` 
 
 
Sequential 
---------- 
 
``Sequential``** is just a stack of layers**, add layer by ``model:add()``. Here is a simple 2-layer MLP example:  
 
	th>  mlp = nn.Sequential() 
	                                                                      [0.0000s]	 
	th> mlp:add( nn.Linear(10, 25) ) -- 10 input, 25 hidden units 
	                                                                      [0.0001s]	 
	th> mlp:add( nn.Tanh() ) -- some hyperbolic tangent transfer function 
	                                                                      [0.0001s]	 
	th> mlp:add( nn.Linear(25, 1) ) -- 1 output 
	                                                                      [0.0001s]	 
	th> mlp:forward(torch.range(1,10)) 
	 1.2697 
	[torch.DoubleTensor of size 1] 
 
 
Parallel 
-------- 
 
``module = Parallel(inputDimension,outputDimension)`` 
 
>*Creates a container module that applies its ith child module to the ith slice of the input Tensor* by using ``select`` on dimension ``inputDimension``. It concatenates the results of its contained modules together along dimension ``outputDimension``.  
 
So if the input for parallel model is ``x``,  the input for its ith child module should be: ``x.select(inputDimension, i)``,  
and the parallel model should be: ``torch.cat( out1, out2, ouputDimension)`` (concat along this dimension).  
 
 
	th> mlp = nn.Parallel(2,1) -- select(split) on dim2 for input, concat along dim1 for output 
	                                                                      [0.0000s]	 
	th> mlp:add(nn.Linear(10,3)) -- input=1st slice of x (x:select()), output1: size=3 
	                                                                      [0.0001s]	 
	th> mlp:add(nn.Linear(10,2)) -- output2: size=2 
	                                                                      [0.0001s]	 
	th> x = torch.randn(10,2)  
	                                                                      [0.0001s]	 
	th> x 
	 0.3242 -1.3911 
	 0.7433 -0.2725 
	 0.3947  0.3332 
	 1.1618  0.6743 
	 0.6655 -1.0901 
	 0.0419 -0.7845 
	-0.8508 -1.4670 
	-0.3842 -0.4107 
	 0.5238  2.3616 
	 1.4136 -0.1327 
	[torch.DoubleTensor of size 10x2] 
	 
	                                                                      [0.0002s]	 
	th> mlp:forward(x) 
	-0.0456 
	-0.5682 
	-0.3488 
	-1.3786 
	-0.6320 
	[torch.DoubleTensor of size 5] 
 
 
Concat 
------ 
 
``module = nn.Concat(dim)`` 
 
Concat concatenates the output of its "parallel" children modules along ``dim``: these child modules *take the same inputs*, and their output is concatenated. 
 
	th> mlp = nn.Concat(1) -- ouput concat along dim 1 
	                                                                      [0.0001s]	 
	th> mlp:add( nn.Linear(10,2) ); 
	                                                                      [0.0001s]	 
	th> mlp:add( nn.Linear(10,3) ); 
	                                                                      [0.0000s]	 
	th> x = torch.randn(1,5) 
	 
	th> mlp:forward(x) 
	 0.7497 
	-0.1909 
	 0.3280 
	-0.3981 
	 0.0207 
	[torch.DoubleTensor of size 5] 
 
 
 
 
