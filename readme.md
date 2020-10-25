# 中南大学nCov健康打卡定时自动脚本（服务器版）

**注意**：本service分支的代码用于部署在个人服务器中，如无服务器，请使用master分支的Github-Actions版，参考其readme文件进行配置。

## Description

**特此声明**：项目用于学习交流，仅用于各项无异常时打卡，如有身体不适等情况还请自行如实打卡！

* 可定时，默认为每天7点5分
* 默认每次提交上次所提交的内容（只有时间部分更新）

![](https://raw.githubusercontent.com/lxy764139720/Figurebed/master/img/20200410105518.jpg)

## Usage

### Linux

1. clone本项目（为了加快clone速度，可以指定clone深度`--depth 1`，只克隆最近一次commit），并cd到本目录，并切换到service分支
    ```bash
    $ git clone https://github.com/lxy764139720/Auto_Attendance.git --depth 1
    $ cd Auto_Attendance
    $ git checkout service
    ```
    
2. 安装依赖

    ```bash
    $ pip3 install -r requirements.txt
    ```

3. 修改 config.json 中的配置，eai-sess和UUkey的获取见下
  
    * 注意：该文件需用utf-8格式编码
    
    ```Json
    {
     "username": "你的中南大学学工号",
      "password": "你的中南大学信息门户密码",
      "schedule": {
        "hour": "7",
        "minute": "5"
      },
      "cookie": {
        "eai_sess": "你的eai-sess cookie",
        "UUkey": "你的UUkey cookie"
      }
    }
    ```

4. 启动定时自动打卡脚本

   ```bash
   $ python3 auto.py
   ```

### Windows

1. 通过GitHub下载本项目的Zip压缩包，或直接点击下方链接进行下载

   [Download Zip](https://github.com/lxy764139720/Auto_Attendance/archive/master.zip)

2. 安装依赖

   ```powershell
   pip install APScheduler requests halo urllib3 -i https://pypi.tuna.tsinghua.edu.cn/simple
   ```

   

3. 解压文件，修改 config.json 中的配置，eai-sess和UUkey的获取见下
    * 注意：该文件需用utf-8格式编码

   ```Json
   {
    "username": "你的中南大学学工号",
     "password": "你的中南大学信息门户密码",
     "schedule": {
       "hour": "7",
       "minute": "5"
     },
     "cookie": {
       "eai_sess": "你的eai-sess cookie",
       "UUkey": "你的UUkey cookie"
     }
   }
   ```

4. 双击auto.py即可启动定时自动打卡脚本

## Cookie

获取eai-sess和UUkey

1. 打开浏览器，按F12调出控制台

2. 打开Network选项，勾选Preserve log

   ![](https://raw.githubusercontent.com/lxy764139720/Figurebed/master/img/20200410114231.jpg)

3. 打开[健康打卡页面](https://wxxy.csu.edu.cn/ncov/wap/default/index)

4. 若跳转至此页面，输入学工号与门户密码进行登录![](https://raw.githubusercontent.com/lxy764139720/Figurebed/master/img/20200410114831.jpg)

5. 在左侧找到info并点开，在右侧找到Request Headers，将Cookie中的eai-sess和UUkey复制到config.json中保存即可![](https://raw.githubusercontent.com/lxy764139720/Figurebed/master/img/20200410115438.jpg)

如果以上方法未能找到info页面和Cookie中的eai-sess和UUke，请尝试按下图方法搜索：

1. 打开Network选项，勾选Preserve log![](https://raw.githubusercontent.com/lxy764139720/Figurebed/master/img/20200915000353.png)

2. 点击放大镜处的搜索按钮![](https://raw.githubusercontent.com/lxy764139720/Figurebed/master/img/20200915000637.png)

3. 搜索eai-sess![](https://raw.githubusercontent.com/lxy764139720/Figurebed/master/img/20200915000915.jpg)

4. 搜索UUkey![](https://raw.githubusercontent.com/lxy764139720/Figurebed/master/img/20200915001018.jpg)

---

参考开源仓库：

1. [浙大nCov健康打卡定时自动脚本](https://github.com/Tishacy/ZJU-nCov-Hitcarder)
2. [北京化工大学COVID-19自动填报脚本](https://github.com/W0n9/BUCT_nCoV_Report)