class Application():
    def __init__(self, name) -> None:
        self.name = name
        self.blocked = False


class AppStore():
    apps = []

    def add_application(self, app):
        self.apps.append(app)

    def remove_application(self, app):
        self.apps.remove(app)

    def block_application(self, app):
        app.blocked = True

    def total_apps(self):
        return len(self.apps)
