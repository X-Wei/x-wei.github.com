Title: [learning torch] 2. Module (layers)  
Date: 2016-10-07 19:40 
Slug:  learn-torch-2-module 
Tags: torch 
Series: torch学习笔记 
 
      
 
``Module`` is an abstract class which defines fundamental methods necessary for a *Layer*. 
 
doc: <https://github.com/torch/nn/blob/master/doc/module.md> 
 
Module class 
------------ 
 
variables in ``Module``:  
 
 
* ``output``: Tensor, the ouput computed from last call of ``forward(input)`` 
* ``gradInput``: Tensor, gradient wrt input of module, computed from last call of ``updateGradInput(input, gradOutput)`` 
 
 
important methods in ``Module``:  
 
 
* ``forward(input)``: return corresponding output of layer 
* ``backward(input, gradOutput)``: return gradInput wrt the given input 
 
 
Linear 
------ 
 
<https://github.com/torch/nn/blob/master/doc/simple.md#nn.Linear> 
 
``Linear`` extends ``Module``, it's just linear transformation of input: ``y=Ax+b`` (parameters/variables: ``weight``, ``bias``) 
 
``gradWeight``, ``gradBias`` are respectively the gradient of each parameter.  
 
 
	th> ln = nn.Linear(3, 2) -- 3 input, 2 output 
	                                                                      [0.0001s]	 
	th> ln.weight:fill(1); ln.bias:zero(); 
	                                                                      [0.0000s]	 
	th> x = torch.Tensor({1,2,3}) 
	                                                                      [0.0000s]	 
	th> y = ln:forward(x) 
	                                                                      [0.0000s]	 
	th> gradinput = ln:backward(x,y) 
	                                                                      [0.0001s]	 
	th> gradinput 
	 12 
	 12 
	 12 
	[torch.DoubleTensor of size 3] 
	 
	                                                                      [0.0001s]	 
	th> ln.gradInput 
	 12 
	 12 
	 12 
	[torch.DoubleTensor of size 3] 
	 
	                                                                      [0.0001s]	 
	th> ln.gradWeight 
	1.1132e+171  1.2000e+01 7.3587e+223 
	1.7112e+243 2.3276e+251 5.0404e+180 
	[torch.DoubleTensor of size 2x3] 
	 
	                                                                      [0.0001s]	 
	th> ln.gradBias 
	 6 
	 6 
	[torch.DoubleTensor of size 2] 
	 
	                                                                      [0.0001s] 
	 
 
 
Identity 
-------- 
 
output reproduces input, this layer can be used to model the input layer of a neural network.  
 
	th> id = nn.Identity() 
	                                                                      [0.0000s]	 
	th> y = id:forward(x) 
	                                                                      [0.0000s]	 
	th> y 
	 1 
	 2 
	 3 
	[torch.DoubleTensor of size 3] 
	 
	                                                                      [0.0001s]	 
	th> id:backward(x,y) 
	 1 
	 2 
	 3 
	[torch.DoubleTensor of size 3] 
	 
	                                                                      [0.0001s]	 
	th> id.gradInput 
	 1 
	 2 
	 3 
	[torch.DoubleTensor of size 3] 
 
 
      
 
Other modules 
------------- 
 
<https://github.com/torch/nn/blob/master/doc/simple.md> 
 
some examples: 
 
 
* ``Add`` 
* ``Mul`` 
* ``CMul`` 
* ``Reshape`` 
 
