from pysesame3.auth import WebAPIAuth
from pysesame3.lock import CHSesame2
from zmq import device
# Japanese and English
# based on this site(JP): https://zenn.dev/key3/articles/6c1c2841d7a8a2

def get_device():
    # 使い方 Usage of library: https://pysesame3.readthedocs.io/en/latest/usage/
    # APIの取得方法 get API from this site: https://partners.candyhouse.co/login
    # ログインの前にサインアップが必要かも before login, you may have to sign up
    auth = WebAPIAuth(apikey="your API key")
    # Sesame3's UUID
    your_key_uuid = "your sesame UUID"

    # 前段の手順で取得した秘密鍵の HEX 文字列 Private Key
    # follow this site: https://zenn.dev/key3/articles/6c1c2841d7a8a2
    # you should translate the page if you read English only
    your_key_secret = "your secret key"

    sesame = CHSesame2(
        authenticator=auth,
        device_uuid=your_key_uuid,
        secret_key=your_key_secret,
    )
    return sesame

def unlock():
    # 解錠処理。 `My Script` はヒストリに記録される文字列。
    # unlock, 'My Script' is the string recored on the history
    get_device().unlock(history_tag="My Script")

def lock():
    # 施錠処理。 `My Script` はヒストリに記録される文字列。
    # lock, 'My Script' is the string recored on the history
    get_device().lock(history_tag="My Script")

def toggle():
    # トグル処理。 `My Script` はヒストリに記録される文字列。
    # toggle, 'My Script' is the string recored on the history
    get_device().toggle(history_tag="My Script")

if __name__ == "__main__":
    unlock()
    lock()
    toggle()