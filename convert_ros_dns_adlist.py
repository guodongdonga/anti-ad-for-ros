# @bilibili:果冻冻啊
# https://space.bilibili.com/7974766
# 从anti-ad获取过滤列表，转换为ros可用的adlist
import os
import requests


def down_load_from_anti_ad():
    # 从https://github.com/privacy-protection-tools/anti-AD 获取最新的广告过滤列表
    # 我们可以从https://anti-ad.net/domains.txt这里下载

    # 设置要下载的文件的URL
    url = 'https://anti-ad.net/domains.txt'

    # 发送HTTP请求获取文件内容
    response = requests.get(url)

    # 检查请求是否成功
    if response.status_code == 200:
        # 文件名用url里面的
        filename = url.split('/')[-1]
        # 保存文件到当前目录
        with open(filename, 'wb') as file:
            file.write(response.content)
        print(f'文件已下载并保存为 {filename}')
    else:
        print('文件下载失败，状态码：', response.status_code)


def convert():
    # 检查当前目录是否有domains.txt
    if os.path.exists('/home/runner/work/anti-ad-ros/anti-ad-ros/code/anti-ad-domains.txt'):
        # 执行转换
        # 打开文件进行读取
        with open('/home/runner/work/anti-ad-ros/anti-ad-ros/code/anti-ad-domains.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()

        # 打开文件进行写入，创建新文件anti-ad-ros.conf
        with open('anti-ad-for-ros.conf', 'w', encoding='utf-8') as file:
            # 写入一行注释说明
            # file.write('# ROS dns adlist, converted from anti-ad.net\n')
            # 遍历每一行，跳过注释行，并在非注释行前加上0.0.0.0
            for line in lines:
                if not line.startswith('#'):
                    # 删除行首尾的空白字符（如果有的话）
                    line = line.strip()
                    # 跳过空行
                    if line:
                        # 在行前加上0.0.0.0 和一个空格
                        file.write('0.0.0.0 {}\n'.format(line))

        print("文件转换完成。")
    else:
        print('没有找到anti-ad-domains.txt，可能clone失败了')
        # print当前目录内容
        print(os.listdir())
        # print /home/runner/work/anti-ad-ros/anti-ad-ros/目录的内容
        print(os.listdir('/home/runner/work/anti-ad-ros/anti-ad-ros/'))


if __name__ == '__main__':
    # 1. 下载文件
    # down_load_from_anti_ad()
    # 2. 格式转换
    convert()
    # 3. 导入ros即可使用
