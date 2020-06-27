<%@ page contentType="text/html; UTF-8" pageEncoding="utf-8" isELIgnored="false" %>
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h1>用户上传文件</h1>
    <form action="/files/upload" method="post" enctype="multipart/form-data">
        <input type="file" name="multipartFile"/>
        <input type="submit" value="上传文件"/>
    </form>
    <hr/>
    <h1>用户文件下载</h1>
    <a href="/files/download?filename=下载1.txt">下载1.txt</a>
    <a href="/files/download?filename=下载2.txt">下载2.txt</a>
</body>

</html>