Title: 用pandoc自由转换markdown与html格式
Slug: 用pandoc自由转换markdown与html格式
Tags: markdown
Date: 2012-06-07

markdown虽然写起来方便, 但是要预览的话还要用ReText打开, 而且ReText好像是Qt程序, 打开文件时不如别的编辑器那么流畅. 所以想找一个可以把markdown文件变成html格式的工具.

我甚至搜了很久"markdown2html"(github上居然可以搜到好几个项目...) 而没有注意到, 在终端输入"html2markdown"时显示的警告:

    $ html2markdown
    程序“html2markdown”尚未安装。  您可以使用以下命令安装：
    sudo apt-get install pandoc

后来安装了pandoc(`sudo apt-get install pandoc`), 其实只要看看帮助就知道咋用了: 

    $ pandoc -h
    pandoc [OPTIONS] [FILES]
    Input formats:  native, markdown, markdown+lhs, rst, rst+lhs, html, latex, latex+lhs
    Output formats:  native, html, html+lhs, s5, docbook, opendocument, odt, latex, latex+lhs, context, texinfo, man, markdown, markdown+lhs, plain, rst, rst+lhs, mediawiki, rtf
    Options:
      -f FORMAT, -r FORMAT  --from=FORMAT, --read=FORMAT                    
      -t FORMAT, -w FORMAT  --to=FORMAT, --write=FORMAT                     
      -s                    --standalone                                    
      -o FILENAME           --output=FILENAME                               
      -p                    --preserve-tabs                                 
                            --tab-stop=TABSTOP                              
                            --strict                                        
                            --reference-links                               
      -R                    --parse-raw                                     
      -S                    --smart                                         
      -m[URL]               --latexmathml[=URL], --asciimathml[=URL]        
                            --mathml[=URL]                                  
                            --mimetex[=URL]                                 
                            --jsmath[=URL]                                  
                            --gladtex                                       
      -i                    --incremental                                   
                            --xetex                                         
      -N                    --number-sections                               
                            --no-wrap                                       
                            --sanitize-html                                 
                            --email-obfuscation=none|javascript|references  
                            --id-prefix=STRING                              
                            --indented-code-classes=STRING                  
                            --toc, --table-of-contents                      
                            --base-header-level=LEVEL                       
                            --template=FILENAME                             
      -V FILENAME           --variable=FILENAME                             
      -c URL                --css=URL                                       
      -H FILENAME           --include-in-header=FILENAME                    
      -B FILENAME           --include-before-body=FILENAME                  
      -A FILENAME           --include-after-body=FILENAME                   
      -C FILENAME           --custom-header=FILENAME                        
      -T STRING             --title-prefix=STRING                           
                            --reference-odt=FILENAME                        
      -D FORMAT             --print-default-template=FORMAT                 
                            --data-dir=DIRECTORY                            
                            --dump-args                                     
                            --ignore-args                                   
      -v                    --version                                       
      -h                    --help       
