# 提供前端可以讓建立 github 專案與部署 vercel 完全自動化
2023-04-05 Bowen Chiu

###

. 請幫我建構前後端，都使用 fastapi app.py 單一檔案不要有額外的檔案出現
. 前端使用 bootstrap RWD 排版要整齊, 手機也要能用, 引用 bootstrap 時不要 integrity 屬性
. 前端要能輸入以下參數 001 to 007
    . 環境變數
        001 <your-github-access-token>
        002 <your-vercel-access-token>
    . git_clone 
        003 <source_url> 
        004 <target_name>
    . vercel_deploy
        005 <github_repo_url> 
        006 <vercel_project_name> 
        007 <vercel_team_id>
. 前端參數輸入之後儲存在瀏覽器的 localStorage
. 如果 localStorage 沒有這些參數就預設是空的輸入框
. 如果 localStorage 已經有 001 to 007 參數，事先帶入預設值放上去
. 前端要有一個「送出」按鈕，可以把參數送給後端
. 前端要有一個較大塊的返回顯示區域，專門用來顯示後端執行之後的返回結果
. 送出按鈕按下去之後，要能夠把後端返回哪些成功或失敗的訊息，全部顯示在返回顯示區域
. fastapi 後端接收到 001 to 007 參數之後，返回一個 json 說明 OK 成功
