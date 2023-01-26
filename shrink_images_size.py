import os
import tinify
from dotenv import load_dotenv

load_dotenv()

tinify.key = os.getenv('key')

root_dir = 'input'        

def check_if_file_exist(file):
    
    curr_dir = ''
    
    for subdir, dirs, files in os.walk('output'):
        for f in dirs:
            curr_dir = os.path.join(subdir, f, file)
            #print(curr_dir)

            if os.path.isfile(curr_dir):
                
                return True
            
            else:
                return False
    
if __name__ == '__main__':    

    for subdir, dirs, files in os.walk(root_dir):
        for file in files:
            if not check_if_file_exist(file):
                source = tinify.from_file(os.path.join(subdir, file))
                file_arr = file.split(' ')
                file = '_'.join(file_arr)
                print(file)
                arr = subdir.split('/')
                arr[0] = 'output'
                for i in range(len(arr)):
                    if arr[i] != 'output' and arr[i] != str(file):
                        second_dir = arr[i].split(' ')
                        arr[i] = '_'.join(second_dir)
                output_dir = '/'.join(arr)
                if not os.path.isdir(output_dir):
                    os.makedirs(output_dir)
                source.to_file(os.path.join(output_dir, file))

            
            