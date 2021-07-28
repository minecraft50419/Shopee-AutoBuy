from auto_buy import Login
import time
from os import system, name
from copy import deepcopy

from rich.console import Console, JustifyMethod
from rich.padding import Padding
from rich.panel import Panel
from rich.table import Table

from data_structure import DataToJSON,Jdata_export,data_template

console = Console()


def LoginPage():
    Login()

def CreatePlanPage():
    ClearScreen()

    copy_data_template = deepcopy(data_template)

    text_1 = Padding("創建計畫", 2)
    console.print(text_1, style="bold cyan", justify="center")


    copy_data_template["website"]=input("  搶購網址: ")

    console.print("")
    console.print("-----------------------------",justify="center",style="bold")
    console.print("由先到後排列",justify="center")
    console.print('商品樣式用 "空格" 區隔',justify="center")
    console.print("-----------------------------",justify="center",style="bold")
    console.print("")

    copy_data_template["items_keywords"]=input("  商品樣式: ").split( )
    copy_data_template["items_values"]=input("  商品數量: ")

    console.print("")
    console.print("-----------------------------",justify="center",style="bold")
    console.print("由先到後排列",justify="center")
    console.print('輸入數字 並用 "空格" 區隔',justify="center")
    console.print('0=貨到付款  1=信用卡金融卡  2=銀行轉帳',justify="center",style="bold bright_black")
    console.print("-----------------------------",justify="center",style="bold")
    console.print("")

    copy_data_template["payment_method"]=input("  付款方式: ").split( )
    a=0
    for i in copy_data_template["payment_method"]:
        if i=="0": copy_data_template["payment_method"][a]="貨到付款"
        if i=="1": copy_data_template["payment_method"][a]="信用卡/金融卡"
        if i=="2": copy_data_template["payment_method"][a]="銀行轉帳"
        a+=1

    console.print("")
    console.print("-----------------------------",justify="center",style="bold")
    console.print("由先到後排列",justify="center")
    console.print('輸入數字 並用 "空格" 區隔',justify="center")
    console.print(' 0=7-11 1=萊爾富 2=全家 3=OK超商 4=黑貓宅急便',justify="center",style="bold bright_black")
    console.print("-----------------------------",justify="center",style="bold")
    console.print("")

    copy_data_template["delivery_method"]=input("  運送方式: ").split( )
    a=0
    for i in copy_data_template["delivery_method"]:
        if i=="0": copy_data_template["delivery_method"][a]="7-11"
        if i=="1": copy_data_template["delivery_method"][a]="萊爾富"
        if i=="2": copy_data_template["delivery_method"][a]="全家"
        if i=="3": copy_data_template["delivery_method"][a]="OK MART"
        if i=="4": copy_data_template["delivery_method"][a]="黑貓宅急便"
        a+=1

    console.print("")
    console.print("-----------------------------",justify="center",style="bold")
    console.print("輸入搶購日期",justify="center")
    console.print('格式為 2021/07/35 12:00',justify="center")
    console.print("-----------------------------",justify="center",style="bold")
    console.print("")

    copy_data_template["times"]=input("  搶購時間: ")

    DataToJSON(copy_data_template)


def All_Plan_Page():
    ClearScreen()
    listData=Jdata_export()
    text_1 = Padding("查看目前計畫清單",2,style="bold yellow")
    table = Table(title=text_1,show_lines=True)

    table.add_column("編號",justify="center")
    table.add_column("搶購時間",style="#E74856")
    table.add_column("網址",justify="center")
    table.add_column("商品數量",justify="center")
    table.add_column("付款方式",justify="center")
    table.add_column("運送方式",justify="center")

    i=1
    for data in listData:
        table.add_row(str(i),data['times'],data['website'],data['items_values'],data['payment_method'][0],data['delivery_method'][0])
        i+=1
    console.print(table,justify="center")
    input("  返回主頁面.....")
    MainMenu()

def Exit():
    console.print("離開")
    time.sleep(2)
    system('pause')

def ClearScreen():
    
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def MainMenu():
    ClearScreen()

    text_1 = Padding("Shopee 搶購 ver1.0.0", 2)
    console.print(text_1, style="bold red", justify="center")

    console.print(Panel(Padding("will50419",(0,5)),title="目前帳號"), justify="center")

    console.print(" ")

    console.print(Panel(Padding("7.25蝦皮商城狂購節",(1,5)), title="2021/07/25 12:00"), justify="center")

    console.print(Padding("1.帳號登入",(1,2)), style="bold")

    console.print(Padding("2.創建計畫",(1,2)), style="bold")

    console.print(Padding("3.查看計畫",(1,2)), style="bold")

    console.print(Padding("4.離開",(1,2)), style="bold")
    
    
    num=input(">>> ")    
    if num=='1': LoginPage()
    elif num=='2': CreatePlanPage()
    elif num=='3': All_Plan_Page()
    elif num=='4': Exit()
    else: console.print("輸入錯誤",style="bold red")

MainMenu()
