# 中南大学nCov健康打卡定时自动脚本（Github-Actions版）

**注意**：本master分支版本代码使用Github-Actions定时运行，无需部署在服务器。如需在服务器中运行，请使用service分支中的代码。

如本项目对您有所帮助，请帮忙点一个⭐star支持一下作者。如果您想更进一步，可以点击💗Sponsor请我喝杯冰可乐。您的鼓励是我持续维护和优化本项目的最大动力。如有任何问题欢迎提交issue或discussion与我联系，在反馈前请仔细阅读Issues区的[使用说明](https://github.com/lxy764139720/Auto_Attendance/issues/13)哦。

## Description

**特此声明**：项目用于学习交流，仅用于各项无异常时打卡，如有身体不适等情况还请自行如实打卡！

* [**本次更新内容**]由[@hidragonma](https://github.com/hidragonma)修复了[五一节后的打卡故障](https://github.com/hidragonma)，感谢贡献代码！
* 仅需输入中南大学学工号和中南大学信息门户密码即可进行自动打卡（不再需要手动获取cookie）
* 可[设置自动打卡时间](#dksj)，默认为每天7点5分
* 默认每次提交上次所提交的内容（只有日期部分更新）
* **位置信息与上一次打卡的位置相同**，即使下次打卡时您的定位改变也不会对打卡位置造成影响。如需变更打卡位置，可以在当天打卡时间前手动定位打卡，之后的位置信息会随之改变
* Github-Actions打卡失败时会通过Github通知邮件发送至绑定的邮箱（需要手动设置Github账号绑定的邮箱）
* 您的学号和密码均以秘钥形式保存在您的Github仓库中，其他人无法查看

![](https://i.loli.net/2020/12/06/qG5X4pUNYyTDaCz.png)

![20200817190036](https://i.loli.net/2020/12/06/e5zZgs6BFDN3IUA.png)

## Usage

### 运行方式

1. fork本项目到你的个人账号
   
2. 设置Secrets

    从Github中进入刚刚fork到你的个人账号下的本项目，打开项目的Settings->Secrets页面
    

![20201206004701](https://i.loli.net/2020/12/06/cegmk76uprEvHU5.png)

* 点击New repository Secret按钮创建第一个仓库密码

  在Name栏中输入大写字符串 **USERNAME** ，在Value栏中输入你的中南大学学工号，点击Add secret按钮保存

* 再次点击New repository Secret按钮创建第二个仓库密码

  在Name栏中输入大写字符串 **PASSWORD** ，在Value栏中输入你的中南大学信息门户密码，点击Add secret按钮保存

3. 启动定时打卡

    方法一：手动开启工作流（推荐）

    进入Actions页面，点击该工作流，点击Run workflow按钮

    ![eIhPdkpV6QqzbJ1](https://i.loli.net/2020/12/06/eIhPdkpV6QqzbJ1.png)

    手动开启工作流的功能由[@sumowi](https://github.com/sumowi)通过/.github/workflows/python-package.yml文件中的workflow_dispatch实现

    方法二：修改Readme以自动触发Github-Actions工作流

    进入Code页面，点击修改按钮

    ![20200817191741](https://i.loli.net/2020/12/06/DHy13dsNSxrchVz.png)

    在readme文件中随意修改任意字符（比如加个空格），然后点击下方的Commit Changes即可激活每日定时打卡脚本

    ![20200817192122](https://i.loli.net/2020/12/06/1W6x2wIBOTCVl7K.png)

4. 查看运行情况

    打开Actions页面，此时在workflows中应该出现了正在运行的工作流。当提交文件时会马上进行一次打卡，以后将会默认在每天的7:05进行打卡

    如果打卡失败请重新运行workflows并检查账号密码设置是否正确
    
    ![20200817192416](https://i.loli.net/2020/12/06/P31tu5einhLpArk.png)

## <span id="dksj">修改打卡时间</span>

打开项目中的/.github/workflows/python-package.yml文件，修改corn中的值，注意使用UTC零区时间。

例如，当前默认打卡时间是北京时间(UTC+8)每天7:05，换算成UTC零区时间为23:05。

更多关于时间的具体书写格式请参考[POSIX cron 语法](https://crontab.guru/)和[官方文档](https://docs.github.com/cn/actions/reference/events-that-trigger-workflows#)。

![20200817194102](https://i.loli.net/2020/12/06/zqXQvYCJwfrN3Pc.png)

![20200817194250](https://i.loli.net/2020/12/06/oRjts1Yy5NV9TI8.png)

---
参考开源仓库：

1. [浙大nCov健康打卡定时自动脚本](https://github.com/Tishacy/ZJU-nCov-Hitcarder)
2. [北京化工大学COVID-19自动填报脚本](https://github.com/W0n9/BUCT_nCoV_Report)

鸣谢：

[@sumowi](https://github.com/sumowi)

[@hidragonma](https://github.com/hidragonma)
