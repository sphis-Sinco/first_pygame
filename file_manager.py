assets_folder = "assets/"
images_folder = f"{assets_folder}images/"

def imageAsset(asset):
    return f'{images_folder}{asset}.png'

def playerAsset(asset):
    return imageAsset(f'player/{asset}')