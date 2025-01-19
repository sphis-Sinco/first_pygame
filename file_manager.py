assets_folder = "assets/"
images_folder = f"{assets_folder}images/"

def imageAsset(asset):
    return f'{images_folder}{asset}'

def playerAsset(asset):
    return imageAsset(f'player/{asset}')