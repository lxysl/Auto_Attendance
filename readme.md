# 中南大学nCov健康打卡定时自动脚本（Github-Actions版）

**注意**：本master分支版本代码使用Github-Actions定时运行，无需部署在服务器。如需在服务器中运行，请使用service分支中的代码。

如本项目对您有所帮助，请帮忙点一个⭐star支持一下作者。如有任何问题欢迎提交issue与我联系。

## Description

**特此声明**：项目用于学习交流，仅用于各项无异常时打卡，如有身体不适等情况还请自行如实打卡！

* 可[设置自动打卡时间](#dksj)，默认为每天7点5分
* 默认每次提交上次所提交的内容（只有时间部分更新）
* 位置信息与上一次打卡的位置相同，如需变更，可以在当天打卡时间前手动定位打卡，之后的位置信息会随之改变
* Github-Actions打卡失败时会通过Github通知邮件发送至绑定的邮箱（需要手动设置Github账号绑定的邮箱）

![](https://raw.githubusercontent.com/lxy764139720/Figurebed/master/img/20200817185806.png)

![](https://raw.githubusercontent.com/lxy764139720/Figurebed/master/img/20200817190036.png)	

## Usage

## 获取Cookie

获取eai-sess和UUkey

1. 打开浏览器，按F12调出控制台

2. 打开Network选项，勾选Preserve log![](https://raw.githubusercontent.com/lxy764139720/Figurebed/master/img/20200410114231.jpg)

3. 打开健康打卡页面[https://wxxy.csu.edu.cn/ncov/wap/default/index](https://wxxy.csu.edu.cn/ncov/wap/default/index)

4. 若跳转至此页面，输入学工号与门户密码进行登录![](https://raw.githubusercontent.com/lxy764139720/Figurebed/master/img/20200410114831.jpg)

5. 在左侧找到info并点开，在右侧找到Request Headers，将Cookie中的eai-sess和UUkey记录下来![](https://raw.githubusercontent.com/lxy764139720/Figurebed/master/img/20200410115438.jpg)

如果以上方法未能找到info页面和Cookie中的eai-sess和UUke，请尝试按下图方法搜索：

1. 打开Network选项，勾选Preserve log![](https://raw.githubusercontent.com/lxy764139720/Figurebed/master/img/20200915000353.png)

2. 点击放大镜处的搜索按钮![](https://raw.githubusercontent.com/lxy764139720/Figurebed/master/img/20200915000637.png)

3. 搜索eai-sess![](https://raw.githubusercontent.com/lxy764139720/Figurebed/master/img/20200915000915.jpg)

4. 搜索UUkey![](https://raw.githubusercontent.com/lxy764139720/Figurebed/master/img/20200915001018.jpg)

### 运行方式

1. fork本项目到你的个人账号
   
2. 设置Secrets

    从Github中进入刚刚fork到你的个人账号下的本项目，打开项目的Settings->Secrets页面
    

![](https://raw.githubusercontent.com/lxy764139720/Figurebed/master/img/20200817190653.png)

​	点击New Secret按钮新建四个密码：

* USERNAME：你的中南大学学工号

* PASSWORD：你的中南大学信息门户密码

* EAI_SESS：你的eai-sess cookie

* UUKEY：你的UUkey cookie

3. 启动定时打卡

    方法一：修改Readme以自动触发Github-Actions工作流

    进入Code页面，点击修改按钮

    ![](https://raw.githubusercontent.com/lxy764139720/Figurebed/master/img/20200817191741.png)

    在readme文件中随意修改任意字符（比如加个空格），然后点击下方的Commit Changes即可激活每日定时打卡脚本

    ![](https://raw.githubusercontent.com/lxy764139720/Figurebed/master/img/20200817192122.png)

    方法二：手动开启工作流

    进入Actions页面，点击该工作流，点击Run workflow按钮

    ![](https://github.com/sumowi/sumowi.github.io/blob/master/image/2.png)  

    手动开启工作流的功能由[@sumowi](https://github.com/sumowi)通过/.github/workflows/python-package.yml文件中的workflow_dispatch实现

    ![](https://github.com/sumowi/sumowi.github.io/blob/master/image/1.png)  

4. 查看运行情况

    打开Actions页面，此时在workflows中应该出现了正在运行的工作流。当提交文件时会马上进行一次打卡，以后将会默认在每天的7:05进行打卡

    ![](https://raw.githubusercontent.com/lxy764139720/Figurebed/master/img/20200817192416.png)

## <span id="dksj">修改打卡时间</span>

打开项目中的/.github/workflows/python-package.yml文件，修改corn中的值，注意使用UTC零区时间。

例如，当前默认打卡时间是北京时间(UTC+8)每天7:05，换算成UTC零区时间为23:05。

更多关于时间的具体书写格式请参考[POSIX cron 语法](https://crontab.guru/)和[官方文档](https://docs.github.com/cn/actions/reference/events-that-trigger-workflows#)。

![](https://raw.githubusercontent.com/lxy764139720/Figurebed/master/img/20200817194102.png)

![](https://raw.githubusercontent.com/lxy764139720/Figurebed/master/img/20200817194250.png)

---
参考开源仓库：

1. [浙大nCov健康打卡定时自动脚本](https://github.com/Tishacy/ZJU-nCov-Hitcarder)
2. [北京化工大学COVID-19自动填报脚本](https://github.com/W0n9/BUCT_nCoV_Report)

鸣谢：

[@sumowi](https://github.com/sumowi)
