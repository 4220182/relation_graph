***测试方法：

**方法1: 

1. git clone git@github.com:4220182/relation_graph.git
2. cd relation_graph
2. docker build -t test/graph:0.0.1 .
3. docker run -d -p 8001:80 test/graph:0.0.1
4. 使用浏览器访问：http://127.0.0.1:8001/ 

**方法2:

1. docker run -d -p 8001:80 koza/relation-graph:0.0.1-beta1
2. 使用浏览器访问：http://127.0.0.1:8001/ 

现在可以娱乐一下了（以下关系来源于网络，请自行百度）：

![avatar](/static/images/sample.png)
