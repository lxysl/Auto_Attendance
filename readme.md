# 中南大学nCov健康打卡定时自动脚本（服务器版）

**注意**：本service分支的代码用于部署在个人服务器中，如无服务器，请使用master分支的Github-Actions版，参考其readme文件进行配置。

如本项目对您有所帮助，请帮忙点一个⭐star支持一下作者，您的鼓励是我持续维护和优化本项目的动力。如有任何问题欢迎提交issue与我联系。

## Description

**特此声明**：项目用于学习交流，仅用于各项无异常时打卡，如有身体不适等情况还请自行如实打卡！

* **[本次更新内容]**仅需输入中南大学学工号和中南大学信息门户密码即可进行自动打卡（不再需要手动输入cookie）
* 可设置自动打卡时间，默认为每天7点5分
* 默认每次提交上次所提交的内容（只有日期部分更新）
* **位置信息与上一次打卡的位置相同**，即使下次打卡时您的定位改变也不会对打卡位置造成影响。如需变更打卡位置，可以在当天打卡时间前手动定位打卡，之后的位置信息会随之改变

![](https://raw.githubusercontent.com/lxy764139720/Figurebed/master/img/20200410105518.jpg)

## Usage

### Linux

1. clone本项目，cd到本目录，并切换到service分支
    ```bash
    $ git clone https://github.com/lxy764139720/Auto_Attendance.git
    $ cd Auto_Attendance
    $ git checkout service
    ```
    
2. 安装依赖

    ```bash
    $ pip3 install -r requirements.txt
    ```

3. 修改 config.json 中的配置
  
    * 注意：该文件需用utf-8格式编码
    
    ```Json
    {
     "username": "你的中南大学学工号",
      "password": "你的中南大学信息门户密码",
      "schedule": {
        "hour": "7",
        "minute": "5"
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

3. 解压文件，修改 config.json 中的配置
    * 注意：该文件需用utf-8格式编码

   ```Json
   {
    "username": "你的中南大学学工号",
     "password": "你的中南大学信息门户密码",
     "schedule": {
       "hour": "7",
       "minute": "5"
     }
   }
   ```

4. 双击auto.py即可启动定时自动打卡脚本

---

参考开源仓库：

1. [浙大nCov健康打卡定时自动脚本](https://github.com/Tishacy/ZJU-nCov-Hitcarder)
2. [北京化工大学COVID-19自动填报脚本](https://github.com/W0n9/BUCT_nCoV_Report)