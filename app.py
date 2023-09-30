import requests

def getFile(username, repoName, fileName):
    url = f"https://api.github.com/repos/{username}/{repoName}/contents/{fileName}"
    response = requests.get(url)
    
    if response.status_code == 200:
        item = response.json()
        if item["type"] == "file":
            fileContent = requests.get(item["download_url"]).text
            return fileContent
        else:
            print(f"{fileName} não é um arquivo.")
            return None
    else:
        print(f"Não foi possível obter o conteúdo do arquivo {fileName}. Código de status: {response.status_code}")
        return None

def createFile(fileName, content):
    try:
        with open(fileName, "w", encoding="utf-8") as arquivo:
            arquivo.write(content)
        print(f"Arquivo {fileName} criado com sucesso.")
    except Exception as e:
        print(f"Ocorreu um erro ao criar o arquivo {fileName}: {str(e)}")

if __name__ == "__main__":
    username = "gFigueiredoo"
    repoName = "unit-gpt"
    fileName = "test.py"
    
    fileContent = getFile(username, repoName, fileName)
    
    if fileContent is not None:
        filePath = f"files-generated/{fileName}.txt"
        createFile(filePath, fileContent)
