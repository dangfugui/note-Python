check_du_file = "/srv/dev-disk-by-label-share/_python/du_all.txt"
with open(check_du_file,encoding='utf-8') as f:
    for line  in f.readlines():
        print(line) # line.find('13x')