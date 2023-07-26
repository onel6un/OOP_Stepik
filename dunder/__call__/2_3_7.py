class RenderList:
    def __init__(self, type_list):
        self.type_list = type_list

    def __call__(self, lst):
        if self.type_list == "ol":
            return (
                '<ol>'
                + ''.join(list(map(lambda x: f'\n<li>{x}</li>', lst)))
                + '\n</ol>'
            )
        return (
            '<ul>'
            + ''.join(list(map(lambda x: f'\n<li>{x}</li>', lst)))
            + '\n</ul>'
        )
