from PIL import Image, ImageDraw, ImageFont
import os, sys
import shutil

# 灰阶值越大，取越后面的字符
symbols = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'.   ")

#生成字符画,在第104行调用！！！！！！将缩略图转成字符串
def ascii_art_convert(src_dir, dest_dir):   #ascii_art_convert('D:\\temp_thum', 'D:\\temp_ascii')
    print('开始生成...')
    picts_list = sorted(os.listdir(src_dir))   #返回文件或文件名并排序
    len_picts = len(picts_list)

    i = 1
    #输出所有缩略图文件和文件夹，对每一张图进行操作
    for picture in picts_list:
        # 调用load_picture()函数
        (pixels, x_size, y_size) = load_picture(os.path.join(src_dir, picture))  #调用转灰度图函数

        #生成字符画图片，os.path.join()，将join（）里面的参数拼接成一个完整得路径。windows默认用\拼接。调用create_ascii_picture()函数
        create_ascii_picture(pixels, symbols,os.path.join(dest_dir, picture), x_size, y_size)  #调用灰度图转字符画

        print('正在生成中... {0}/{1}'.format(i, len_picts))
        i += 1

#在第100行调用！！！！！！
#调用PIL库形成缩略图，也就是改变图片尺寸，为后面转字符画提高效率，并临时存储
def create_thumbnail(src_dir, dst_dir):
    # os.listdir返回目录中文件名（无序的）
    # sorted默认升序排序
    picts_list = sorted(os.listdir(src_dir))

    for picture in picts_list:
        base_name = os.path.basename(picture)
        img = Image.open(os.path.join(src_dir, picture))
        size = 200, 200
        img.thumbnail(size, Image.ANTIALIAS)
        img.save(os.path.join(dst_dir, base_name))



#在第17行调用！！！！！！
#将图片转为灰度图
def load_picture(filename):

    # Gray = R*0.299 + G*0.587 + B*0.114  灰度公式
    #在这里直接调用PIL库实现
    img = Image.open(filename).convert('L')
    (x, y) = img.size

    pixels = list(img.getdata())
    img.close()
    return (pixels, x, y)


#在第21行调用！！！！！！
#将灰度图的每一个像素点替换为相应的字符
def create_ascii_picture(pixels, symbols, dest_name, x_size, y_size):
    scale = 4    # 长宽扩大倍数
    border = 1  # 边框宽度

    interval_pixel = 2     #原图片间隔多少个像素点来填充，使图片看起来不密集，提高转化时间

    img = Image.new('L',(x_size*scale + 2*border,y_size*scale + 2*border),255)
    fnt = ImageFont.truetype('C:\Windows\Fonts\Arial.ttf', int(scale*3))    #C:\Windows\Fonts\Arial.ttf  是计算机上字体的文件路径
    t = ImageDraw.Draw(img)

    x = border
    y = border
    for j in range(0, y_size, interval_pixel):
        for i in range(0, x_size, interval_pixel):
            t.text((x, y),symbols[int(pixels[j*x_size + i]/256 * len(symbols))],font=fnt,fill=0)
            x += scale * interval_pixel
        x = border
        y += scale * interval_pixel

    img.save(dest_name, "JPEG")    #将所有替换后的字符画成一张字符画

#创建目录
def start_convert(src_file):
    # 将视频分割成的图片，存放在D:\\temp_pic
    if not os.path.exists('D:\\temp_pic'):
        os.mkdir('D:\\temp_pic')
    # 将视频分割成的图片生产缩略图，存放在D:\\temp_thum
    if not os.path.exists('D:\\temp_thum'):
        os.mkdir('D:\\temp_thum')

    if not os.path.exists('D:\\temp_ascii'):
        os.mkdir('D:\\temp_ascii')


    #分离音频
    slice_audio_cmd = 'ffmpeg.exe -i {0} -vn D:\\temp.mp3'.format(src_file)  #D:\\temp.mp3是临时保存分离音频的路径
    os.system(slice_audio_cmd)    #os.system（)将字符串转化为命令在服务器上运行(在shell中执行命令)

    #分割视频为若干图片
    slice_pic_cmd = 'ffmpeg.exe -i {0} -r 24 D:\\temp_pic/%06d.jpeg'.format(src_file)  #分割图片的命令，D:\\temp_pic临时是保存切割好的图片的路径
    os.system(slice_pic_cmd)


    #生成缩略图，调用create_thumbnail()函数
    create_thumbnail('D:\\temp_pic', 'D:\\temp_thum')     #调用了前面定义的函数 D:\\temp_thum是临时保存缩略图的路径


    #生成字符画，调用ascii_art_convert()函数
    ascii_art_convert('D:\\temp_thum', 'D:\\temp_ascii')    #调用了前面定义的函数，保存字符画图片D:\\temp_ascii

    #合成字符视频
    dst_name = os.path.join(os.path.dirname(src_file), 'ascii_' + os.path.basename(src_file))    #os.path.dirname(path) 拼接转换结果文件名F:\\ascii_latata.mp4
    merge_ascii_video_cmd = 'ffmpeg -threads 2 -start_number 000001 -r 24 -i {0}/%06d.jpeg -i D:\\temp.mp3 -vcodec mpeg4 {1}'.format('D:\\temp_ascii', dst_name)
    os.system(merge_ascii_video_cmd)

    print('生成完成！')

#删除一些临时的文件及文件夹
    if os.path.exists('D:\\temp_pic'):
        shutil.rmtree('D:\\temp_pic')     #递归地删除分割视频得到的图

    if os.path.exists('D:\\temp_thum'):
        shutil.rmtree('D:\\temp_thum')    #递归地删除缩略图文件

    if os.path.exists('D:\\temp_ascii'):
        shutil.rmtree('D:\\temp_ascii')  # 递归地删除字符画图片

    if os.path.exists('D:\\temp.mp3'):
        os.remove('D:\\temp.mp3')


if __name__ == '__main__':
    src_file = 'F:\\latata.mp4'      #待转换视频的文件路径
    start_convert(src_file)   #调用函数

