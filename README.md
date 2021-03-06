# 简单网页项目
1. 基于多种DB&Redis的后台
2. 基于 Flask 后台
3. 基于 Bootstrap 前端
4. 持续演进

## 关于静态文件
- 在掌握Nginx配置后, 部署时应将动静文件分开部署;
- 自动构建过程完成动态部分部署，静态文件需手动上传静态文件位置到CDN地址;

## 关于根据数据库自动生成模型映射文件
```
自动生成model的语法如下：
flask-sqlacodegen "mysql://root:123456@127.0.0.1/movie_cat" --tables user --outfile "common/models/user.py"  --flask
```


## DButils
### PooledDB
- 为了使用 PooledDB 模块，你首先需要通过创建 PooledDB 来设置数据库连接池，传递如下参数：
- dbapi: 需要使用的DB-API 2模块
- mincached : 启动时开启的空连接数量(缺省值 0 意味着开始时不创建连接)
- maxcached: 连接池使用的最多连接数量(缺省值 0 代表不限制连接池大小)
- maxshared: 最大允许的共享连接数量(缺省值 0 代表所有连接都是专用的)如果达到了最大数量，被请求为共享的连接将会被共享使用。
- maxconnections: 最大允许连接数量(缺省值 0 代表不限制)
- blocking: 设置在达到最大数量时的行为(缺省值 0 或 False 代表返回一个错误；其他代表阻塞直到连接数减少)
- maxusage: 单个连接的最大允许复用次数(缺省值 0 或 False 代表不限制的复用)。当达到最大数值时，连接会自动重新连接(关闭和重新打开)
- setsession: 一个可选的SQL命令列表用于准备每个会话，如 ["set datestyle to german", ...]
- 其他，你可以设置用于传递到真正的DB-API 2的参数，例如主机名、数据库、用户名、密码等。
