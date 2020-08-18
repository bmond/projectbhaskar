import sys
import math
import itertools
import random
from PIL import Image
    
def shuffle_order(size, shuffle_seed):
    order = []
    for i in range (size):
        order.append(i)
    print("Suffle Seed",shuffle_seed)
    if (shuffle_seed):
        random.seed(shuffle_seed)
        shuffled = random.shuffle(order)
        return order
    else:
        return order
    
def encrypt(plain, key):
    cipher = []
    k = 0
    len_key = len(key)
    len_plain = len(plain)
    for i in range(len_plain):
        cipher.append((plain[i] + ord(key[i % len_key])) % 256)
    return cipher

def decrypt(cipher, key):
    plain = []
    k = 0
    len_key = len(key)
    len_cipher = len(cipher)
    for i in range(len_cipher):
        plain.append((cipher[i] + 256 - ord(key[i % len_key])) % 256)
    return plain


def readLSB(image, width, binary, order):
    bit = []
    px = image.load()
    imwidth, imheight = image.size
    k = 0
    cur = 0
    for pos in order:
        i = pos / width
        j = pos % width
        if (binary):
            cur |= (px[i % imwidth, j % imheight] & 1) << k
        else:
            cur |= (px[i % imwidth, j % imheight][0] & 1) << k
        k += 1
        if (k >= 8):
            bit.append(cur)
            k = 0
            cur = 0
    if (k > 0):
        bit.append(cur)
    return bit

def psnr(watermarkedcover, plaincover):
    return 20 * math.log10(255/rms(watermarkedcover, plaincover))

def rms(image_a,image_b):
    px_a = image_a.load()
    width_px_a, height_px_a = image_a.size
    px_b = image_b.load()
    width_px_b, height_px_b = image_b.size
    sum=0;
    for i in range(width_px_a):
        for j in range(height_px_a):
            p_a = px_a[i,j]
            p_b = px_b[i,j]
            sum += math.pow((p_a[0] - p_b[0]), 2) + math.pow((p_a[1] - p_b[1]), 2) + math.pow((p_a[2] - p_b[2]), 2)

    return math.sqrt(sum / (width_px_a * height_px_a) / 3)


def extract_lsb(inputpath, outputpath):
    cover = Image.open(inputpath)
    lsb = Image.new("1", cover.size);
    width, height = cover.size
    px_cover = cover.load()
    px_lsb = lsb.load()

    #key = input("enter keys: ")
    key = "bhaskar"
    seed = 0
    key_size = len(key)
    for i in range(key_size):
        seed += ord(key[i])
    cipher = readLSB(cover, width, 0, shuffle_order(width * height, seed))
    plain = decrypt(cipher, key)

    k = 0
    cur = 0
    positions = shuffle_order(width * height, 0)
    for pos in positions:
        i = pos % width
        j = pos % height
        px_lsb[i, j] = ((plain[int(k / 8)] >> (k % 8)) & 1)
        k = (k + 1)
    lsb.save(outputpath);
    lsb.show();

def insert_lsb(inputpath, watermarkpath, outputpath):
    cover = Image.open(inputpath)
    height,width = cover.size
    print(width)
    watermark = Image.open(watermarkpath).convert("1")
    output = Image.new(cover.mode, cover.size)
    px_cover = cover.load()
    print(cover.size)
    px_watermark = watermark.load()
    px_output = output.load()
    plain = readLSB(watermark, width, 1, shuffle_order(width * height, 0))
    #key = input("enter keys: ")
    key = "bhaskar"
    cipher = encrypt(plain, key)
    #print(cipher)
    k = 0
    cur = 0
    wm_height,wm_width = watermark.size
    mod = wm_width * wm_height
    seed = 0
    key_size = len(key)
    for i in range(key_size):
        seed += ord(key[i])
    positions = shuffle_order(width * height, seed)
    print(width * height)
    for pos in positions:
        i = pos / width
        j = pos % width
        #print("Value of I J",i,j)
        #print("Print Type of px_cover" , px_cover[i,j])
        p = list(px_cover[i,j])
        p[0] = (p[0] & 0b11111110) | ((cipher[int(k / 8)]>>(k % 8)) & 1)
        k = (k + 1) % mod
        px_output[i, j] = tuple(p)
    output.save(outputpath)
    output.show()

def print_psnr(watermarkedpath, plainpath):
    watermarked = Image.open(watermarkedpath)
    plain = Image.open(plainpath)

    print("PSNR: " + str(psnr(watermarked, plain))) 

def main():
    insert_lsb("test/ganesha.jpg", "test/Lenna.png", "test/Lenna_watermark.jpg")
# =============================================================================
#     cmd = input("enter selection (i)nsert / (e)xtract: ")
#     if cmd == 'i':
#         insert_lsb(str(sys.argv[1]), str(sys.argv[2]), str(sys.argv[3]))
#         print("Original image:", sys.argv[1])
#         print("Watermark image:", sys.argv[2])
#         print("Image with watermark:", sys.argv[3])
#         print("Analyzing...")
#         print_psnr(str(sys.argv[1]), str(sys.argv[3]))
#     else:
#         print("Image with watermark:", sys.argv[1])
#         print("Extracted watermark:", sys.argv[2])
#         extract_lsb(str(sys.argv[1]), str(sys.argv[2]))
# =============================================================================

if __name__ == '__main__':
    main()
