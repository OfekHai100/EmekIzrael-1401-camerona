import os

def main():
    path = "validation\\female\\"
    dst = "validation\\female1\\"
    images = os.listdir(path)
    i = len(os.listdir(dst)) + 1
    break_at = int(input("how much photos to transfer? "))
    for image_path in images:
        if i == break_at:
            break
        input_path = os.path.join(path, image_path)
        output_path = os.path.join(dst, str(i)+'.jpg')
        os.rename(input_path, output_path)
        i += 1

if __name__ == '__main__':
    main()