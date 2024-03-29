import os
import time
import requests
import random
import threading

# 这个主要用来查bili用户的基础信息



class gugufan():
    def __init__ (self,filename):
        #创建一个文件夹先，免得下一堆ts文件
        try:
            os.makedirs("./ts_files")
        except:
            pass
        #下载标志位
        self.i=0
        #下载的ts文件
        self.filename = f"ts_files/{filename}{self.i}.ts"
        #合成输出的文件名
        self.filemerge = filename+".mp4"
        #emm忘了什么了，使用日志？
        self.__userdate__=""
        #下载失败的文件，后面出现的连续数字十有八九是多余的
        #主要看前面是否有断断续续的数字
        self.fail=[]

        


    # download
    def __download_content__(self,i):
        url=f"https://a95.yizhoushi.com/acgworld/videos/202403/24/65ff827619e8b73b239c0e93/98ecf5/index{i}.ts"
        head={
            'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0'
            }
        
        pa={
            # 留备用）
        }

        proxies = ['HTTP://110.243.30.23:9999', 'HTTP://222.189.191.206:9999', 'HTTP://118.212.104.138:9999',
           'HTTP://182.149.83.97:9999', 'HTTP://106.42.163.100:9999', 'HTTP://120.83.107.69:9999',
           'HTTP://60.13.42.135:9999', 'HTTP://60.205.188.24:3128', 'HTTP://113.195.232.23:9999',
           'HTTP://59.62.36.74:9000', 'HTTP://218.2.226.42:80']
        proxy = {'HTTP': random.choice(proxies)}  #随机选取一个IP


        response = requests.get(url, proxies=proxy, headers=head)
        return response
    
    # 文件写入
    def save_file(self):
        i=self.i
        #睡一会，怕太快了服务器酱受不了
        time.sleep(i)
        print(f"therding:{i}ing")
        try:
            r=self.__download_content__(i)
            #  如果没通则except
            r.raise_for_status()
            r.encoding = "utf-8"
            with open(self.filename, mode="wb") as f:
                f.write(r.content)
                print(f"{i}完成,",end="")
        except:
            #   这里会抛出很多i可能，看爬了多少次
            self.fail.append(i)

        
    

    #启用多线程以更快的下载ts文件
    def getallfiles(self,num):
            #线程列表
            thread_list=[]
            #线程数量
            threads=range(num)
            #for循环线程加载
            for i in threads:
                print(f"therding:{i}")
                self.i=i
                #！！！！！！！！
                #十分注意，请使用target，加括号也可能导致线程无法作用如self.save_file()
                t=threading.Thread(target=self.save_file)
                #原神，启动！
                t.start()
                thread_list.append(t)
            for i in thread_list:
                i.join()

    #用于存档下载失败的文件，以防万一
    def fail_log(self):
        pass
    
    #合并ts文件
    def merge_ts(self):
        pass

            

    
if __name__=="__main__":
    n=gugufan("wuwu")
    n.getallfiles(200)
    print(n.fail)

