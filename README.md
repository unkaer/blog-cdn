# blog-cdn
储存网站所用资源
发布后用[jsdelivr](https://www.jsdelivr.com/)加速访问

完全省略版本以获取最新版本
你不应该在生产中使用这个
```bash
https://cdn.jsdelivr.net/gh/unkaer/blog-cdn/images/background.webp
```
添加 / 在末尾获取目录列表
```bash
https://cdn.jsdelivr.net/gh/unkaer/blog-cdn/
```
直接访问文件
```bash 
https://raw.githubusercontent.com/unkaer/blog-cdn/master/apkupdate/com.vipvideos.unkaer/v
```
某一键脚本
```bash
wget -N --no-check-certificate https://raw.githubusercontent.com/unkaer/blog-cdn/ssr.sh && chmod +x ssr.sh && bash ssr.sh
```
原版
```bash
wget -N --no-check-certificate https://raw.githubusercontent.com/ToyoDAdoubi/doubi/master/ssr.sh && chmod +x ssr.sh && bash ssr.sh
```
