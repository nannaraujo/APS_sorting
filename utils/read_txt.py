import os

def read_file_content():
    txt_files = [file for file in os.listdir("Resources/") if file.split(".")[1] == "txt"]
    for i,item in enumerate(txt_files):
        print(f"{i}- {item}")
    user_select = input("Selecione a pasta: ")

    if user_select == "0":
        selected_file = txt_files[0]
    elif user_select == "1":
        selected_file = txt_files[1]
    elif user_select == "2":
        selected_file = txt_files[2]
    else:
        print("Nenhuma opção valida foi selecionada")
    
    with open(os.path.join("Resources",selected_file),"r") as file:
        list_of_numbers = [int(i.strip("\n")) for i in file]
    return selected_file,list_of_numbers