# discord_bot_bemo

Bemo 是一個非常簡單的Discord機器人，目前的功能是進行一些簡單的指令：


在管理成員的方面可以執行如：將成員在語音頻道間移動、更改成員在伺服器的暱稱。

另外還有一些有趣小功能如：從解答之書中隨機挑一個答案、從給予的成員名單中隨機抽選一位。

大多數的管理功能是我在使用Discord時覺得很實用的，才寫進來，所以目前的功能還非常少。

得益於目前的架構，新增指令只需要在./cmds/cmd.py中新增function，對於任何指令的開發都非常方便。

若要使用，僅須將./datas/setting.json 中之的 "Your TOKEN" 改為你的Bot token，即可正常運作。
