from glob import glob
from os import remove, rename

subtitles = glob("*.ass")
find = 'WrapStyle: 0\n'
insert = 'ScaledBorderAndShadow: yes\n'

for file in subtitles:
    with open(file, 'r', encoding='utf-8') as f_in, open('_' + file, 'w', encoding='utf-8') as f_out:
        prev_line = ''
        is_inserted = False 
        for line in f_in:
            if not is_inserted and prev_line == find and line != insert:
                f_out.write(insert)
                is_inserted = True 
            f_out.write(line)
            prev_line = line
    try: 
        remove(file)
    except Exception as e: 
        print(f"{file}: {e}")
        continue 
    try: 
        rename('_' + file, file)
    except Exception as e: 
        print(f"{file}: {e}")
        continue