import os

folders = os.listdir('.')

for folder in folders:
    if folder in ['images', 'static', 'pages']: continue 
    if os.path.isdir(folder)==False: continue
    for fn in os.listdir(folder):
        fpath = os.path.join( folder, fn)
        if os.path.isdir(fpath): continue
        print fpath
        with open(fpath, 'r') as f:
            content = ''.join( f.readlines() )
        new_content = content.replace('![](images', '![](../images'  )
        with open(fpath, 'w') as f:
            f.write(new_content)
    
