from bs4 import BeautifulSoup
import requests
import time


def sendLineNotify():
    lineNotifyToken = "Your Token"
    lineNotifyApi = "Your API"
    headers = {"Authorization": f"Bearer {lineNotifyToken}"}
    data = {"message": "販売開始しましたhttps://humanmade.jp/products/hm23te024"}
    requests.post(lineNotifyApi, headers=headers, data=data)
    
def detect_updates():
    url = 'https://humanmade.jp/products/hm23te024'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')

    # パックTのエレメント
    new_elem = str(soup.select_one('.product-form'))

    try:
        with open('old_elem.txt') as f:
            old_elem = f.read()
    except:
        old_elem = ''

    if new_elem == old_elem:
        print('変化なし')
        return False
    else:
        with open('old_elem.txt', 'w') as f:
            f.write(new_elem)
        print('Webページが更新されました')
        sendLineNotify()
        return True
    
    
    
while(True):
    detect_updates()
    print("トラッキングしました")
    time.sleep(60 * 5)
    print('再度収集します')