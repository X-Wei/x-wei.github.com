Title: [learning torch] 6. optim (optimization tools)    
Date: 2016-10-10   
Slug: learn-torch-6-optim  
Tags: torch    
 
6. optim 
======== 
Created Sunday 10 October 2016 
 
ref: <http://rnduja.github.io/2015/10/26/deep_learning_with_torch_step_7_optim/>    
doc: <https://github.com/torch/optim/blob/master/doc/intro.md>    
 
 
Before we implement the gd update step by defining a ``gradientUpdate`` function and calling it in a loop.  
 
	function gradientUpdate(model, x, y, criterion, learningRate) 
		local pred = model:forward(x) -- assumes pred is what criterion expects as input 
		local loss = criterion:forward(pred, y) 
		model:zeroGradParameters() 
		local grad_cri = criterion:backward(pred, y) 
		model:backward(x, grad_cri) 
		model:updateParameters(learningRate) 
	end 
 
But this is functionality is implemented in the ``optim`` module. In addition to just grad-descent, it has more complicated optimization algorithms implemented.  
 
Interface 
--------- 
 
The interface for all optimization algos are: 
 
``params_new, fs, ... = optim._method_(feval, params[, config][, state])`` 
 
explination:  
 
* ``params``: current parameters vector (**1D tensor**), this will be updated during optimization 
* ``feval``: a user-defined closure that respects this API: ``f, df/dx = feval(x)`` 
* ``config``: a table of parameters for the algorithm (e.g. learning rate) 
* ``state``: a table of state variables 
* ``params_new``: the resulting new parameter (in a 1D tensor), which minimizes the function f 
* ``fs``: a table of f values evaluated during the optimization, ``fs[#fs]`` is the optimized function value 
 
 
**note:**  
As optim expects the input to be 1D tensors, we need to **flatten** the parameters in our model, this can be achieved via:  
 
``params, gradParams = model:getParameters()`` 
 
the reuslting ``params`` and ``gradParams`` are all flattened into 1D tensor.  
 
Example: sgd to train mlp the XOR function 
------------------------------------------ 
 
Here is an example for learning an XOR using a mlp with one hidden layer.  
 
### model, criterion 
 
First, define the model and criterion (use MSE here, see it as a regression problem):  
 
	require 'nn' 
	inputs = 2; outputs = 1; HUs = 20 -- parameters 
	 
	model = nn.Sequential()  -- make a multi-layer perceptron 
	model:add(nn.Linear(inputs, HUs)) 
	model:add(nn.Tanh()) 
	model:add(nn.Linear(HUs, outputs)) 
	 
	criterion = nn.MSECriterion() 
 
 
### data 
 
Then generate dataset of XORs: sample 2d inputs, and lables are -1 if the samples are of the sign, otherwise +1. Generate 128 training samples: 
 
	batchSize = 128 
	batchInputs = torch.DoubleTensor(batchSize, inputs)  
	batchLabels = torch.DoubleTensor(batchSize)         
	 
	for i = 1, batchSize do 
	   local input = torch.randn(2)   
	   local label 
	   if input[1] * input[2] > 0 then  -- calculate label for XOR function 
	      label = -1 
	   else 
	      label = 1 
	   end 
	   batchInputs[i]:copy(input) 
	   batchLabels[i] = label 
	end 
 
 
### feval() closure 
 
Then define the feval function that returns the loss and the gradient wrt the loss:  
 
	function feval(params) 
	    gradParams:zero() 
	    local outputs = model:forward(batchInputs) 
	    local loss = criterion:forward(outputs, batchLabels) 
	    local dloss_doutputs = criterion:backward(outputs, batchLabels) 
	    model:backward(batchInputs, dloss_doutputs) 
	    return loss, gradParams 
	end 
 
 
finally, apply ``optim.sgd`` to the batch for 500 epochs:  
 
	require 'optim' 
	local sgdcfg = {learningRate=0.01} 
	 
	for epoch=1,500 do 
	    optim.sgd(feval, params, sgdcfg) 
	end 
 
can take some examples to test:  
 
	x = torch.Tensor(2) 
	x[1] =  0.5; x[2] =  0.5; print(model:forward(x)[1]) 
	x[1] =  0.5; x[2] = -0.5; print(model:forward(x)[1]) 
	x[1] = -0.5; x[2] =  0.5; print(model:forward(x)[1]) 
	x[1] = -0.5; x[2] = -0.5; print(model:forward(x)[1]) 
 
 
The output is:  
 
	-0.0073583598776157	 
	0.24137506111789	 
	0.31254747107449	 
	-0.14114052583337 
	 
 
And the signs are correct for XOR function.  
