### Android 文档

##### 开发环境搭建

1.在工程目录下新建gradle文件config.gradle，并在ext{..}方法下设置一个数组变量;  
例：ext{  
		esss=[  compileSdkVersion :29  
				 buildToolsVersion “29.0.3"  
				 minSdkVersion 26   
				targetSdkVersion 29  				
				]  
}  
  
2.再在工程目录下的build.gradle文件中的首行，应用该文件'apply from:"config.gradle"'：   
3.最后需要在模块的build.gradle文件下调用’rootProject.ext.变量名.键值'即可：  
  
##### 编译代码方式
  
android源码编译的四个流程:  
1.源码下载;  
2.构建编译环境;  
3.编译源码;  
4运行  

##### 如何调试定位问题

·APP崩溃、报错抛异常  
·在左下角Run中 查看报错的原因及位置；    
在没有崩溃的情况下可以用debug调试找出问题；  

##### 大概的代码框架

1.View注入框架 — ButterKnife  
2.APP中列表刷新 — SmartRefresh  
3.APP适配 — autosize  
4.解析json串 — Gson  
5.列表加载 — RecyclerView  
6.事件发布/订阅框架 — EventBus  
7.访问外网 — okhttp  
8.图片加载 — picasso  
9.二维码 — zxing  
