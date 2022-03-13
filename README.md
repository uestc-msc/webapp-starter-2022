# webapp-starter-2022

Start your first web application with Vue 3 and Django 4!

## 2022.2.26

[录屏](http://b23.tv/awoyG9Y)

### Web 开发的门槛

* 任意一门编程语言，主要是了解变量、循环结构、分支结构、函数、类（或结构体）的概念

### Web 开发分工

* 前端：把数据展示到页面上
* 后端：把数据从数据库里拿出来给前端

### 编程语言和框架

* 后端：Java(Spring Boot), Go(Gin), Python(Flask, **Django**), JavaScript(Node.js, Express.js), Ruby(Rails)
* 前端：JavaScript(**Vue.js**, React.js, Angular.js)

### 配置环境

* Node.js
* npm (Node Package Manager) / yarn / pnpm
* 换镜像源
* git（可选）
* IDE（前端）：Visual Studio Code / IntelliJ IDEA Ultimate / WebStorm
* IDE（后端）：Visual Studio Code / IntelliJ IDEA Ultimate / PyCharm

* GitHub Copilot（可选）

### 前端用到的技术

* Vue 3
* TypeScript
* Vuetify 3 (组件库)
* Vite (Webpack)
* ESLint + Prettier

### TypeScript

C 语言：

```c
int sum(int n) {
    int s = 0;
    for (int i = 0; i < n; i++) {
        s += i;
    }
    return s;
}
```

JavaScript：

```js
function sum(n) {
    let s = 0;
    for (let i = 0; i < n; i++) {
        s += i;
    }
    return s;
}
```

TypeScript 提供了类型推导，大大提高了项目的可维护性：

```ts
function sum(n: Number) {
    let s: Number = 0;
    for (let i = 0; i < n; i++) {
        s += i;
    }
    return s;
}
```

### 安装、运行 demo

```
pnpm i
```

点击 `package.json` 的绿色箭头，或执行 `pnpm run dev` 启动项目。

去组件库的文档里面找代码，把它拷贝到项目里，然后运行即可创建一个最简单的组件。


## 2020.3.12

## 前后端交互协议

交互协议：**http**/grpc/websocket

数据格式：xml/**json**/protobuf

REST API：**GET**/**POST**/**PUT**/**DELETE**

Django REST Framework

## 数据库配置

Docker + PostgreSQL

```shell
docker run -d --name django_starter_postgres -p 5432:5432 -e POSTGRES_PASSWORD=test --restart always postgres
```

## url 接上函数 -- 路由 / 指路

[urls.py](django-starter/django_starter/urls.py)

## 编写 models

[models.py](django-starter/cards/models.py)

## 编写 serializers

[serializers.py](django-starter/cards/serializers.py)

## 编写 views

[views.py](django-starter/cards/views.py)

[urls.py](django-starter/cards/urls.py)
