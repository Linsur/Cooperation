# Html,Css

## Html

```html
<!DOCTYPE html>
<html lang="en">
<head> 页面信息
    <title>Hello</title>
</head>
<body> 网页内容
    <h1>hello world!</h1>
</body>
</html>
```

完整的html程序包括head部分和body部分。



### title

多级标题

```html
<h1></h1>
<h2></h2>
...
<h6></h6>
```



### list

有序列表(An Ordered list)

```html
<ol>
	<li>first item</li>
    <li>second item</li>
    <li>third item</li>
</ol>
```

无序列表(An unorderd list)

```html
<ul>
	<li>one item</li>
    <li>another item</li>
    <li>yet another</li>
</ul>
```



### image

```html
<body>
	<img src="cat.jpg" alt="Cat" width="300"> 避免出现图像无法显示时，使用alt替代文本
</body>
```



### table

```html
<body>
	<table>
        <thead>
            <tr>
                <th>Ocean</th>
            	<th>Average Depth</th>
            	<th>Maximum Depth</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Pacidic Ocean</td>
                <td>4,280 m</td>
                <td>10,911 m</td>
            </tr>
            <tr>
                <td>Atlantic Ocean</td>
                <td>3,646 m</td>
                <td>8.486 m</td>
            </tr>
        </tbody>
    </table>
</body>
```



### form

```html
<body>
	<form>
		<input type="text" placeholder="Full Name" name="name">
		<input type="submit">
	</form>
</body>
```



```html
<body>
    <div> 
       <input name="name" type="text" placeholder="Name">
       <input name="password" type="password" placeholder="Password">
    </div>
    
    <div>
        <input name="color" type="radio" value="red">Red
        <input name="color" type="radio" value="Green">Green
        <input name="color" type="radio" value="Blue">Blue
        <input name="color" type="radio" value="Other">other
    </div>
</body>

```



### style

```html
<style>
    h1 {
        color:blue;
        text-align:center;
    }
</style>
```



可将style部分写到styles.css文件中。

在读取css文件时，需要使用link来链接

```html
<!DOCTYPE html>
<html lang="en">
<head> 页面信息
    <title>Hello</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body> 网页内容
    <h1>hello world!</h1>
</body>
</html>
```



## Css



### size

```css
background-color: organe;
width: 200px; 
height: 200px;
padding: 20px 填充
margin: 20px; 边距
```



### font

```css
font-family: Arial, sans-serif;
font-size: 28px;
font-weight: bold;
```



### border

```css
border: 3px; 边框
border-collapse: collapse; 折叠边框
```

 

### id（唯一HTML元素命名方式）

```html
html

<!DOCTYPE html>
<html lang="en">
<head> 页面信息
    <title>Hello</title>
</head>
<body> 网页内容
    <h1 id="foo">heading 1</h1>
    <h1>heading 2</h1>
    <h1>heading 3</h1>
</body>
</html>
```

```css
Css

#foo{
	color：blue；
}
```



### class（HTML元素命名方式）

```html
html

<!DOCTYPE html>
<html lang="en">
<head> 
    <title>Hello</title>
</head>
<body> 
    <h1 class="baz">heading 1</h1>
    <h1 class="baz">heading 2</h1>
    <h1>heading 3</h1>
</body>
</html>
```

```css
Css

.baz{
	color: Blue;
}
```



### Css Specificity（具体性）

1. inline 内联
2. id 唯一标识
3. class 类
4. type 类型


### Css Selectors


```html
Html

<!DOCTYPE html>
<html lang="en">
<head> 
    <title>Hello</title>
</head>
<body> 
    <ol>
	<li>list item one</li>
    <li>list item two</li>
    <ul>
        <li>sublist item one</li>
        <li>sublist item two</li>
	</ul>
    <li>list item three</li>
	</ol>
</body>
</html>
```

设置列表中所有元素

```css
Css

li{
	color: blue;
}
```


仅设置无序列表中的元素

```css
Css

ul li{
	color: blue;
}
```



### Attribute Selector

```html
Html

<!DOCTYPE html>
<html lang="en">
<head> 
    <title>Hello</title>
</head>
<body> 
    <ul>
        <li><a href="https://google.com">Google</a></li>
        <li><a href="https://facebook.com">Facebook</a></li>
        <li><a href="https://amazon.com">Amazon</a></li>
	</ul>
</body>
</html>
```

