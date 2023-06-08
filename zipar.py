import os, zipfile

def zip_directory(directory_path, zip_path):
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Adiciona o arquivo index.html ao arquivo zip
        # Adds the index.html file to the zip file
        index_html_path = os.path.join(directory_path, 'index.html')
        if os.path.exists(index_html_path):
            zipf.write(index_html_path, 'index.html')
        
        # Adiciona a pasta src ao arquivo zip
        # Add src folder to zip file
        src_path = os.path.join(directory_path, 'src')
        if os.path.exists(src_path):
            for root, dirs, files in os.walk(src_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    zip_path = os.path.relpath(file_path, src_path)
                    zipf.write(file_path, os.path.join('src', zip_path))

# Diretório da pasta onde estão os arquivos
# Directory of the folder where the files are
origin_path = r""

# Caminho completo com o nome do arquivo zip
# Full path with zip file name
zip_file_path = r""

# Compacta o diretório especificado
# Compresses the specified directory
zip_directory(diretorio_origem, arquivo_zip_destino)
