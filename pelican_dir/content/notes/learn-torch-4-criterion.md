Title: [learning torch] 4. Criterion (loss function)  
Date: 2016-10-08 14:00 
Slug:  learn-torch-4-criterion  
Tags: torch  
Series: torch学习笔记 
 
       
  
ref: <http://rnduja.github.io/2015/10/05/deep_learning_with_torch_step_3_nn_criterions/>   
doc: <https://github.com/torch/nn/blob/master/doc/criterion.md>   
  
``Criterion``: abstract class, given input and target(true label), a ``Criterion`` can compute the gradient according to a certain loss function.   
  
Criterion class  
---------------  
  
important methods:   
  
* ``forward(input, target)``: compute the loss function, the ``input`` is usually the prediction/log-probability prediction of the network, ``target`` is the truth label of training data.   
* ``backward(input, target)``: compute gradient of the loss function.   
  
  
subclasses of ``Criterion``:  
  
  
* classification critierions: cross-entropy, neg loglikelihood, ...  
* regression criterions: MSE, Abs, KL divergence, ...  
* embedding criterions  
* misc criterions  
  
  
Classification criterion examples  
---------------------------------  
  
### ClassNLLCriterion  
  
negative log likelihood criterion  
  
<https://github.com/torch/nn/blob/master/doc/criterion.md#nn.ClassNLLCriterion>  
  
``crt = nn.ClassNLLCriterion([weights])``  

optional argument ``weights`` is to assign class weights (1D tensor), which is useful for unbalanced dataset.   
  
For NLL criterion, the ``input`` given through a ``forward(input, target)`` is expected to be the *log-probabilities* of each class. The ``target`` is expected to be a class index (1 to n).   
  
The *probabilities* of each class can be computed by applying softmax on *logits*,  the log-proba is just to take the log of the probabilities. Can use directly [logsoftmax](https://github.com/torch/nn/blob/master/doc/transfer.md#logsoftmax) layer to achieve this (ex. add ``nn.LogSoftMax`` as last layer of a sequential container).   
  
If the input ``x`` is log-proba of each class, the loss is just:   
  
``loss = forward(x, target) = -x[target_class]``  
  
  
### CrossEntropyCriterion  
  
<https://github.com/torch/nn/blob/master/doc/criterion.md#nn.CrossEntropyCriterion>  
  
This combines a logsoftmax and a NLLcriterion, so the ``input`` is expected to be *logits* (scores)  
  
### MarginCriterion  
  
<https://github.com/torch/nn/blob/master/doc/criterion.md#margincriterion>  
  
computes hinge loss of binary classification problem.   
  
``input`` x is expected to be svm scores, ``target`` y is expected to be ±1 labels.   
  
  
Regression criterion examples  
-----------------------------  
  
### MSECriterion  
  
<https://github.com/torch/nn/blob/master/doc/criterion.md#nn.MSECriterion>  
  
``criterion = nn.MSECriterion()``  
  
the loss is just MSE, input and target both have n elements:   
  
``loss = forward(x,y) = sum[ (xi-yi)^2 ] / n``  
  
### AbsCriterion  
  
L1 distance between x and y.   
  
### DistKLDivCriterion  
  
KL divergence for class probabilities   
  
  
A Complete Example  
------------------  
  
### updating function  
  
First write a function for  grad-desc updating for a ``model``, input *to the model* is ``x``, truth label is ``y``.   
  
```lua
	function gradientUpdate(model, x, y, criterion, learningRate)  
		local pred = model:forward(x) -- assumes pred is what criterion expects as input  
		local loss = criterion:forward(pred, y)  
		model:zeroGradParameters()  
		local grad_cri = criterion:backward(pred, y)  
		model:backward(x, grad_cri)  
		model:updateParameters(learningRate)  
	end  
```  
  
This function implements an update step, given a training sample (``x``,``y``):  
  
  
1. the model computes its output by ``model:forward(x)``  
2. criterion takes model's output, and computes loss by``criterion:forward(pred, y)``, *note*: the output of model shall be what criterion expects, e.g. pred=log-class-proba for NLL criterion.   
3. criterion gives the gradient of loss function wrt the model output by ``cri:backward(pred, y)``  
4. model computes the gradient of its parameters using the gradient from criterion by ``model:backward(x, grad_cri)``  
5. the model do a gradient descent step to modify its parameters by ``model:updateParameters(learningRate)``  
  
    
*This is the function that we should pass to an optimizer.*   
  
### model, criterion and data  
  
  
* the model is just a linear layer (5 inputs, 1 output ), output = Ax+b  
  
  ```lua
		model = nn.Sequential()  
		model:add(nn.Linear(5,1))  
    ```
  
  
  
* the criterion is just hinge loss:   
  
  
``criterion = nn.MarginCriterion(1)``  
  
  
* For the data, just use 2 datapoints:   
  
  ```lua
	x1 = torch.rand(5)  
	y1 = torch.Tensor({1})  
	x2 = torch.rand(5)  
	y2 = torch.Tensor({-1})  
  ```
  
### training  
  
To train the model, we run the update funcion on the data points 1000 times (*epochs*):   
  
  ```lua
	for i = 1,1000 do  
	    gradientUpdate(model, x1, y1, criterion, 0.01)  
	    gradientUpdate(model, x1, y1, criterion, 0.01)  
	end  
  ```
  
### evaluating  
  
to see the prediciton, just use ``model:forward(x)``  
  
  ```lua
	print('prediction for x1='..model:forward(x1)[1]..' expected value='..y1[1])  
	print('prediction for x2='..model:forward(x2)[1]..' expected value='..y2[1])  
  ```  
  
to see loss, use ``criterion:forward(model_out, y)``  
  
  ```lua
	print('loss after training for x1 = ' .. criterion:forward(model:forward(x1), y1))  
	print('loss after training for x2 = ' .. criterion:forward(model:forward(x2), y2))  
  ```
