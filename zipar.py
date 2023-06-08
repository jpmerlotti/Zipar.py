import os
import zipfile

def zip_directory(directory_path, zip_path):
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Adiciona o arquivo index.html ao arquivo zip
        index_html_path = os.path.join(directory_path, 'index.html')
        if os.path.exists(index_html_path):
            zipf.write(index_html_path, 'index.html')
        
        # Adiciona a pasta src ao arquivo zip
        src_path = os.path.join(directory_path, 'src')
        if os.path.exists(src_path):
            for root, dirs, files in os.walk(src_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    zip_path = os.path.relpath(file_path, src_path)
                    zipf.write(file_path, os.path.join('src', zip_path))

# Diretório da pasta onde estão os arquivos
diretorio_origem = r'D:\Projetos\HTML\SiteFatec'

# Caminho completo com o nome do arquivo zip
arquivo_zip_destino = r"D:\Projetos\HTML\SiteFatec.zip"

# Compacta o diretório especificado
zip_directory(diretorio_origem, arquivo_zip_destino)