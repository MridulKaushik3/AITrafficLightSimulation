from icrawler.builtin import GoogleImageCrawler

# google_crawler = GoogleImageCrawler(storage={'root_dir': 'ambulance_data/ambulance'})
# google_crawler.crawl(keyword='ambulance on road', max_num=300)

# google_crawler = GoogleImageCrawler(storage={'root_dir': 'ambulance_data/non_ambulance/x'})
# google_crawler.crawl(keyword="vehicles at traffic signal", max_num=400)



import os

folder_path = 'ambulance_data/non_ambulance'
start_index = 1  # Starting from 0000058

# Sort files to rename in order
files = sorted(os.listdir(folder_path))

# Loop through and rename each file
for i, filename in enumerate(files):
    ext = os.path.splitext(filename)[1]  # Get file extension (e.g., '.jpg')
    new_name = f"{i + start_index:07d}{ext}"  # 7-digit number with leading zeros
    src = os.path.join(folder_path, filename)
    dst = os.path.join(folder_path, new_name)

    os.rename(src, dst)

print("Renaming complete.")
# import os, random, shutil

# folder = 'ambulance_data/non_ambulance'
# files = os.listdir(folder)
# random.shuffle(files)

# for i, fname in enumerate(files):
#     ext = os.path.splitext(fname)[-1]
#     new_name = f"non_{i:04d}{ext}"
#     os.rename(os.path.join(folder, fname), os.path.join(folder, new_name))
