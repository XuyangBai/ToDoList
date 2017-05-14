# ToDoList

### 任务要求

使用 Django, Django Rest Framework, Bootstrap, PostgreSQL (optional), React+React Router+ Redux + Redux API (optional), jQuery (optional) 等技术做一个待办事项的网站。

一个参考的例子：[todoist.com](http://todoist.com/)

实现的功能：

* 创建一个待办事项（待办事项可以设置优先级、expire-date）
* 删除一个待办事项
* 标记一个待办事项为已完成
* 编辑一个待办事项的具体内容
* 列出所有的未完成的待办事项
* 支持按照不同的方式排序

### 界面展示
  
1. **TaskList**

 ![](https://d3dr1ze7164817.cloudfront.net/items/2Q3K0Q3I3s0S181V043f/FireShot%20Capture%209%20-%20TaskList%20-%20http___127.0.0.1_8000_task_.png?X-CloudApp-Visitor-Id=2759577)

2. **TaskDetail**

![](https://d3dr1ze7164817.cloudfront.net/items/1O2Y3D2Y3D0Y1p2U0b42/FireShot%20Capture%2010%20-%20TaskDetail%20-%20http___127.0.0.1_8000_task_47_.png?X-CloudApp-Visitor-Id=2759577)

### 功能展示

1. **创建待办事项**

事项有 `title,content,expire_date,priority` 这几个属性

![](https://d3dr1ze7164817.cloudfront.net/items/302C3O283U0M3Y2m3v1z/Screen%20recording%202017-05-14%20at%2006.13.08%20PM.gif?X-CloudApp-Visitor-Id=2759577)


2. **删除待办事项**

![](https://d3dr1ze7164817.cloudfront.net/items/1Q1f3w3x1D2W3Z0d340h/Screen%20recording%202017-05-14%20at%2006.14.26%20PM.gif?X-CloudApp-Visitor-Id=2759577)


3. **标记事项已完成**

![](https://d3dr1ze7164817.cloudfront.net/items/0o1k1u1F1P2d1F33322Z/Screen%20recording%202017-05-14%20at%2006.17.04%20PM.gif?X-CloudApp-Visitor-Id=2759577)


4. **编辑（修改）一个待办事项的具体内容**

这里修改的表单中如果不填入内容，就默认不改变

![](https://d3dr1ze7164817.cloudfront.net/items/3Y310U403T0a0w2p2m00/Screen%20recording%202017-05-14%20at%2006.15.32%20PM.gif?X-CloudApp-Visitor-Id=2759577)


5. **列出所有的未完成的待办事项**

![](https://d3dr1ze7164817.cloudfront.net/items/192E0x2d3P222L0c0a0m/Screen%20recording%202017-05-14%20at%2006.21.39%20PM.gif?X-CloudApp-Visitor-Id=2759577)


6. **支持按照不同的方式排序**

目前设计的有 **按创建时间排序（默认）, 按过期时间排序 , 按优先级排序**

![](https://d3dr1ze7164817.cloudfront.net/items/1P0M1F1A081t3N1P2z13/Screen%20recording%202017-05-14%20at%2006.23.44%20PM.gif?X-CloudApp-Visitor-Id=2759577)


### 改进方向

1. 列表界面支持翻页
2. 把Sqlite换成PostgreSQL
2. 使用React,Redux构建界面,美化界面
