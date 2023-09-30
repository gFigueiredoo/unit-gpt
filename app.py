import git

def clonar_repositorio(url, destino):
    git.Repo.clone_from(url, destino)

if __name__ == "__main__":
    url_do_repositorio = "https://github.com/usuario/repositorio.git"
    destino_do_clone = "C:\Users\elisi\Desktop\gabriel\test"
    
    clonar_repositorio(url_do_repositorio, destino_do_clone)
