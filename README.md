## 事件注册与回调

为了降低各模块之间的耦合度，除了可以采用rpc的方式外，也可以采用事件订阅的方式进行。

### demo

#### demo1 

demo1 以输入信号的方式进行调用

见 [here](demo1.py)

demo1 运行结果

```python
Input your action <create, update, delete>: create
*****starting create database*****
.
.
.
*****create database finish*****
*****starting create student table*****
.
.
.
*****create database finish*****
*****starting create class table*****
.
.
.
*****create database finish*****
*****starting create teacher table*****
.
.
.
*****create database finish*****

```

#### demo2

在demo2中使用了接口请求的方式进行调用，灵活性我觉得更好一些

见[here](./demo2.py)

demo2运行结果与demo1相同，只是通过了接口调用的方式进行。