```css
Css

a{
	color: blue
}
```


```css
Css

a{
	color: blue
}
a[href="https://facebook.com"]{
	color: red
}
```



### hover(鼠标悬停时改变样式)

```html
Html

<!DOCTYPE html>
<html lang="en">
<head> 
    <title>Hello</title>
</head>
<body> 
    <button>Click me</button>
</body>
</html>
```

```css
Css

button{
    width: 200px;
    height: 200px;
    font-size: 24px;
    background-color: green;
}

button:hover{
    background-color: orange;
}
```



### Responsive Design

- viewport

```css
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```



```css
Css

@media(min-width: 600px){
	body{
		background-color: red;
	}
}

@media(max-width: 599px){
    body{
        background-color: blue;
    }
}
```



- Flexbox

```html
Html

<!DOCTYPE html>
<html lang="en">
<head> 
    <title>Hello</title>
</head>
<body> 
    <div id="container">
        <div>
            1.This is some sample element
        </div>
        <div>
            2.This is some sample element
        </div>
        <div>
            3.This is some sample element
        </div>
        <div>
            4.This is some sample element
        </div>
        <div>
            5.This is some sample element
        </div>
    </div>
</body>
</html>
```



```css
Css

#container{
	display: flex;
	flex-wrap: wrap;
}

#container > div{
	background-color: springgreen;
	font-size: 20px;
	margin: 20px;
	paddong: 20px;
}
```


- grid

```html
Html

<!DOCTYPE html>
<html lang="en">
<head> 
    <title>Hello</title>
</head>
<body> 
    <div id="grid">
        <div class="grid-item">1</div>
        <div class="grid-item">2</div>
        <div class="grid-item">3</div>
        <div class="grid-item">4</div>
        <div class="grid-item">5</div>
        <div class="grid-item">6</div>
        <div class="grid-item">7</div>
        <div class="grid-item">8</div>
    </div>
</body>
</html>
```



```css
Css

#grid{
	background-color: green;
	display: grid;
	padding: 20px;
	grid-column-gap: 20px;
    grid-row-gap: 10px；
    grid-template-columns: 200px 200px auto;
}

.grid-item{
	background-color: white;
    font-size: 20px;
	margin: 20px;
	paddong: 20px;
}
```


### Boostrap(Css样式库)

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Bootstrap demo</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
  </head>
  <body>
    <h1>Hello, world!</h1>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
  </body>
</html>
```



### variables

```html
Html

<!DOCTYPE html>
<html lang="en">
<head> 
    <title>Hello</title>
</head>
<body> 
    <ul>
        <li>sublist item one</li>
        <li>sublist item two</li>
        <li>sublist item three</li>
	</ul>
    <ol>
        <li>list item one</li>
        <li>list item two</li>
        <li>list item three</li>
	</ol>
</body>
</html>
```



```css
Css

ul{
    font-size: 14px;
    color: red;
}

ol{
    font-size: 18px;
    color: red;
}
```



#### Scss file

当我们想要让两个列表共用color这个属性时候，可以创建scss文件

```scss
Scss

$color: red;

ul{
    font-size: 14px;
    color: $color;
}

ol{
    font-size: 18px;
    color: $color;
}
```

但在引用时注意，网页无法识别scss文件，因此不可直接引用,需要经过编译转换

```shell
sass variables.scss:variables.css
```

现在我们可以引用了

```html
<link rel="stylesheet" href="variables.css"
```

Scss文件自动化转换成Css文件

```shell
sass -watch variables.scss:variables.css
```



##### inheritance(继承)

```scss
%message{ 通用属性
	font-family: sans-serif;
    font-size: 18px;
    font-weight: bold;
    border: 1px solid black;
    padding: 20px;
    margin: 20px;
}

.success{
	@extend %message;
    background-color: green;
}

.warning{
	@extend %message;
    background-color: orange;
}

.error{
	@extend %message;
    background-color: red;
}
```

通过sass转换成css文件后，代码如下

```css
.success, .warning, .error{ 通用属性
	font-family: sans-serif;
    font-size: 18px;
    font-weight: bold;
    border: 1px solid black;
    padding: 20px;
    margin: 20px;
}

.success{
    background-color: green;
}

.warning{
    background-color: orange;
}

.error{
    background-color: red;
}
```
