"""
データ型：UserName
    属性：
        実際のユーザ名
    ルール：
        ユーザ名は４文字以上２０文字以内である
    できること：
        ユーザ名を大文字に変換する
"""


class UserName:
    def __init__(self, name):
        # ４文字以上２０文字以内のチェック
        if not (len(name) >= 4 and len(name) <= 20):
            raise ValueError(f"{name}はルール違反です。")
        self.name = name

    def screen_name(self):
        return self.name.upper()


tanaka = UserName(name="tanaka")
# bob = UserName(name="bob")

print(tanaka.screen_name()
)
# print(bob.name)
