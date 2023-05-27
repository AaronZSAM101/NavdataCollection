# 定义当前导航周期期号、起止日期、文件路径
AIRAC_CYCLE = input('请输入当前AIRAC周期号(eg.2303):')
DATE = input('请输入起止日期（eg.MAR.23 - APR.19):')
NAIPNavdataPath = input(f'请输入{AIRAC_CYCLE}期的Navdata文件的路径（精确到文件夹）：')
NaviSidstarsPath = input(f'请输入{AIRAC_CYCLE}期的境外Sidstars文件的路径（精确到文件夹）：')
NAIPSidstarsPath = input(f'请输入{AIRAC_CYCLE}期的国内Sidstars文件的路径（精确到文件夹）：')
PublishPath = input(f'请输入{AIRAC_CYCLE}期导航数据的存储路径（精确到文件夹）：')

# 新建一个新文件夹以存放文件
import os
os.mkdir(os.path.join(PublishPath, f"PMDG nAIP {AIRAC_CYCLE}"))
os.mkdir(os.path.join(PublishPath, f"PMDG nAIP {AIRAC_CYCLE}", "Navdata"))
os.mkdir(os.path.join(PublishPath, f"PMDG nAIP {AIRAC_CYCLE}", "Sidstars"))

# 复制转换好的Navdata文件到刚才新建的文件夹
import shutil
shutil.copy(os.path.join(NAIPNavdataPath,'airports.dat'),os.path.join(PublishPath, f"PMDG nAIP {AIRAC_CYCLE}", "Navdata"))
shutil.copy(os.path.join(NAIPNavdataPath,'wpNavAID.txt'),os.path.join(PublishPath, f"PMDG nAIP {AIRAC_CYCLE}", "Navdata"))
shutil.copy(os.path.join(NAIPNavdataPath,'wpNavAPT.txt'),os.path.join(PublishPath, f"PMDG nAIP {AIRAC_CYCLE}", "Navdata"))
shutil.copy(os.path.join(NAIPNavdataPath,'wpNavFIX.txt'),os.path.join(PublishPath, f"PMDG nAIP {AIRAC_CYCLE}", "Navdata"))
shutil.copy(os.path.join(NAIPNavdataPath,'wpNavRTE.txt'),os.path.join(PublishPath, f"PMDG nAIP {AIRAC_CYCLE}", "Navdata"))

# 新建一个cycle_info.txt 和 fmc_ident.txt
with open(os.path.join(PublishPath, f"PMDG nAIP {AIRAC_CYCLE}", "Navdata", "cycle_info.txt"), 'w') as f:
    f.write(f'AIRAC: {AIRAC_CYCLE}({DATE})\n \nData: CAAC-AISC\n \nRMK:\n1. Only for flight simulation.\n  Any form of reverse extraction engineering is strictly prohibited \n2. NOT TO PUBLIC WITHOUT ANY PERMISSION')
with open(os.path.join(PublishPath, f"PMDG nAIP {AIRAC_CYCLE}", "Navdata", "fmc_ident.txt"), 'w') as f:
    f.write(f'[Ident]\nNavdata=NAIP-{AIRAC_CYCLE}\nOpProgram={DATE.replace(".","").replace(" ","").replace("-","")}/{AIRAC_CYCLE[:2]}\nCoData=CAAC-{AIRAC_CYCLE}')

# 复制公版Sidstars的境外机场
NaviFilesnames=os.listdir(NaviSidstarsPath)
for file in NaviFilesnames:
    if file[:2] not in ["ZB","ZG","ZH","ZL","ZP","ZS","ZU","ZW","ZY"]:
        shutil.copy(os.path.join(NaviSidstarsPath, file),os.path.join(PublishPath, f"PMDG nAIP {AIRAC_CYCLE}", "Sidstars"))

# 复制模拟器路径下的中国大陆机场的文件
NAIPFilesnames=os.listdir(NAIPSidstarsPath)
for file in NAIPFilesnames:
    shutil.copy(os.path.join(NAIPSidstarsPath, file), os.path.join(PublishPath, f"PMDG nAIP {AIRAC_CYCLE}", "Sidstars"))

# 将文件打包成压缩包
shutil.make_archive(os.path.join(PublishPath,f"PMDG nAIP {AIRAC_CYCLE}"), "zip", os.path.join(PublishPath, f"PMDG nAIP {AIRAC_CYCLE}"))

# 退出程序
input("导航数据生成并打包完成，按回车键开瘾！")