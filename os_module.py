# OS MODULE--------------------------------------------------------------------
import os
from datetime import datetime

# print(os.name)  # გამოაქვს შესაბამის ოპერატიულის სახელი (nt- ვინდოუსის; posix-mac)
# print(dir(os))
# print(os.getcwd())  # იმ დირექტორიის მისამართი რომელშიც ვიმყოფებით
#
# os.chdir("C:/Users/User/PycharmProjects/BTU/moduls/os")  # მოდულისთვის მდებარეობის შესაცვლელად
# print(os.getcwd())  # შეცვლილი მდებარეობა
#
# print(os.listdir())  # ფაილების ლისთი მოცემულ ადგილას
#
# os.mkdir("images-1")  # გამოიყენება დირექტორიის შესაქმნელად მოცემული, შესაძლებელია მხოლოდ ერთი დირექტორიის შექმნა
# os.makedirs("images-2/sub-dir")  # გამოიყენება დირექტორიის შესაქმნელად, შესაძლებელია ქვედა დონის დირექტორიის შექმნაც
#
# os.rmdir("images-1")  # გამოიყენება მხოლოდ მაღალ ლეველიანი დირექტორიის წასაშლელად
# os.removedirs("images-2/sub-dir")  # შესაძლებელია მითითებული ყველა დირექტორიის ჭაშლა
#
# os.rename("images-1", "image")  # გამოიყენება ფაილის სახელის შესაცვლელად
#
# print(os.stat('text.txt'))  # მოცემულ ფაილზე მთელი იმფორმაციის მისაღებად,
# print(os.stat("text.txt").st_size)  # ფაილის ბაიტების რაოდენობა
# print(os.stat("text.txt").st_mtime)  # ბოლო მოდიფიაკაციის დრო
# mod_time = os.stat("text.txt").st_mtime
# print(datetime.fromtimestamp(mod_time))  # ბოლო მოდიფიკაციის დროის ნორმალური დროით ჩვენება
#
# # walk ფუნქციის გამოყენებით შესაძლებელია მისამართის მიხედვით დირექტორიისა და მასში არსებული ფაილების შესახებ ინფორმირება
# for dirpath, dirnames, filenames in os.walk("C:/Users/User/PycharmProjects/BTU/moduls/os"):
#     # ასევე გამოაქვს მასში არსებული ქვედირექტორიის შესახებ ინფორმაცია
#     print("Current Path: ", dirpath)
#     print("Directories: ", dirnames)
#     print("Files: ", filenames)
#
# print(os.environ.get("HOMEPATH"))  # აჩვენებს ჰოუმ დირექტორიას
# for item, value in os.environ.items():  # გამოაქვს სამუშაო გარემოს შესახებ ინფორმაცია
#     print("{}: {}".format(item, value))

# # ჰოუმ დირექტორიაში ამატებს პარამეტრად გადაცემულ ფაილს
# file_path = os.path.join(os.environ.get("HOMEPATH"), "test.txt")
# print(file_path)
#
# print(dir(os.path))
# print(os.path.basename("/temp/test.txt"))  # რენდომულად აღებული ფაილის სახელი
# print(os.path.dirname("/temp/text.txt"))  # აბრუნებს დირექტორიის სახელი
# print(os.path.split("/temp/text.txt"))  # დირექტორიისა და ფაილის სახელის დასპლიტვა
# print(os.path.exists("/temp/text.txt"))  # ფაილის არსებობის შემოწმება
# print(os.path.isdir("/temp/text.txt"))  # არის თუ არა დირექტორია
# print(os.path.isfile("/temp/text.txt"))  # არის თუ არა ფაილი
# print(os.path.splitext("/temp/text.txt"))  # რა ტიპისაა ფაილი extention


# print(os.getcwd())  # ლოკალური დირექტორიის ფაზის ჩვენება
# os.chdir("/Users/User/PycharmProjects/BTU/moduls/os/images")  # images დირექტორიაში გადასვლა
# # print(os.getcwd())  # ახალი ლოკაციის ჩვენება
# n = 1
# for i in os.listdir():
#     name, format = os.path.splitext(i)  # სახელისა და ფორმატის გაყოფა
#     new_name = os.rename(i, f"image{n}{format}")
#     n += 1
