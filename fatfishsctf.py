import base64
import os

def decode_logic(data):
    """纯粹的解码逻辑。如果成功，返回 True；如果失败，返回 False"""
    data = data.replace('\n', '').replace('\r', '').replace(' ', '')
    
    # 【防空拦截】
    if not data:
        print("\n[提示] 输入为空，已取消解码。")
        return False
        
    count = 0
    while True:
        count += 1
        try:
            decoded = base64.b64decode(data, validate=True).decode('utf-8')
        except Exception:
            print(f"\n第 {count} 层解码结束/失败。")
            print("==================================")
            print(f"最终结果：\n{data}")
            print("==================================")
            return True  # 报错了说明到底了，但也是解出结果了，返回成功
            
        # 【死循环拦截】
        if decoded == data:
            print("\n[提示] 解码无变化，停止运行。")
            return True
            
        data = decoded
        print(f"第 {count} 层解码结果：{decoded[:30]}...")

if __name__ == "__main__":
    # 用 while True 开启主菜单循环
    while True:
        print("\n==============================")
        print("【CTF 解码小工具】")
        print("1. 自动读取当前目录下的文件")
        print("2. 手动粘贴 Base64 字符串")
        print("3. 退出程序")
        print("==============================")
        
        mode = input("请输入 1、2 或 3 并回车：")

        if mode == '1':
            file_name = input("请输入你要读取的文件名（例如 test1.txt）：\n")
            if os.path.exists(file_name):
                with open(file_name, 'r', encoding='utf-8') as f:
                    content = f.read()
                print(f"\n[成功] 已读取 {file_name}，开始自动解码...\n")
                decode_logic(content) 
            else:
                print(f"\n[错误] 找不到文件 {file_name}，请确认它在这个目录下。")
                # 报错后不退出，自动回到上面的 while True 重新显示菜单

        elif mode == '2':
            text = input("\n请粘贴你的 Base64 字符串，然后回车：\n")
            print("\n开始解码...\n")
            decode_logic(text)
            # 解码完自动回到菜单

        elif mode == '3':
            print("\nbye！")
            break  # 只有输入 3 才会打破循环，退出程序
            
        else:
            print("\n[错误] 输入无效，只能输入 1、2 或 3。")
            # 输错后自动回到菜单
