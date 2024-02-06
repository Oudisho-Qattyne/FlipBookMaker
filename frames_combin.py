from PIL import Image , ImageDraw
from pathlib import Path
import os
import math
class FramesCombine :
    def __init__(self , out_dir , vid):
        self.out_dir = out_dir
        self.vid = vid
    
    def create_dir_if_not_exists(self, dirname: str):
        """Create a directory with the specified name inside the 'out_dir' 
        directory if it doesn't exist.
        :param dirname: Name of the directory to be created.
        :return: created dir path.
        """
        target_dir = Path.joinpath(self.out_dir, dirname)
        if not target_dir.exists():
            target_dir.mkdir(parents=True, exist_ok=True)
        else:
            return target_dir
        return target_dir
    
    def combine(self):
        A4 = Image.open('A4.jpg')
        final_result = self.create_dir_if_not_exists(self.vid)
        new_dir = Path.joinpath(self.out_dir ,'re_size_frames' + self.vid )
        img=Image.open( Path.joinpath(new_dir , os.listdir(new_dir)[0]))
        rows_number = A4.height//img.height
        number_of_images = len([name for name in os.listdir(new_dir) if os.path.isfile(os.path.join(new_dir, name))])
        number_of_pages = math.ceil(number_of_images/(rows_number*2))
        print(rows_number)
        print(number_of_images)
        print(number_of_pages)
        for i in range(number_of_pages):
            orig_file_location = f"{final_result}/{i}.jpg"
            # new_image = Image.open('A4.jpg')
            new_image = Image.new('RGB',(A4.width,A4.height), (250,250,250))
            counter = 0
            rows = 0
            # print(image_counter*rows_number*2)
            # print(image_counter*rows_number*2 + rows_number*2 )
            for j in range(i*rows_number*2 +1,i*rows_number*2 + rows_number*2 +1): 
                if j<number_of_images:
                    
                    # if  os.path.isfile(os.listdir(Path.joinpath(self.out_dir ,'re_size_frames' ))[j]):
                        print(j)
                        # Check whether file is in text format or not 
                        if os.listdir(new_dir)[j].endswith(".jpg"): 
                            # while(counter <3):
                                img = Image.open(f"{new_dir}/{j}.jpg")
                                draw = ImageDraw.Draw(img)
                                draw.text((6, 6), str(j) , fill='white' , )
                                # if counter == 0:
                                if counter%2 != 0:
                                    # new_image.paste(img , (0,int(img.height*counter)))
                                    new_image.paste(img , (0,img.height*rows))
                                    rows+=1
                                else:
                                    # new_image.paste(img , (img.width,int(img.height*(counter-1))))
                                    new_image.paste(img , (img.width,img.height*rows))

                                counter += 1
            new_image.save(orig_file_location,'JPEG')
            