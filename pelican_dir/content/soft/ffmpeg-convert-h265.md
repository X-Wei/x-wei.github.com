Title: 用ffmpeg压缩视频(H265)
Date: 2021-07-15
Slug: ffmpeg-convert-h265
Tags: linux

DJI运动相机拍摄的视频体积都比较大, 查了一下因为encoding是H264, 如果改成H265的话压缩率会高很多.

转换的命令是: (ref. [stackoverflow](https://stackoverflow.com/questions/58742765/convert-videos-from-264-to-265-hevc-with-ffmpeg))

    ffmpeg -i input.mp4 -c:v libx265 -vtag hvc1 output.mp4

加上`-qscale 0`可以保持quality (不过好像对h265不管用? ref. [stackoverflow](https://stackoverflow.com/questions/25569180/ffmpeg-convert-without-loss-quality))


## 保留metadata

视频的metadata里有拍摄时间之类的内容, 可以用`-movflags use_metadata_tags` 或者`-map_metadata 0`将其保存下来 (ref: [stackexchange](https://video.stackexchange.com/questions/23741/how-to-prevent-ffmpeg-from-dropping-metadata))

要查看一个视频文件的metadata的话:

    $ sudo apt-get install mediainfo
    $ mediainfo foo.mp4 > info.txt

**例子**:

    $ time ffmpeg -i input.MP4 -c:v libx265 \
      -movflags use_metadata_tags -map_metadata 0 \
      -vtag hvc1 output.MP4

==> 用时370秒, 把一个416MB的文件压缩到了33MB

## 批量处理fish脚本


给converted文件加一个h256前缀:

```sh
for fn in (ls *.MP4)
  if string match -rq -- "h265" $fn;
    echo skipping $fn; # skip files with "h265" in the name
  else;
    ffmpeg -i $fn -c:v libx265 -movflags use_metadata_tags -map_metadata 0 -vtag hvc1 h265_$fn;
  end
end
```

或者把converted的文件放进子文件夹"h265"里头:

```sh
mkdir h265
time for fn in (ls *.MP4)
  ffmpeg -i $fn -c:v libx265 -movflags use_metadata_tags -map_metadata 0 -vtag hvc1 h265/$fn
end
```

