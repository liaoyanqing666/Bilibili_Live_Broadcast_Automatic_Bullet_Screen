# Bilibili_Live_Broadcast_Automatic_Bullet_Screen
Bilibili直播自动发送弹幕，Bilibili live automatically sends bullet



## Chinese Introduction

**切勿使用此程序攻击网站或任何人，此程序仅供个人使用，如弹幕抽奖。**

可以在[这个网址](https://blog.csdn.net/m0_61718615/article/details/146134482)查看详细的使用介绍。

本程序借助了chatgpt4.0的帮助完成。

突发奇想做了一个b站自动发弹幕的小py脚本，可以实现每5~6秒钟发送一条重复弹幕的功能。使用`webdriver` (chromedriver)和`selenium`库配合使用，我第一次尝试写相关代码，可能会有疏漏或者错误。

程序在两种不同的直播间试验过，不过不保证能适配所有直播间。并且随着Bilibili的网站版本更新，可能也会失效。

程序的防 防脚本 功能很弱，使用后被封号后果自负。（不过根据个人账号实验，并未被封）

cookie是用来进行免密登陆的，在已经登陆过的Bilibili网页上按F12，选中“应用”，找到cookie，点开，并把其中对应内容复制过去（有经验的屏蔽此条）。也可以直接全部复制后和chatgpt说把所有相关cookie填写好。

## English Introduction

**Never use this program to attack the website or anyone, this program is only for personal use, such as draw a bullet raffle.**

The program was completed with the assistance of ChatGPT 4.0.

On a whim, I created a small Python script for automatically sending barrage messages on Bilibili. It is capable of sending a repetitive barrage message every 5 to 6 seconds. I used the `webdriver` (chromedriver) and `selenium` library in conjunction. This is my first attempt at writing such code, so there may be omissions or errors.

The program has been tested in two different live rooms, but there is no guarantee that it will work in all live rooms. Additionally, as Bilibili's website undergoes version updates, the program may become ineffective.

The program's anti-anti-script feature is quite weak, so users who choose to use it do so at their own risk of being banned. (However, according to the personal account experiment, it was not banned.)

The cookie is used for password-free login. To obtain it, navigate to a logged-in Bilibili webpage, press F12, select "Application," locate the cookie, open it, and copy the corresponding content (experienced users may skip this step). You can also copy all the cookies directly and ask chatgpt to fill in all the relevant cookies.
