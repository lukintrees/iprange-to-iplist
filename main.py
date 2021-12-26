filein = input("file: ")
fileout = input("file out: ")
file = open(filein, "w")
lines = file.readlines()
file1 = open(fileout, "w")
for line in lines:
    print(line.strip())
    line = line.strip()
    ips = line.split('-')
    ip1 = ips[0]
    ip2 = ips[1]
    i = 1
    part1 = ip1.split('.')
    part1[0] = int(part1[0])
    part1[1] = int(part1[1])
    part1[2] = int(part1[2])
    part1[3] = int(part1[3])
    file1.write(ip1 + "\n")
    while True:
        part1[3] = part1[3] + 1
        if part1[3] == 256:
            part1[3] = 0
            part1[2] = part1[2] + 1
            if part1[2] == 256:
                part1[2] = 0
                part1[1] = part1[1] + 1
                if part1[1] == 256:
                    part1[1] = 0
                    part1[0] = part1[0] + 1
        ip13 = f"{part1[0]}.{part1[1]}.{part1[2]}.{part1[3]}"
        i = i + 1
        file1.write(ip13 + "\n")
        if ip13 == ip2:
            break
file1.close()
